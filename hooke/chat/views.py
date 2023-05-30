from django.shortcuts import render
from django.contrib.auth.models import User
from chat.models import Inbox, Message
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def inbox (request, user_id):
    gotten = Inbox.objects.filter((Q(user1_id=user_id,user2=request.user) | Q(user2_id=user_id,user1=request.user)))
    inbox = None
    chatting_with = User.objects.get(pk=user_id)
    if not gotten.exists():
        inbox = Inbox(user1 = request.user, user2 = chatting_with)
        inbox.save()
    else:
        inbox = Inbox.objects.filter((Q(user1_id=user_id,user2=request.user) | Q(user2_id=user_id,user1=request.user)))[0]
    params = {
    "sending_to":chatting_with,
    "messages": list(reversed( Message.objects.filter((Q(sender=user_id,receiver=request.user) |
                                        Q(receiver=user_id,sender=request.user))).order_by('-timestamp')[:10])),
    "inbox": inbox,
    "users": User.objects.exclude(id=request.user.id)
    }
    return render(request, 'chat/inbox.html', params)


@login_required()
def inbox (request):
    gotten = Inbox.objects.filter((Q(user2=request.user) | Q(user1=request.user)))
    params = {
    "users": User.objects.exclude(id=request.user.id)
    }
    return render(request, 'chat/inbox.html', params)

@login_required()
def view_chats(request):
    pass
