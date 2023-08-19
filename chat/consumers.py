import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        uuid = self.scope["url_route"]["kwargs"]["uuid"]
        
        async_to_sync(self.channel_layer.group_add)(
            f'chat_{uuid}', self.channel_name
        )
        self.accept()

    def receive(self, text_data):
        print(self.scope["user"].username)
        uuid = self.scope["url_route"]["kwargs"]["uuid"]
        async_to_sync(self.channel_layer.group_send)(
            f'chat_{uuid}',
            {
                'type':'chat_message',
                'message':text_data,
            }
        )

    def chat_message(self, event):
        self.send(text_data=json.dumps({
            'message':event["message"],
            'created':self.scope["user"].username
            }))


    def disconnect(self, close_code):
        uuid = self.scope["url_route"]["kwargs"]["uuid"]
        self.channel_layer.group_discard(f'chat_{uuid}', self.channel_name)
