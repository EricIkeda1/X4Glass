# consumer.py
from channels.generic.websocket import AsyncWebsocketConsumer
from json import loads, dumps
from .models import eventos  
from asgiref.sync import sync_to_async

class EventConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "temperlandia"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = loads(text_data)
        
        # Salva o evento no banco de dados SQLite
        await self.save_event(data)

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'send_message',
                'message': data
            }
        )

    async def send_message(self, event):
        message = event['message']
        await self.send(text_data=dumps(message))

    @sync_to_async
    def save_event(self, data):
        # Aqui você salva os dados no SQLite
        eventos.objects.create(nome=data.get("nome"), descricao=data.get("descricao"))
