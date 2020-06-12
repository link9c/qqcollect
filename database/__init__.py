import pymysql
import aiomysql

# conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='coolq', port=3307)
# remote_conn = pymysql.connect(
#     host="118.xxx.209",
#     port=3306,
#     user="link",
#     password="xxxx",
#     db="coolq")

async def connect_mysql():
    return await aiomysql.connect(
        # host="118.xxx.209",
        host="127.0.0.1",
        port=3306,
        user="link",
        password="xxxx",
        db="coolq"
    )
