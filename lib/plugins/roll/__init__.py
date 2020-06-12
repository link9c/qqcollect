import random
import re

from nonebot import on_command, permission, CommandSession


@on_command('roll', aliases=('r', 'rol'), only_to_me=False, permission=permission.EVERYBODY)
async def roll(session: CommandSession):
    if session.ctx.get('preprocessed'):
        text = session.current_arg_text.strip()
        print(text)
        if text:
            _text = text.split('d')
            roll_map = []
            offset_map = []
            if len(_text) == 2 and _text[0].isdigit():
                text_offset = _text[1]
                regx = re.findall(r'(\d+)([+\-*/])(\d+)', text_offset)
                if regx and len(regx[0]) == 3 and regx[0][0].isdigit() and regx[0][2].isdigit():

                    a = int(_text[0])
                    b = int(regx[0][0])
                    sign = regx[0][1]
                    offset = int(regx[0][2])

                    for i in range(a):
                        rolled = random.randint(1, b)
                        offset_rolled = eval("%s%s%s" % (rolled, sign, offset))
                        result = int(round(offset_rolled, 0)) if offset_rolled > 0 else 0
                        roll_map.append(rolled)
                        offset_map.append(result)
                    back_text = "%s %s 偏移后%s 总计%s" % (
                        text.strip(), str(roll_map), str(offset_map), sum(offset_map))
                else:
                    a = int(_text[0])
                    b = int(text_offset)
                    for i in range(a):
                        rolled = random.randint(1, b)
                        roll_map.append(rolled)

                    back_text = "%s %s 总计%s" % (text.strip(), str(roll_map), sum(roll_map))
                await session.send(back_text, at_sender=True)
