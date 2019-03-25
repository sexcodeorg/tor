import urllib, sys
import urllib.request
import urllib.parse
host = 'http://ipquery.market.alicloudapi.com'
path = '/query'
method = 'GET'
appcode = 'e998d0446794416f888cb1a4d9af21c2'
querys = 'ip=58.30.0.0'
bodys = {}
url = host + path + '?' + querys

urllib.parse.urlencode()
request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    print(content)
