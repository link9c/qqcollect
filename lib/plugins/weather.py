import json
import ssl

import aiohttp
from nonebot import on_command, CommandSession, permission


context = ssl._create_unverified_context()
# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」
@on_command('w', aliases=('天气', '天气预报', '查天气'), only_to_me=False, permission=permission.EVERYBODY)
async def weather(session: CommandSession):
    if session.ctx.get('preprocessed'):
        print('ok')
        # 从会话状态（session.state）中获取城市名称（city），如果当前不存在，则询问用户
        city = session.get('city', prompt='你想查询哪个城市的天气呢？')
        # 获取城市的天气预报
        weather_report = await get_weather_of_city(city)
        # 向用户发送天气预报
        await session.send(weather_report)


# weather.args_parser 装饰器将函数声明为 weather 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@weather.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['city'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('要查询的城市名称不能为空呢，请重新输入')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg


async def get_weather_of_city(city: str):
    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回真实数据的天气 API，并拼接成天气预报内容
    location = city.replace(' ', '')
    print(location)

    url = """https://free-api.heweather.net/s6/weather/now?location=%s&key=0b8e3b249f8d4a66818b92d3e16b0a9b""" % location


    try:
        # 使用 aiohttp 库发送最终的请求
        async with aiohttp.ClientSession() as sess:
            async with sess.get(url,ssl_context=context) as response:
                if response.status != 200:
                    # 如果 HTTP 响应状态码不是 200，说明调用失败
                    return '可能出现了一些问题。。。'

                resp = json.loads(await response.text())
                status = resp.get("HeWeather6")[0].get('status')

                if status == 'ok':
                    wh = resp.get("HeWeather6")[0].get('now')
                    cond = wh['cond_txt']
                    tgwd = wh['fl']
                    xdsd = wh['hum']
                    tmp = wh['tmp']
                    jsl = wh['pcpn']
                    wind_dir = wh['wind_dir']
                    wind_sc = wh['wind_sc']
                    wt = "天气 %s，体感温度 %s ℃，温度 %s ℃，相对湿度 %s%%，%s%s级，降水量 %s" % (
                    cond, tgwd, tmp, xdsd, wind_dir, wind_sc, jsl)
                    return wt
                else:
                    return '你输入的地址我不知道呢。。。'
    except (aiohttp.ClientError, json.JSONDecodeError, KeyError) as e:
        print(e)
        # 抛出上面任何异常，说明调用失败
        return None



