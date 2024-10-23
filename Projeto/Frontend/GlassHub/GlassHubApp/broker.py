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
        params = pika.URLParameters('')
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name, durable=True)
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)

        print(f"[*] Aguardando mensagens na fila '{self.queue_name}'. Para sair pressione CTRL+C")
        self.channel.start_consuming()

    def callback(self, ch, method, properties, body):
        import websocket

        uri = "ws://localhost:8000/ws/eventos/"
        socket = websocket.create_connection(uri)
        socket.send_text(body.decode('utf-8'))
        socket.close()

    def stop(self):
        if self.connection:
            self.connection.close()
        if self.thread:
            self.thread.join()
