import pymysql
import aiomysql
from secret import *


async def connect_mysql():
    return await aiomysql.connect(
        # host=HOST,
        host="127.0.0.1",
        port=3306,
        user=USER,
        password=MYSQLPASS,
        db="coolq"
    )
