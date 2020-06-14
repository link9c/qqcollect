import random
import re

from nonebot import on_command, permission, CommandSession


@on_command('roll', aliases=('r', 'rol'), only_to_me=False, permission=permission.EVERYBODY)
async def roll(session: CommandSession):
    if session.ctx.get('preprocessed'):
        text = session.current_arg_text.strip()
        # 3D100+8/9
        # (1d100+10-5-4-3) * 2
        roll_map = []
        offset_map = []
        regx = re.findall('(\d+)d(\d+)', text)
        if regx != [] and len(regx) == 1:
            turns = int(regx[0][0])
            random_range = int(regx[0][1])
            ruler = "%sd%s" % (turns, random_range)
            sign = re.findall('[+\-*/]', text) != []
            if len(regx[0]) == 2 and sign:
                for i in range(turns):
                    rolled = random.randint(1, random_range)
                    try:
                        offset = eval(text.replace(ruler, str(rolled)))
                    except:
                        return
                    result = int(round(offset, 0)) if offset > 0 else 0
                    roll_map.append(rolled)
                    offset_map.append(result)
                back_text = "%s %s 偏移后%s 总计%s" % (
                    text.strip(), str(roll_map), str(offset_map), sum(offset_map))
            else:

                for i in range(turns):
                    rolled = random.randint(1, random_range)
                    roll_map.append(rolled)

                back_text = "%s %s 总计%s" % (text.strip(), str(roll_map), sum(roll_map))
            await session.send(back_text, at_sender=True)
