import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from asgiref.sync import async_to_sync


class MessageConsumer(WebsocketConsumer):
    def connect(self):
        print('accept')
        self.accept()
    
    def disconnect(self, code):
        print('disconnect', code)
        return super().disconnect(code)
    
    def receive(self, text_data):
        message = json.loads(text_data)
        self.send(text_data=text_data)
        # return super().receive(text_data=text_data, bytes_data=bytes_data)


class RoomConsumer_(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
        print('channel', self.channel_name)
        self.accept()
    
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        return super().disconnect(code)
    
    def receive(self, text_data):
        message = json.loads(text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message['message']
            }
        )
    
    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'message': message
        }))


class RoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
    
    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        return await super().disconnect(code)
    
    async def receive(self, text_data):
        message = json.loads(text_data)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message['message']
            }
        )
    
    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))