from nonebot import message_preprocessor, NoneBot
from nonebot.typing import Context_T


@message_preprocessor
async def _(bot: NoneBot, ctx: Context_T):
    print('group_id:', ctx.get('group_id'))
    print('middleware--ok')
