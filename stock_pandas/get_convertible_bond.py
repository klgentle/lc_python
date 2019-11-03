#convertible_bond

import pandas as pd
import requests

def get_convertible_bond():
    
    resp = requests.get(
        "http://data.10jqka.com.cn/ipo/bond/"
    )

    print(resp.text)
    #data = resp.json()
    #print(data)


if __name__ == "__main__":
    get_convertible_bond()
