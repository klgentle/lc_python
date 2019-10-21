import requests


def requests_auth_login():
    s = requests.Session()
    r = s.get("http://100.11.94.171:8080/BOE/CMC", auth=("administrator", "Yxjk123"))
    print(r.status_code)
    print(r.text)
    # print(r.url)
    # print(r.cookies)
    r2 = s.get("http://100.11.94.171:8080/BOE/CMC/1901061353/admin/logon.faces")
    print(r2.status_code)
    #print("r2-------------\n", r2.text)


def requests_post_login():
    login_data = {
        "_id2:logon:USERNAME": "administrator",
        "_id2:logon:PASSWORD": "Yxjk123",
    }
    r = requests.post("http://100.11.94.171:8080/BOE/CMC", data=login_data)
    print(r.status_code)
    print(r.text)
    print(r.url)
    print(r.cookies)


def requests_create_promotion():
    promotion_jobs_url = "http://100.11.94.171:8080/BOE/CMC/1901061353/admin/App/home.faces?service=%2Fadmin%2FApp%2FappService.jsp&appKind=CMC&bttoken=MDAwRD1EPEowR11AV0hpa05bPV9Va281ZDBlaWkBSNjAEQ"
    r = requests.get(promotion_jobs_url)
    print(r.status_code)
    print(r.text)
    print(r.url)
    print(r.cookies)


if __name__ == "__main__":
    requests_auth_login()
