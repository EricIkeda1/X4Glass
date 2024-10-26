import pika
import threading

class PikaConsumer:
    def __init__(self, queue_name):
        self.queue_name = queue_name
        self.connection = None
        self.channel = None
        self.thread = None

    def start(self):
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def run(self):
        import asyncio 
        loop = asyncio.new_event_loop()

        params = pika.URLParameters('')
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name, durable=True)
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=lambda ch, method, properties, body: loop.run_until_complete(self._callback(ch, method, properties, body)), auto_ack=True)

        print(f"[*] Aguardando mensagens na fila '{self.queue_name}'. Para sair pressione CTRL+C")
        self.channel.start_consuming()

    async def _callback(self, ch, method, properties, body):
        import websockets

        try:
            uri = "ws://localhost:8000/ws/eventos/"
            server = await websockets.connect(uri)
            await server.send(body.decode('utf-8'))
        except Exception as e:
            print(e)

    def stop(self):
        if self.connection:
            self.connection.close()
        if self.thread:
            self.thread.join()
