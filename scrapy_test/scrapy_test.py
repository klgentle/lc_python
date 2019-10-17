import requests

# login_data = {"_id2:logon:USERNAME": "administrator", "_id2:logon:PASSWORD": "Yxjk123"}
# r = requests.post("http://100.11.94.171:8080/BOE/CMC", data=login_data)
# print(r.status_code)
# print(r.text)
# print(r.url)
# print(r.cookies)

promotion_jobs_url = "http://100.11.94.171:8080/BOE/CMC/1901061353/admin/App/home.faces?service=%2Fadmin%2FApp%2FappService.jsp&appKind=CMC&bttoken=MDAwRD1EPEowR11AV0hpa05bPV9Va281ZDBlaWkBSNjAEQ"
r = requests.get(promotion_jobs_url)
print(r.status_code)
print(r.text)
print(r.url)
print(r.cookies)
