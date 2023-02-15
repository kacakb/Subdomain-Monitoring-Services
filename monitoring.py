import redis
import requests
import json
import time

# Redis veritabanı bağlantısı
r = redis.Redis(host='localhost', port=6379, db=0)

# SecurityTrails api key tanımla
securitytrails_api_key = "YOUR_API_KEY"

# Discord api web hook url tanımla
webhook_url = "YOUR_DISCORD_WEB_HOOK"

# Domainleri tanımla
domains = ["domain1", "domain2"]

# Her bir saatte istekleri döngüye sok
while True:
    for domain in domains:
        securitytrails_endpoint = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
        try:
            response = requests.get(securitytrails_endpoint + "?apikey=" + securitytrails_api_key, headers={'Content-Type': 'application/json'})
            data = response.json()
        except:
            print(f"Error getting data for {domain}")
            continue

        try:
            # Subdomainleri array olarak al
            subdomains = data["subdomains"]
        except KeyError:
            print(f"Subdomains not found for {domain}")
            continue

        # Her subdomaini döngüye al
        for subdomain in subdomains:
            # Subdomainle redis veritabanında mevcut mu 
            exists = r.sismember(f"{domain}_subdomains",subdomain)

            # Eğer subdomain, rediste mevcut değilse discord webhookua mesaj gönder.
            if not exists:
                # Subdomaini redis'e ekle
                r.sadd(f"{domain}_subdomains", subdomain)

                # Eğer mevcut değilse discord web hookuna mesaj gönder
                requests.post(webhook_url, json.dumps({"content": f"New subdomain found for {domain}: " + subdomain}), headers={"Content-Type": "application/json"})

    # 1 Saat bekle
    time.sleep(3600)
