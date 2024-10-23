import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class EventConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept() 
        
    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        event_data = json.loads(text_data)
        await self.process_event(event_data)

    async def process_event(self, event_data):
        formatted_event = {
            'sector': event_data.get('sector'),
            'product': event_data.get('product'),
            'date': event_data.get('date'),
            'max_idle': event_data.get('max_idle', None) 
        }

        await self.send(text_data=json.dumps(formatted_event))

