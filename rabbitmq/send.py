#!/usr/bin/env python
import pika
from sys import argv


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=argv[1])
print " [x] Sent " + argv[1]
connection.close()
