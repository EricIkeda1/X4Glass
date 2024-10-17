import pika
import os
import json
import websockets
import asyncio

url = os.environ.get('CLOUDAMQP_URL', '')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='eventos_queue', durable=True)

async def send_event_to_websocket(data):
    uri = "ws://localhost:8000/ws/eventos/"  # Altere para o seu WebSocket URI
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps(data))

def callback(ch, method, properties, body):
    print("Recebendo os dados:")  # Mensagem de início do recebimento
    data = json.loads(body.decode('utf-8'))
    print("Received:", data)  # Isso mostrará os dados recebidos

    asyncio.run(send_event_to_websocket(data))  # Enviar evento para o WebSocket

channel.basic_consume('eventos_queue', callback, auto_ack=True)
channel.start_consuming()
