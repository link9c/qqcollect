import nonebot
from nonebot import on_command, CommandSession, CQHttpError
bot = nonebot.get_bot()

@on_command('say',only_to_me=False)
async def disseminate(session:CommandSession):
    if session.ctx.get('user_id') == 605629353:
        text = session.current_arg
        if text.strip():
        #187861757
            await bot.send_group_msg(group_id=876153248,message=text)

    else:
        await session.send('你没有权限')