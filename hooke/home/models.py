from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Interests(models.Model):
    """
    ### Keeps a table of those people who are clickin the interested button
    """
    seeker = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name='intereted')
    seeked = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name='seeked')
     
    def __str__(self):
        return self.seeker.username
    
class Notifications(models.Model):
    """
    ### Keeps a log of notifications
    """
    from_user = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name='to_user')
    type = models.CharField(max_length=10) # like or like-back
    status = models.CharField(max_length=10, default="unread") # read / unread
    date = models.DateTimeField(auto_now_add=True, null=True)
     
    
        