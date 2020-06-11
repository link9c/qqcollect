import datetime

import nonebot

from database import connect_mysql
from logger import Logger

log = Logger(__name__)
# cursor = conn.cursor()

bot = nonebot.get_bot()


@bot.on_message('group')
async def handle_group_message(ctx):

    message = ctx.get('message')
    # 发送消息的类型
    _type = message[0].get('type')
    # 原始消息
    raw_message = ctx.get('raw_message')
    if isinstance(raw_message, list):
        cq, content = raw_message
    else:
        cq = ''
        content = raw_message

    # 发送人信息
    sender = ctx.get('sender')
    # 发送人qq号
    user_id = ctx.get('user_id')
    group_id = ctx.get('group_id')
    # 时间戳
    timestamp = ctx.get('time')
    format_time = datetime.datetime.fromtimestamp(timestamp)
    con = await connect_mysql()
    # await con.ping()
    async with con.cursor() as cursor:

        sql = """
        insert into `qqmessage` (user_id,group_id,sender,`type`,cq,content,`time`,format_time) values
        ('%s','%s',"%s",'%s','%s',"%s",'%s','%s')""" % (user_id, group_id, sender, _type, cq, content, timestamp, format_time)
        log.get_log().info(sql)
    # print(sql)
        try:
            await cursor.execute(sql)
            await con.commit()
            log.get_log().info("sql success")
        except Exception as e:
            print(e)

    # print('接受到信息：%s' % ctx)


if __name__ == '__main__':
    pass
