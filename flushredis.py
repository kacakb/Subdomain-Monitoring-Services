import redis

# Redis kütüphanesi python'da tanımlandı.Sonrasında redis sunucusuna bağlanıldı.
# r.flushall() fonksiyonu kullanılarak redisteki veriler silindi.

r = redis.Redis(host='localhost', port=6379, db=0)
r.flushall()
