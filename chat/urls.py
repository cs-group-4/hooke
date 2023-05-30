from django.urls import  path
from . import  views
app_name = "chats"
urlpatterns = [
    path('',views.inbox, name="chat"),
    path('<int:user_id>',views.inbox_message, name="chat"),
]