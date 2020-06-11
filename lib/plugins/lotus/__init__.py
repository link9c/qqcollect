import nonebot
from nonebot import on_command, CommandSession

from .core import get_lotus

bot = nonebot.get_bot()


@on_command('lotus', aliases=('口吐芬芳'), only_to_me=False)
async def lotus(session: CommandSession):
    text = session.current_arg_text
    if len(text.split()) == 2:
        if '@' in text:
            num, at = text.split()
            num = int(num) if num.isnumeric() else 1
            group = None
        else:
            num, group = text.split()
            num = int(num) if num.isnumeric() else 1
            group = int(group) if group.isnumeric() else None
            at = ''
            print(num,group,'1')

    elif len(text.split()) == 3:
        num, group, at = text.split()
        num = int(num) if num.isnumeric() else 1
        group = int(group) if group.isnumeric() else 1
        at = at if '@' in at else ''
        print(num, group,'2')
    else:
        num = int(text) if text.isnumeric() else 1
        group = None
        at = ''
        print(num, group,'3')

    if num >= 255:
        num = 255

    if num and group is None:

        i = 0
        while i < num:
            msg = await get_lotus()
            await session.send(at + ' ' + msg)
            i += 1
    if num and group:
        print('group')
        i = 0
        while i < num:
            msg = await get_lotus()
            await bot.send_group_msg(group_id=group, message=at + ' ' + msg)
            i += 1
