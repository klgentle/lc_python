import requests        #导入requests包
import json
def get_report_date(word=None):
    url = 'http://10.95.64.198:9086/SmartReport/RegularReport'
    From_data={
        'ajax': 1,
        's_id': None,
        'type': 'GRKHXX.xls',
        'freq': 'ymd',
        'branchCap': '000000 - 创兴银行有限公司(管理行汇总)',
        'branch': '000000',
        'day': '20210331',
        'dayCap': '2021年3月31日',
        'rmlpar': 'ymd|000000 - 创兴银行有限公司(管理行汇总)|20210331',
        'paraDef': 'str|str|str',
        'reportid': 'GRKHXX',
        'S_ID': 'GRKHXX',
        'op': 'view',
        'page': '0',
        'section': '0'
        }
    #请求表单数据
    response = requests.post(url,data=From_data)
    #将Json格式字符串转字典
    content = json.loads(response.text)
    print(content)
    #打印翻译后的数据
    #print(content['translateResult'][0][0]['tgt'])
if __name__=='__main__':
    get_report_date('')
