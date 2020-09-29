#!/usr/bin/python3
# -*- coding: utf-8 -*- 
import subprocess
import os
import json
from kafka import KafkaProducer
import datetime
import time

alert_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
producer = KafkaProducer(bootstrap_servers=['10.14.56.23:9092','10.14.56.24:9092','10.14.56.25:9092'])

ZK1 = 'xx.xx.xx.xx'
ZK2 = 'xx.xx.xx.xx'
ZK3 = 'xx.xx.xx.xx'

zk1_results=subprocess.getoutput("echo stat | nc xx.xx.xx.xx  2181 | grep Mode | awk '{print $2}'") 
zk2_results=subprocess.getoutput("echo stat | nc xx.xx.xx.xx  2181 | grep Mode | awk '{print $2}'") 
zk3_results=subprocess.getoutput("echo stat | nc xx.xx.xx.xx  2181 | grep Mode | awk '{print $2}'") 

zk_status = ['follower','leader']

#for state in zk_status:
if zk1_results not in zk_status:
    msg_dict = {
        "alertName" : "zookeeperStatus",
        "alertState" : "ALERT",
        "curValue" : zk1_results,
        "dimensions" : ZK1,
        "expression" : "zookeeper has stoped.",
        "instanceName" : "NULL",
        "metricName" : "zookeeper Available",
        "metricProject" : "GZ-zookeeper",
        "namespace" : "NULL",
        "preTriggerLevel" : "NULL",
        "ruleId" : "NULL",
        "signature" : "NULL",
        "timestamp" : alert_time,
        "triggerLevel" : "WARN",
        "userId" : "NULL"
    }
    msg = json.dumps(msg_dict).encode()
    producer.send('alert_monitor_aliyun_resource_info',msg)
    producer.close()

if zk2_results not in zk_status:
    msg_dict = {
        "alertName" : "zookeeperStatus",
        "alertState" : "ALERT",
        "curValue" : zk2_results,
        "dimensions" : ZK2,
        "expression" : "zookeeper has stoped.",
        "instanceName" : "NULL",
        "metricName" : "zookeeper Available",
        "metricProject" : "GZ-zookeeper",
        "namespace" : "NULL",
        "preTriggerLevel" : "NULL",
        "ruleId" : "NULL",
        "signature" : "NULL",
        "timestamp" : alert_time,
        "triggerLevel" : "WARN",
        "userId" : "NULL"
    }
    msg = json.dumps(msg_dict).encode()
    producer.send('alert_monitor_aliyun_resource_info',msg)
    producer.close()

if zk3_results not in zk_status:
    msg_dict = {
        "alertName" : "zookeeperStatus",
        "alertState" : "ALERT",
        "curValue" : zk3_results,
        "dimensions" : ZK3,
        "expression" : "zookeeper has stoped.",
        "instanceName" : "NULL",
        "metricName" : "zookeeper Available",
        "metricProject" : "GZ-zookeeper",
        "namespace" : "NULL",
        "preTriggerLevel" : "NULL",
        "ruleId" : "NULL",
        "signature" : "NULL",
        "timestamp" : alert_time,
        "triggerLevel" : "WARN",
        "userId" : "NULL"
    }
    msg = json.dumps(msg_dict).encode()
    producer.send('alert_monitor_aliyun_resource_info',msg)
    producer.close()

-- 另外写法
#!/usr/bin/python3
# -*- coding: utf-8 -*- 
import subprocess
import os
import json
from kafka import KafkaProducer
import datetime
import time

alert_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
producer = KafkaProducer(bootstrap_servers=['10.14.56.23:9092','10.14.56.24:9092','10.14.56.25:9092'])

ZK1 = 'xx.xx.xx.xx'
ZK2 = 'xx.xx.xx.xx'
ZK3 = 'xx.xx.xx.xx'
ZK4 = 'xx.xx.xx.xx'
ZK5 = 'xx.xx.xx.xx'

zk1_results=subprocess.getoutput("echo stat | nc xx.xx.xx.xx  2181 | grep Mode | awk '{print $2}'") 
zk2_results=subprocess.getoutput("echo stat | nc xx.xx.xx.xx  2181 | grep Mode | awk '{print $2}'") 
zk3_results=subprocess.getoutput("echo stat | nc xx.xx.xx.xx  2181 | grep Mode | awk '{print $2}'") 
zk4_results=subprocess.getoutput("echo stat | nc xx.xx.xx.xx  2181 | grep Mode | awk '{print $2}'")
zk5_results=subprocess.getoutput("echo stat | nc xx.xx.xx.xx  2181 | grep Mode | awk '{print $2}'")


zk_status = ['follower','leader']
servers = [ZK1,ZK2,ZK3,ZK4,ZK5]
results = [zk1_results,zk2_results,zk3_results,zk4_results,zk5_results]

for result in results:
    for server in servers:
        if result not in zk_status:
            msg_dict = {
                "alertName" : "zookeeperStatus",
                "alertState" : "ALERT",
                "curValue" : result,
                "dimensions" : server,
                "expression" : "zookeeper has stoped.",
                "instanceName" : "NULL",
                "metricName" : "zookeeper Available",
                "metricProject" : "COMM-zookeeper",
                "namespace" : "NULL",
                "preTriggerLevel" : "NULL",
                "ruleId" : "NULL",
                "signature" : "NULL",
                "timestamp" : alert_time,
                "triggerLevel" : "WARN",
                "userId" : "NULL"
            }
            msg = json.dumps(msg_dict).encode()
            producer.send('alert_monitor_aliyun_resource_info',msg)
            print(msg)
producer.close()


