import requests
import re

# proxy = '114.98.27.155:4216'
# proxies = {
#             'http': 'http://' + proxy,
#             'https': 'https://' + proxy,
#         }
# res = requests.get("http://www.baidu.com",proxies=proxies)

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
}


def get_proxy(page=1):
    prox_url = "https://www.xicidaili.com/nn/%s" % page
    res = requests.get(prox_url, headers=headers)
    html = res.content.decode('utf-8')
    pattern = re.compile(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>.+?<td>(\d{1,6})</td>', re.DOTALL)
    _list = re.findall(pattern, html)
    print(_list)
    return _list


def test_proxy():
    proxy_able = []
    proxy_list = get_proxy()
    for each in proxy_list:
        proxy = each[0] + ":" + each[1]
        proxies = {
            'http': 'http://' + proxy,
            'https': 'https://' + proxy,
        }
        try:
            res = requests.get("http://www.baidu.com", proxies=proxies, timeout=3.5,headers=headers)
        except requests.exceptions.ProxyError as e:
            print(e,'continue')
            continue
        except requests.exceptions.ConnectTimeout :
            print("timeout continue")
            continue
        except  requests.exceptions.ReadTimeout:
            print("timeout continue")
            continue
        except Exception as e:
            print(e)
            continue

        if res.status_code == 200:
            print(proxy,'is ok')
            proxy_able.append(proxy)
    return proxy_able


if __name__ == '__main__':
    print(test_proxy())
