import redis
# Kütüphaneyi tanımla
# Redis database bağlantısı
r = redis.Redis(host='localhost', port=6379, db=0)

# Anahtarın adı
key = "x.com_subdomains"

# Anahtarınızın adı ne ise key değişkeni ile değiştirin.

# Anahtarın içeriğini alın
subdomains = r.smembers(key)

# Anahtarın içeriğini ekrana yazdırın
for subdomain in subdomains:
    print(subdomain.decode())
