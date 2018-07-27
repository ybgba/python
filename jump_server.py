CREATE TABLE mysql_server (
  id int(11) NOT NULL PRIMARY key AUTO_INCREMENT COMMENT '主键', 
  tag varchar(50) DEFAULT '' COMMENT '标识',
  ip varchar(15) DEFAULT '' COMMENT 'IP地址',
  port int(11) DEFAULT 3306 COMMENT '数据库端口',
  basedir varchar(50) DEFAULT '' COMMENT '程序存放位置',
  datadir varchar(50) DEFAULT '' COMMENT '数据存放位置',
  soketdir varchar(50) DEFAULT '' COMMENT 'socket存放位置',
  binlog varchar(50) DEFAULT '' COMMENT 'binlog位置',
  relaylog varchar(50) DEFAULT '' COMMENT 'relay位置',
  errorlog varchar(50) DEFAULT '' COMMENT 'error日志位置',
  mysql_user varchar(20) DEFAULT '' COMMENT '登录用户名',
  mysql_pass varchar(50) DEFAULT '' COMMENT '登录密码',
  status tinyint DEFAULT 1 COMMENT '1为正常使用，0为已经停止使用',
  info varchar(500) DEFAULT '' COMMENT '服务器信息'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


insert into mysql_server (tag,ip,port,basedir,datadir,soketdir,binlog,relaylog,errorlog,mysql_user,mysql_pass,status,info) 
values 
('anedbkdgis02','172.17.18.18',3306,'/mnt/mysql5636/','/data/ane56/','/data/ane56/mysqld.sock','/data/mysqlbinlog/','/data/mysqlbinlog/mysql-relay-bin','/var/log/mysqld.log','dba','qwe123',1,'快递gis从库'),
('pmysqlkdgis04','172.17.18.13',3306,'/mnt/mysql5636/','/data/ane56/','/data/ane56/mysqld.sock','/data/mysqlbinlog/','/data/mysqlbinlog/mysql-relay-bin','/var/log/mysqld.log','dba','qwe123',1,'快递gis从库'),
('pmysqlkdgis04','172.17.18.13',3307,'/mnt/mysql5636_3307/','/data/ane56_3307/','/data/ane56_3307/mysqld.sock','/data/mysqlbinlog_3307/','/data/mysqlbinlog_3307/mysql-relay-bin','/var/log/mysqld.log','dba','qwe123',1,'快递gis从库'),
('pmysqlkdgis04','172.17.18.13',3308,'/mnt/mysql5636_3308/','/data/ane56_3308/','/data/ane56_3308/mysqld.sock','/data/mysqlbinlog_3308/','/data/mysqlbinlog_3308/mysql-relay-bin','/var/log/mysqld.log','dba','qwe123',1,'快递gis从库'),
('pmysqlkdgis04','172.17.18.13',3309,'/mnt/mysql5636_3309/','/data/ane56_3309/','/data/ane56_3309/mysqld.sock','/data/mysqlbinlog_3309/','/data/mysqlbinlog_3309/mysql-relay-bin','/var/log/mysqld.log','dba','qwe123',1,'快递gis从库')
;




#!/usr/bin/python3
# -*- coding: utf-8 -*- 
import pymysql
import os

MYSQL = '/mnt/mysql5721/bin/mysql'
HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'qwe123'
PORT = 11856
DB = 'jumpmysql'
CHARSET = 'utf8'

conn = pymysql.connect(host=HOST,port=PORT,user=USER,passwd=PASSWORD,db=DB,charset=CHARSET)

while True:
    cur = conn.cursor()
    cur.execute("select * from mysql_server;")
    servers = cur.fetchall()
    idlist = []
    for server in servers:
        id = server[0]
        ip = server[2]
        port = server[3]
        tag = server[13]
        print(id,ip,port,tag)
        idlist.append(id)

    try:
        serverid = int(input("Please choose the instance ID: "))
        if serverid not in idlist:
            print("\033[1;31;40mPlease enter the correct ID of instance and try again.\033[0m")
            continue
        else:
            SQL = "select ip,mysql_user,mysql_pass,port from mysql_server where id = {SERVER_ID}".format(SERVER_ID=serverid)
            cur.execute(SQL)
            data = cur.fetchone()
            host = data[0]
            user = data[1]
            password = data[2]
            port = data[3]
            conninfo = MYSQL + " -h%s -u%s -p%s -P%s" %(host,user,password,port)
    except:
        break

    try:
        MSG = "\033[1;31;40mYou will connect to HOST:\033[0m" + "\033[1;37;41m%s\033[0m" %(host) + "\033[1;31;40m, PORT:\033[0m" + "\033[1;37;41m%s\033[0m" %(port) + "\033[1;31;40m, this server is:\033[0m" + "\033[1;37;41m%s\033[0m" %(tag) + "\033[1;31;40m, please make sure and confirm it!\033[0m"
        print(MSG)
        CHOOSE = format(input("Please enter 'Y' or 'N' : ")).lower()
        if CHOOSE == 'y':
            os.system(conninfo)
        elif CHOOSE == 'n':
            break
        else:
            print("Input error and please re-enter 'y' or 'n'.")
            continue
    except:
        print("The database cannot be connected, please check up the info of connection and try again.")
    
    cur.close()
    conn.close()
    break
