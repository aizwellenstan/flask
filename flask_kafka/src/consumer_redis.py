
from kafka import KafkaConsumer
import json
import redis
 
# redis
pool=redis.ConnectionPool(host='localhost',port=6379,db=0)
r=redis.Redis(connection_pool=pool)
def dict2redis(d):
    r.hset(d['eventOrder'],'eventOrder',d['eventOrder'])
    r.hset(d['eventOrder'],'relateOrder',d['relateOrder'])
    r.hset(d['eventOrder'],'omsOrderItemId',d['omsOrderItemId'])
    r.hset(d['eventOrder'],'zacty',d['zacty'])
    r.hset(d['eventOrder'],'appearTime',d['appearTime'])
    r.hset(d['eventOrder'],'eventSource',d['eventSource'])    
 
#写入redis    
# f=open('consumer.txt','w')
consumer = KafkaConsumer('test17',group_id='group1',bootstrap_servers=['192.168.1.185:9092'])
 
for msg in consumer:
    
    # dict=json.loads(msg.value.decode('utf-8'))
    # print(dict)
    # dict2redis(dict)
    print(msg.value)
 
print(r.hgetall('WP2020016300386'))