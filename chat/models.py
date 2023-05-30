from django.db import models
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync, sync_to_async
# Create your models here.




class Inbox(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1', editable=False)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2', editable=False)

    @property
    def name(self):
        return f"{self.user1.username} and {self.user2.username} inbox"
    @property
    @sync_to_async
    def async_name(self):
        return f"{self.user1.username}__{self.user2.username}_inbox"

class Message(models.Model):
    inbox = models.ForeignKey(Inbox, on_delete=models.CASCADE,editable=False, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', editable=False)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver', editable=False)
    content = models.TextField(editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)
