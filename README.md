Türkçe

Kodun çalışması için gereksinimler:
1.Redis sunucusunu kurmalısınız.
2.Discord webhook domaini alarak Bot oluşturmalısınız.(Ben discord webhook kullandım siz farklı bir webhook kullanabilirsiniz.Kullandığımız web hooku kodda tanımlamalısınız.)

Kod nasıl çalışır:

Öncelikle Securitytrails api anahtarınızı tanımlayın.Discord webhook url'inizi tanımlayın.

Python kodu domains değişkeni içerisindeki root domainlerinin,securitytrails'te tanımlı subdomainleri ,redis sunucusunda depolanmasını sağlar.
sleep(int) int değişkeni içerisine yazdığımız değer secutriytrails'in api'ine kaç saat/dakikada bir istek atılacağı değeri belirtir.
Diyelim ki 3 saat olsun sleep(10800)

3 saatte bir securitytrails'e belirtilen domainlerin, subdomainlerine istek atar.Daha önce redis sunucusunda depolanan subdomainler, yeni atılan istekteki(3 saat sonra)subdomainlerde bulunmazsa.Discord webhookuna -> {domain} için Yeni subdomain bulundu {{Subdomain}} bildirisi gönderilir.

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
