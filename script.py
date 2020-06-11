from database import conn

cursor = conn.cursor()
sql = """
CREATE TABLE IF NOT EXISTS `qqmessage`(
   `id` INT UNSIGNED AUTO_INCREMENT,
   `user_id` VARCHAR(50),
   `group_id` VARCHAR(50),
   `sender` VARCHAR(500),
   `type` VARCHAR(50),
   `cq` VARCHAR(200),
   `content` VARCHAR(3000),
   `time` VARCHAR(25),
   PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""
sql2 = """
select * from `qqmessage`"""
sql3 ="""
truncate table qqmessage
"""
sql4 ="""
drop table qqmessage
"""
cursor.execute(sql2)
conn.commit()
res = cursor.fetchall()
print(res)
# conn.commit()
