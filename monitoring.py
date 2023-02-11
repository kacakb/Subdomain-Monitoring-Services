import redis
import requests
import json
import time

# Redis database bağlantısı
r = redis.Redis(host='localhost', port=6379, db=0)

# Securitytrails API endpoint'ini tanımlayın
securitytrails_api_key = "YOUR_API_KEY"
securitytrails_endpoint = "https://api.securitytrails.com/v1/domain/google.com/subdomains"

# Discord webhook url'ini tanımlayın
webhook_url = "YOUR_DISCORD_WEBHOOK_URL"


domains = ["x.com", "y.com"]
# 6 saatte bir çalışacak döngü
while True:

                securitytrails_endpoint = f"https://api.securitytrails.com/v1/domain/{domains}/subdomains"

   
response = requests.get(securitytrails_endpoint + "?apikey=" + securitytrails_api_key, headers={'Content-Type': 'application/json'})
data = response.json()

# Subdomainleri bir dizi olarak alın
subdomains = data["subdomains"]

# Her subdomain için döngü
for subdomain in subdomains:
    # Subdomaini redis'te var mı kontrol edin
    exists = r.sismember(f"{domain}_subdomains",subdomain)

    # Redis'te yoksa
    if not exists:
        # Subdomaini redis'e ekleyin
         r.sadd(f"{domain}_subdomains", subdomain)

        # Discord webhook ile mesaj gönderin
requests.post(webhook_url, json.dumps({"content": f"{domain} için Yeni subdomain bulundu: " + subdomain}), headers={"Content-Type": "application/json"})

# 6 saat bekle
time.sleep(10800)
