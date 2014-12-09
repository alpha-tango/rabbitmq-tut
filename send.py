#!/usr/bin/env python
import pika
import logging
logging.basicConfig()

# Rabbit set up

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')

# Send message

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print " [x] Sent 'Hello World!'"

# close connection

connection.close()
