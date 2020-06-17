from nonebot import on_request, RequestSession


# 将函数注册为群请求处理器
@on_request
async def _(session: RequestSession):
    # 判断验证信息是否符合要求
    print(session.event)