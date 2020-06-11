import asyncio
import json
import ssl

import aiohttp

context = ssl._create_unverified_context()


async def get_lotus():
    url = 'https://nmsl.shadiao.app/api.php?lang=zh_cn'
    try:
        # 使用 aiohttp 库发送最终的请求
        async with aiohttp.ClientSession() as sess:
            async with sess.get(url, ssl_context=context) as response:
                if response.status != 200:
                    # 如果 HTTP 响应状态码不是 200，说明调用失败
                    return '可能出现了一些问题。。。'

                resp = await response.text()
                return resp
    except (aiohttp.ClientError, json.JSONDecodeError, KeyError) as e:
        print(e)


if __name__ == '__main__':
    tasks = [get_lotus()]

    event_loop = asyncio.get_event_loop()
    results = event_loop.run_until_complete(asyncio.gather(*tasks))
    event_loop.close()
