from nonebot import MessageSegment
from nonebot import on_command, CommandSession


@on_command('echo', only_to_me=False)
async def echo(session: CommandSession):
    emoji_id = session.current_arg_text
    text = session.current_arg
    await session.send(text)

    # if emoji_id.isnumeric():
    #
    #
    #     msg = MessageSegment.emoji(int(emoji_id))
    #     msg2 = MessageSegment.face(int(emoji_id))
    #
    #     await session.send(msg2)
    #     await session.send(msg)
    # else:
    #     await session.send('请输入数字')
