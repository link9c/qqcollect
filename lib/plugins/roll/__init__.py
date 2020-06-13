import random
import re

from nonebot import on_command, permission, CommandSession


@on_command('roll', aliases=('r', 'rol'), only_to_me=False, permission=permission.EVERYBODY)
async def roll(session: CommandSession):
    if session.ctx.get('preprocessed'):
        text = session.current_arg_text.strip()
        # 3D100+8/9
        print(text)
        if text:
            _text = text.split('d')
            roll_map = []
            offset_map = []
            if len(_text) == 2 and _text[0].isdigit():
                text_offset = _text[1]
                # regx = re.findall(r'(\d+)([+\-*/])(\d+)', text_offset)
                regx = re.findall(r'(\d+)([+\-*/>])', text_offset)
                print(regx)
                if regx and regx[0][0].isdigit() and len(regx[0]) == 2:

                    a = int(_text[0])
                    b = int(regx[0][0])

                    for i in range(a):
                        rolled = random.randint(1, b)
                        try:
                            offset = eval(text_offset.replace(str(b), str(rolled)))
                        except:
                            return
                        result = int(round(offset, 0)) if offset > 0 else 0
                        roll_map.append(rolled)
                        offset_map.append(result)
                    back_text = "%s %s 偏移后%s 总计%s" % (
                        text.strip(), str(roll_map), str(offset_map), sum(offset_map))
                else:
                    a = int(_text[0])
                    b = int(regx[0][0])
                    for i in range(a):
                        rolled = random.randint(1, b)
                        roll_map.append(rolled)

                    back_text = "%s %s 总计%s" % (text.strip(), str(roll_map), sum(roll_map))
                await session.send(back_text, at_sender=True)
