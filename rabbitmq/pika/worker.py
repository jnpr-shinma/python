#!/usr/bin/env python
import pika
import time

credentials = pika.PlainCredentials('cspmq', 'Juniper1')

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='10.102.93.212',credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='48762a6f-e3ca-3536-880b-ac8dffc3b4d6', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='48762a6f-e3ca-3536-880b-ac8dffc3b4d6')

channel.start_consuming()