import asyncio
import json
from lxml import etree
import aiohttp



async def get_rank(ruler: str):
    bangumi = False
    if ruler in ['', 'all', '全站']:
        url = 'https://www.bilibili.com/ranking/all/0/0/3'
    if ruler in ['origin', '原创']:
        url = 'https://www.bilibili.com/ranking/origin/0/0/3'
    if ruler in ['bangumi', '新番', '番剧']:
        bangumi = True
        url = 'https://www.bilibili.com/ranking/bangumi/13/0/3'
    try:
        # 使用 aiohttp 库发送最终的请求
        async with aiohttp.ClientSession() as sess:
            async with sess.get(url,verify_ssl=False) as response:
                if response.status != 200:
                    # 如果 HTTP 响应状态码不是 200，说明调用失败
                    return '可能出现了一些问题。。。'

                resp = await response.text()
                html = etree.HTML(resp)

                try:
                    databox = html.xpath('//div[@class="detail"]/span[@class="data-box"]/text()')
                    info = html.xpath('//div[@class="info"]/a/text()')
                    pts = html.xpath('//div[@class="pts"]/div/text()')
                    href = html.xpath('//div[@class="info"]/a/@href')

                    if bangumi:
                        n = 3
                        st = "No%s %s\n播放%s\n评论%s\n喜欢%s\n综合评分:%s\n地址:%s\n"
                        args = '(r[0],r[1][0],r[1][1],r[1][2],r[2],r[3])'
                    else:
                        n = 2
                        st = "No%s %s\n播放%s\n评论%s\n综合评分:%s\n地址:%s\n"
                        args = '(r[0],r[1][0],r[1][1],r[2],r[3])'

                    quant = [databox[i:i + n] for i in range(0, len(databox), n)]
                    rank = zip(info, quant, pts, href)

                    _list = ''
                    for i, r in enumerate(rank):
                        if i < 5:
                            _list += st % (i + 1, *eval(args))
                            i += 1
                        else:
                            break
                    return _list
                except Exception as e:
                    print(e)
                    return '可能输入的点不对'

    except (aiohttp.ClientError, json.JSONDecodeError, KeyError) as e:
        print(e)

tasks = [get_rank('bangumi')]

event_loop = asyncio.get_event_loop()
results = event_loop.run_until_complete(asyncio.gather(*tasks))
event_loop.close()
