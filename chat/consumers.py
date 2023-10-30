import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth.decorators import login_required

from chat.models import UserProfile


class ChatConsumer(AsyncWebsocketConsumer):

    @login_required
    async def connect(self):
        self.room_group_name = 'Chat-Room-1'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        if self.scope['user'].is_authenticated:
            try:
                profile = UserProfile.objects.get(user=self.scope['user'])
                username = profile.user.username
            except UserProfile.DoesNotExist:
                username = 'Anonymous'
        else:
            username = 'Anonymous'

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': f'{username} has joined {self.room_group_name}'
            }
        )

        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = self.scope['user']
        if user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=user)
                username = profile.user.username
            except UserProfile.DoesNotExist:
                username = 'Anonymous'
        else:
            username = 'Anonymous'

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))
