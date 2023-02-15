Türkçe

Kodun çalışması için gereksinimler:

1.Redis sunucusunu kurmalısınız.

2.Discord sunucunuz'a webhook url'i entegre etmelisiniz(tanımlamalısınız).(Ben discord webhook kullandım.Siz farklı bir webhook kullanabilirsiniz.Kullandığınız web hooku kodda tanımlamalısınız.)

Kod nasıl çalışır:

Öncelikle Securitytrails api anahtarınızı tanımlayın.(Koda farklı api key'lerde tanımlayabilirsiniz)
Discord webhook url'inizi tanımlayın.

Python kodu, domains değişkeni içerisindeki root domainlerinin,securitytrails'te tanımlı subdomainlerini, api key vasıtası ile çekerek ,redis sunucusunda depolanmasını sağlar.

sleep(int) int değişkeni içerisine yazdığımız değer secutriytrails'in api'ine kaç saat/dakikada bir istek atılacağı değeri belirtir.
Örneğin, 3 saat olarak belirleyecekseniz: sleep(10800)

Üç saatte bir securitytrails'e belirtilen domainlerin, subdomainlerine istek atar.Daha önce redis sunucusunda depolanan subdomainler, yeni atılan istekteki(3 saat sonra)subdomainlerde bulunmazsa.Discord webhookuna -> {domain} için Yeni subdomain bulundu {{Subdomain}} bildirisi gönderilir.

Her atılan istekte bulunmayan subdomainler eş zamanlı olarak redis sunucusuna da eklenir.

Redis sunucusunu yükleyip,kurduktan sonra:

  "redis-server &" komutu ile redis sunucunuzu başlatabilirsiniz.

  "redis-cli" komutu ile redis komut satırına ulaşabilirsiniz.

  'KEYS *' komutu ile varolan keylerinizi görüntüleyebilirsiniz. :

      Domain değişkenine tanımladığınız root domainler, redis'te anahtar şeklinde depolanır. Örneğin:
        domain = ["x.com", "y.com"]
       
/
redis-cli

KEYS *

x.com_subdomains

y.com_subdomains
/

Rediste depolanan verileri görüntülemek için bir python kodu ekledim.

Hangi key'de depolanan veriyi görüntelemek istiyorsanız ona göre KEYS değişkenini değiştirebilirsiniz.

Rediste, anahtarlarda depolanan verileri silmek için de bir python kodu ekledim.
  

Redis sunucusunu kurmak için bu siteyi ziyaret edip faydalanabilirsiniz: https://redis.io/docs/getting-started/installation/install-redis-on-linux/


English


Requirements for the code to work:

You must install Redis server.
Create a bot by getting a Discord webhook domain. (I used Discord webhook, but you can use a different webhook. We must define the webhook we use in the code.)
How the code works:

First, define your Securitytrails API key and Discord webhook URL.

The Python code stores the subdomains of the root domains defined in the "domains" variable in the Securitytrails in the Redis server.
The sleep (int) int variable tells how many hours/minutes an API request will be sent to securitytrails, for example if it is 3 hours, sleep (10800).

Every 3 hours, the code requests subdomains of the specified domains from Securitytrails. If the subdomains stored in the Redis server before are not found in the new request (3 hours later), a notification message "New subdomain found for {domain} {{Subdomain}}" is sent to the Discord webhook.

You can visit this site to install Redis server: https://redis.io/docs/getting-started/installation/install-redis-on-linux/
