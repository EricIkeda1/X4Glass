import json
from channels.generic.websocket import WebsocketConsumer

class EventConsumer(WebsocketConsumer):
    def connect(self):
        self.accept() 
        
    def disconnect(self, close_code):
        pass 

    def receive(self, text_data):
        event_data = json.loads(text_data)

        # Processa o evento recebido
        self.process_event(event_data)

    def process_event(self, event_data):
        formatted_event = {
            'sector': event_data.get('sector'),
            'product': event_data.get('product'),
            'date': event_data.get('date'),
            'max_idle': event_data.get('max_idle', None) 
        }

        self.send(text_data=json.dumps({
            'message': formatted_event
        }))
