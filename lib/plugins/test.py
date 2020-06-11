import ssl

import requests

from database import remote_conn as conn
import datetime

context = ssl._create_unverified_context()

def  test():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    }
    url = "https://m.hobui.com"

    res = requests.request('get',headers=header,url=url,verify=False,proxies={'http':'123.171.5.82:8118'})


    print(res.status_code)

                # 如果 HTTP 响应状态码不是 200，说明调用失败

if __name__ == '__main__':
    test()

