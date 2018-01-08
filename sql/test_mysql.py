# coding: utf-8
import MySQLdb
import random

# CREATE TABLE `stu` (
#   `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
#   `name` varchar(255) DEFAULT NULL,
#   `create_at` datetime DEFAULT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
# #
# CREATE TABLE `sco` (
#   `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
#   `name` varchar(255) DEFAULT NULL,
#   `stu_id` bigint(20) DEFAULT NULL,
#   `create_at` datetime DEFAULT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

db = MySQLdb.connect("localhost","root","ld3RjS1yYp_O","test" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 插入语句
sql_stu = """INSERT INTO stu(name, age) VALUES ('%s', '%s')"""
sql_sco = """INSERT INTO sco(name, stu_id, score) VALUES ('%s', '%s', '%s')"""
try:
   # 执行sql语句
   for i in range(100000):
       _sql = sql_stu % ('name' + str(i), random.randint(1, 100))
       print _sql
       cursor.execute(_sql)

   for i in range(1000000):
       _sql = sql_sco % ('sco' + str(i), str(random.randint(1, 200)), str(random.randint(1, 200)))
       print _sql
       cursor.execute(_sql)
   # 提交到数据库执行
   db.commit()
except Exception as ex:
   # Rollback in case there is any error
   db.rollback()

# 关闭数据库连接
db.close()
