import requests
url = 'https://movie.douban.com/top250?start=0&filter='

# 把 user-agent 伪装成浏览器
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

# 构造请求头部的 user-agent
header = {}
header['user-agent'] = user_agent

response = requests.get(url, headers=header)
print(response)
# 返回200
print(response.text)
# 返回请求的网页内容
