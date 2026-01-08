import json
import time
import random
from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:9092'})

def produce_telemetry():
    trucks = ['TRUCK-001', 'TRUCK-002']
    while True:
        for truck in trucks:
            data = {
                "truck_id": truck,
                "temp": round(random.uniform(2.0, 10.0), 2),
                "fuel": random.randint(40, 100),
                "timestamp": time.time()
            }
            p.produce('truck_telemetry', json.dumps(data).encode('utf-8'))
        p.poll(0)
        time.sleep(2)

if __name__ == "__main__":
    produce_telemetry()