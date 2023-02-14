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

# Loop that will run every 6 hours
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
            # Get subdomains as an array
            subdomains = data["subdomains"]
        except KeyError:
            print(f"Subdomains not found for {domain}")
            continue

        # Loop through each subdomain
        for subdomain in subdomains:
            # Check if the subdomain exists in Redis
            exists = r.sismember(f"{domain}_subdomains",subdomain)

            # Eğer subdomain, rediste mevcut değilse discord webhookua mesaj gönder.
            if not exists:
                # Add the subdomain to Redis
                r.sadd(f"{domain}_subdomains", subdomain)

                # Send a message through the Discord webhook
                requests.post(webhook_url, json.dumps({"content": f"New subdomain found for {domain}: " + subdomain}), headers={"Content-Type": "application/json"})

    # 1 Saat bekle
    time.sleep(3600)
