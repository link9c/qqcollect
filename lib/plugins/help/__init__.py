from nonebot import on_command, CommandSession, permission


@on_command('help', aliases=('h', '帮助'), only_to_me=False, permission=permission.EVERYBODY)
async def help(session: CommandSession):
    if session.ctx.get('preprocessed'):
        text = """/w /天气 --- 查询实时天气\n/f /翻译 --- 翻译\n/g /群  ---  群信息\n/rank  --- bilibili排行榜"""
        await session.send(text)
