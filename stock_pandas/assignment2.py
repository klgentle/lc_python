import requests
url = "https://sites.google.com/site/chnyyang/price_data.csv"
f = requests.get(url) 
with open("price_data.csv", "wb") as code:
   code.write(f.content)
