from nonebot import on_command, permission, CommandSession

from .core import translated_get


@on_command('翻译', aliases=('trans', 'f'), only_to_me=False, permission=permission.EVERYBODY)
async def _translate(session: CommandSession):
    if session.ctx.get('preprocessed'):
        text = session.current_arg_text.strip()
        if "-help" in text:
            back_text = "api:有道\n支持中英日韩法德俄西班牙葡萄牙意大利越南阿拉伯"
            await session.send(back_text.strip())
            return
        if text:
            _text = text.split(' ')
            if len(_text) > 1:
                from_to = _text[0]
                word = ' '.join(_text[1:])

                print(word, from_to)
                back_text = await translated_get(word, from_to)

            else:
                back_text = await translated_get(text)

            await session.send(back_text.strip())
