from urllib import request
import json

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print(f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s %s' % (k, v))
    # print('Data: ', data.decode('utf8'))

# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print(f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s %s' % (k, v))
#     print(f.read().decode('utf8'))

def fetch_data(url):
    response = request.urlopen(url)
    resopnse_str = json.loads(response.read().decode('utf-8'))
    return resopnse_str

# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
# assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')

# print(data['query']['results']['channel']['location']['city'])