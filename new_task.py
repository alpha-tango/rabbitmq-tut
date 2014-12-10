#!/usr/bin/env python
import pika
import logging
import sys
logging.basicConfig()

# Rabbit set up

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

# Send preset message or arbitrary text from command line

message = ' '.join(sys.argv[1:]) or "Hello world!"
channel.basic_publish(exchange='',
		      routing_key='task_queue',
		      body=message,
			  properties=pika.BasicProperties(
				delivery_mode = 2, # make messages as persistent
			))
print " [x] sent %r" % (message,)

# close connection

connection.close()
