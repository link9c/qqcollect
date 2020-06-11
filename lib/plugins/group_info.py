import nonebot
from nonebot import on_command, CommandSession, CQHttpError
bot = nonebot.get_bot()
import time


@on_command('群',aliases=('g'))
async def groupInfo(session: CommandSession):
    if session.ctx.get('preprocessed'):
        print('ok')
        try:
            info = await bot.get_group_member_list(group_id=187861757)

            text = ''
            auth = {'owner': '群主', 'member': '成员', 'admin': '管理员'}

            convert = lambda t: time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(t)))

            for msg in info:
                nickname = msg.get('nickname')
                card = msg.get('card')
                role = auth[msg.get('role')]
                join_time = convert(msg.get('join_time')) if msg.get('join_time') else '未知'
                last_send_time = convert(msg.get('last_sent_time')) if msg.get('last_sent_time') else '无记录'

                text += f"{card}-{nickname}-{role}\n加入时间：{join_time}\n上次发言时间：{last_send_time} \n\n"
            print(text)
            await session.send(text)
        except CQHttpError:
            pass

# [{'age': 0, 'area': '', 'card': '怜狼@竹林的公主@提不起劲@今日绝赞衰退中', 'card_changeable': False, 'group_id': 187861757, 'join_time': 0, 'last_sent_time': 1582453267, 'level': '', 'nickname': '黑羽夜鸣', 'role': 'owner', 'sex': 'unknown', 'title': '威严', 'title_expire_time': -1, 'unfriendly': False, 'user_id': 273992999}, {'age': 0, 'area': '', 'card': '【吃】纳兹琳', 'card_changeable': False, 'group_id': 187861757, 'join_time': 1438328625, 'last_sent_time': 1578128420, 'level': '', 'nickname': '老鼠', 'role': 'member', 'sex': 'male', 'title': '寻宝与被食物', 'title_expire_time': -1, 'unfriendly': False, 'user_id': 463166103}, {'age': 27, 'area': '', 'card': '【网瘾老年】', 'card_changeable': False, 'group_id': 187861757, 'join_time': 1395844406, 'last_sent_time': 1582555089, 'level': '', 'nickname': '戲言', 'role': 'member', 'sex': 'male', 'title': '白浊的胖次', 'title_expire_time': -1, 'unfriendly': False, 'user_id': 605629353}, {'age': 0, 'area': '', 'card': '【论外】云雀', 'card_changeable': False, 'group_id': 187861757, 'join_time': 0, 'last_sent_time': 1582367842, 'level': '', 'nickname': '三二一', 'role': 'member', 'sex': 'unknown', 'title': '这是小封', 'title_expire_time': -1, 'unfriendly': False, 'user_id': 851129824}, {'age': 0, 'area': '', 'card': '【自由神】蓝狐(｀・ヘ・´)', 'card_changeable': False, 'group_id': 187861757, 'join_time': 1441986572, 'last_sent_time': 1582554938, 'level': '', 'nickname': 'Nielm', 'role': 'admin', 'sex': 'male', 'title': '这是大佬', 'title_expire_time': -1, 'unfriendly': False, 'user_id': 864458494}, {'age': 28, 'area': '', 'card': '【影】黑焰的白光影狼', 'card_changeable': False, 'group_id': 187861757, 'join_time': 1473085079, 'last_sent_time': 1580741568, 'level': '', 'nickname': '黑焰的白光影狼', 'role': 'member', 'sex': 'female', 'title': '影子', 'title_expire_time': -1, 'unfriendly': False, 'user_id': 979363863}, {'age': 70, 'area': '', 'card': '【萌受】哈士奇', 'card_changeable': False, 'group_id': 187861757, 'join_time': 1458719574, 'last_sent_time': 1582555090, 'level': '', 'nickname': '戲說', 'role': 'member', 'sex': 'male', 'title': '精分的白浊', 'title_expire_time': -1, 'unfriendly': False, 'user_id': 1047841168}, {'age': 117, 'area': '', 'card': '【纸式】猫又', 'card_changeable': False, 'group_id': 187861757, 'join_time': 1441956955, 'last_sent_time': 1577285540, 'level': '', 'nickname': '            橙', 'role': 'member', 'sex': 'female', 'title': '精分的二货猫', 'title_expire_time': -1, 'unfriendly': False, 'user_id': 1282789448}]
