import pika
from os import environ

class Broker:
    def __init__(self, exchange: str, routing_key: str):
        self.exchange = exchange
        self.routing_key = routing_key
        self.connection = None
        self.channel = None

    def publish(self, body: str):
        params = pika.URLParameters(environ.get("AMQP_URL"))
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()
        self.channel.basic_publish(exchange=self.exchange, routing_key=self.routing_key, body=body)
        self.connection.close()