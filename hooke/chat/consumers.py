import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer, AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync, sync_to_async
from .models import Inbox, Message
from channels.db import database_sync_to_async
from django.contrib.auth.models import User


class ChatConsumer(AsyncWebsocketConsumer):
    @database_sync_to_async
    def get_inbox(self, inbox_ob):
        return Inbox.objects.get(pk=inbox_ob)

    async def connect(self):
        # user_id = self.scope['url_route']['kwargs']['user_id']
        # to_id = self.scope['url_route']['kwargs']['to_id']
        inbox_ob = self.scope['url_route']['kwargs']['inbox']
        # gotten = await self.get_inbox(inbox_ob)

        gotten = await database_sync_to_async(Inbox.objects.get)(pk=inbox_ob)


        print(gotten)
        name = await gotten.async_name
        print(name)
        self.room_group_name = f"chat_inbox_{name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        await self.send(text_data=json.dumps({
            'type': 'connection established',
            'message': 'you are now connected mazafaka'
        }))

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = text_data_json["username"]
        user_ob = text_data_json["user"]
        inb = text_data_json['inbox']

        gotten = await database_sync_to_async(Inbox.objects.get)(pk=int(inb))
        user_ref = await database_sync_to_async(User.objects.get)(pk=int(user_ob))

        chatting_with = text_data_json['reciever']
        print("wasdsa")
        print(chatting_with)
        receipt = await  database_sync_to_async(User.objects.get)(pk=int(chatting_with))
        # msg = Message()
        print(inb)
        msg = await database_sync_to_async(Message.objects.create)(sender=user_ref,receiver=receipt,
                      inbox=gotten,content=message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message': message,
                "username":user
            }
        )

    async def chat_message(self, e):
        message = e['message']

        await self.send(text_data=json.dumps(
            {
            'type': 'chat',
            'message': message,
            'username':e['username']
            }
        ))