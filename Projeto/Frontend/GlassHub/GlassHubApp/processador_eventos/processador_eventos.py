# import pika
# import os
# import json
# import websocket
# import asyncio

# url = os.environ.get('CLOUDAMQP_URL', '')
# params = pika.URLParameters(url)
# connection = pika.BlockingConnection(params)
# channel = connection.channel()
# channel.queue_declare(queue='eventos_queue', durable=True)

# def send_event_to_websocket(data):
    

# def callback(ch, method, properties, body):
#     data = json.loads(body.decode('utf-8'))
#     print(data)
#     send_event_to_websocket(data)

# channel.basic_consume('eventos_queue', callback, auto_ack=True)
# channel.start_consuming()