import asyncio
import json
import re
import time

import aiohttp
import random
import math

import ctypes
import requests


class Crack:
    @classmethod
    def int_overflow(self, val):
        maxint = 2147483647
        if not -maxint - 1 <= val <= maxint:
            val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
        return val

    @classmethod
    def unsigned_right_shitf(self, n, i):
        # 数字小于0，则转为32位无符号uint
        if n < 0:
            n = ctypes.c_uint32(n).value
        # 正常位移位数是为正数，但是为了兼容js之类的，负数就右移变成左移好了
        if i < 0:
            return -self.int_overflow(n << abs(i))
        # print(n)
        return self.int_overflow(n >> i)

    def _a(self, r):
        t = [r_ for r_ in r]
        if isinstance(r, list):

            for o in range(len(r)):
                t[o] = r[o]
            return t
        return t

    def _n(self, r, o):
        for t in range(0, len(o) - 2, 3):
            a = o[t + 2]
            a = ord(a[0]) - 87 if a >= "a" else int(a)
            a = self.unsigned_right_shitf(r, a) if o[t + 1] == "+" else r << a
            r = r + a & 4294967295 if o[t] == "+" else r ^ a

        return r

    def e(self, r, gtk):
        o = re.match('/[\uD800-\uDBFF][\uDC00-\uDFFF]/g', r)

        if o is None:
            t = len(r)
            if t > 30:
                r = "" + r[0, 10] + r[math.floor(t / 2) - 5, 10] + r[-10, 10]
        else:
            e = re.split('/[\uD800-\uDBFF][\uDC00-\uDFFF]/g', r)
            C = 0
            h = len(e)
            f = []
            while h > C:
                if e[C] != "":
                    f = map(self._a(e[C].split("")), f)
                if C != h - 1:
                    f.append(o[C])
                g = len(f)
                if g > 30:
                    r = "".join(f[0:10]) + "".join(f[math.floor(g / 2) - 5:math.floor(g / 2) + 5]) + "".join(f[-10:])
        u = gtk
        d = u.split(".")
        m = int(d[0]) or 0
        s = int(d[1]) or 0
        S = [0 for _r in range(len(r) * 3)]
        c = 0

        for v in range(len(r)):
            A = ord(r[v])
            if A < 128:
                S[c] = A
            else:
                if A < 2048:
                    S[c] = A >> 6 | 192
                else:
                    if 55296 == (64512 & A) and (v + 1) < len(r) and 56320 == (64512 & ord(r[v + 1])):
                        v += 1
                        A = 65536 + ((1023 & A) << 10 + (1023 & ord(r[v])))
                        S[c] = A >> 18 | 240
                        c += 1
                        S[c] = A >> 12 & 63 | 128
                        c += 1
                    else:

                        S[c] = (A >> 12 | 224)
                        c += 1
                        S[c] = A >> 6 & 63 | 128
                        c += 1
                        S[c] = 63 & A | 128
                        c += 1

        p = m
        F = "" + chr(43) + chr(45) + chr(97) + ("" + chr(94) + chr(43) + chr(54))
        D = "" + chr(43) + chr(45) + chr(51) + ("" + chr(94) + chr(43) + chr(98)) + ("" + chr(43) + chr(45) + chr(102))

        for b in range(len(S)):
            p += S[b]
            p = self._n(p, F)
        p = self._n(p, D)
        p ^= s
        if p < 0:
            p = (2147483647 & p) + 2147483648
        p %= 1e6
        return str(int(p)) + "." + str((int(p) ^ m))


class BaiduCrack:

    def __init__(self):
        self.try_time = 0
        self._root_url = "https://fanyi.baidu.com/"
        self._second_root_url = "https://fanyi.baidu.com/#zh/en/%E4%BD%A0%E5%A5%BD"
        self._headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        self.cookies = []
        self.sess = requests.Session()

    def get_true_token_cookie(self):

        self.sess.get(self._root_url, headers=self._headers)
        resp = self.sess.get(self._second_root_url, headers=self._headers)
        resp = resp.content.decode('utf-8')
        cookies = self.sess.cookies.values()

        regx = re.findall('token: \'(.+)\'', resp)
        token = regx[0] if regx != [] else None
        regx = re.findall('window.gtk = \'(.+)\'', resp)
        gtk = regx[0] if regx != [] else None

        self.token = token
        self.gtk = gtk
        self.cookies = "BAIDUID=" + cookies[0]

    def do_translate(self, query, f, t):

        self.get_true_token_cookie()

        url = "https://fanyi.baidu.com/v2transapi?from=%s&to=%s" % (f, t)
        sign = Crack().e(query, self.gtk)
        h = {"from": f, "to": t, "query": query, "simple_means_flag": 3, "sign": sign,
             "token": self.token,
             "domain": "common"}

        headers = {
            'cookie': self.cookies,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        }
        proxy = ['223.247.94.239:4216', '223.241.2.91:4216', '36.59.120.182:4216', '139.196.52.1:8080',
                 '223.243.5.147:4216', '222.186.55.41:8080', '116.22.48.220:4216']
        r_prx = random.choice(proxy)
        proxies = {
            'http': 'http://' + r_prx,
            'https': 'https://' + r_prx,
        }
        print(h)
        print(r_prx)
        # print(headers)
        try:
            res = self.sess.post(url, data=h, headers=headers, proxies=proxies, timeout=5)
        except Exception as e:
            print(e)
            return "代理出错"

        if res.status_code != 200:
            print(res.status_code)
            return None

        content = res.content.decode('utf-8')

        data_dict = json.loads(content)
        # print(data_dict)
        # token或cookie失效时再次获取
        if data_dict.get('errno') == 997 or data_dict.get('errno') == 998:
            print("cookie或token获取错误")
            return None

        try:
            result = data_dict["trans_result"]["data"][0]["dst"]
            print(result)
        except:
            result = None
            print("返回错误")

        return result


if __name__ == '__main__':
    # "531318.849991"
    # e("Ni")
    st = time.time()
    c = BaiduCrack()
    # c.get_true_token_cookie()
    c.do_translate("明天来吃饭吗", "zh", "en")

    print(time.time() - st)
