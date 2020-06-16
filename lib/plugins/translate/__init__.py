import time

from nonebot import on_command, permission, CommandSession

from lib.plugins.translate.api_youdao import translated_get
from .apiBaidu import BaiduCrack
from .apiBaidu.lang import langMap

baidu = BaiduCrack()


@on_command('翻译', aliases=('trans', 'f'), only_to_me=False, permission=permission.EVERYBODY)
async def _translate(session: CommandSession):
    if session.ctx.get('preprocessed'):
        text = session.current_arg_text.strip()
        if "-help" in text:
            back_text = "api:百度\n 使用方法：中>日 你好\n注：简写有可能歧义，可以写多个字符或全称"
            await session.send(back_text.strip())
            return
        if "-support" in text:
            support = ",".join(langMap.keys())
            back_text = "支持:%s" % support
            await session.send(back_text.strip())
            return

        _text = text.split(' ')
        if len(_text) > 1:
            from_to = _text[0]
            word = ' '.join(_text[1:])
            split_text = from_to.split(">")
            if len(split_text) == 2:
                f, t = split_text
                # await baidu.get_true_token_cookie()
                # time.sleep(0.5)
                t_simple, f_simple = None, None
                for key in langMap.keys():
                    if t in key[0:len(t) if len(key) > len(t) else len(key)]:
                        t_simple = langMap.get(key)
                    if f in key[0:len(f) if len(key) > len(f) else len(key)]:
                        f_simple = langMap.get(key)
                if t in '中文(简体)':
                    t_simple = 'zh'
                if f in '中文(简体)':
                    f_simple = 'zh'
                if t_simple:
                    back_text = baidu.do_translate(word, f_simple, t_simple)
                    if back_text:
                        await session.send("%s->%s : " % (f_simple, t_simple) + back_text.strip())


                else:
                    await session.send("请检查你的输入，或查询-support")
