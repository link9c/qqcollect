import nonebot
from nonebot import on_command, CommandSession
from nonebot import MessageSegment

bot = nonebot.get_bot()


@on_command('say', only_to_me=False)
async def disseminate(session: CommandSession):
    if session.ctx.get('user_id') == 605629353:
        text = session.current_arg


        if text.strip():
            print(text)
            # text.replace()
            # 187861757
            # await bot.send_group_msg(group_id=876153248,message=text)
            await bot.send_group_msg(group_id=187861757, message=text)
            # msg = MessageSegment.face(int(212))
            # print(msg)
            # await bot.send_private_msg(user_id=605629353, message=text, auto_escape=True)
            # await bot.send_group_msg(group_id=705591820, message=text)

    else:
        await session.send('你没有权限')
