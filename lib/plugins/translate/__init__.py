from nonebot import on_command, permission, CommandSession

from .core import translated_get


@on_command('翻译', aliases=('trans', 'f'), only_to_me=False, permission=permission.EVERYBODY)
async def _translate(session: CommandSession):
    # 从会话状态（session.state）中获取城市名称（city），如果当前不存在，则询问用户
    if session.ctx.get('preprocessed'):
        text = session.current_arg_text.strip()
        if text:
            _text = text.split(' ')
            if len(_text) > 1:
                from_to = _text[0]
                word = ' '.join(_text[1:])

                print(word, from_to)
                back_text = await translated_get(word, from_to)

            else:
                back_text = await translated_get(text)


            # print(back_text)
            # 获取城市的天气预报

            # 向用户发送天气预报
            await session.send(back_text.strip())
