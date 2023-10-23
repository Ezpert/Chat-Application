import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_group_name = None
        self.room_name = None

    async def connect(self):
        # Connect to the WebSocket
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        pass

    async def disconnect(self, close_code):
        # Disconnect from the WebSocket
        pass

    async def receive(self, text_data):
        # Handle incoming messages
        message = json.loads(text_data)

        await self.channel_layer.group_send(
            self.room_group_name,


        )

        pass
