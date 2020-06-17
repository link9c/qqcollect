from nonebot import message_preprocessor, NoneBot
from nonebot.typing import Context_T


@message_preprocessor
async def _(bot: NoneBot, ctx: Context_T):
    if ctx.get('group_id') not in ["876153248", "829302143"] or ctx.get('group_id') is None:
        ctx['preprocessed'] = True
        print('group_id:', ctx.get('group_id'))
        print('middleware--ok')
