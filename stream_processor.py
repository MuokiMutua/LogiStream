from confluent_kafka import Consumer
import json
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'speed-layer', 'auto.offset.reset': 'latest'})
c.subscribe(['truck_telemetry'])

while True:
    msg = c.poll(1.0)
    if msg:
        data = json.loads(msg.value().decode('utf-8'))
        # Store live temp in Redis (Speed Layer)
        r.set(f"temp:{data['truck_id']}", data['temp'])
        
        if data['temp'] > 7.0:
            print(f"🚨 ALERT: {data['truck_id']} is too hot! ({data['temp']}°C)")