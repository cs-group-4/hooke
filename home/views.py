from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from chat.models import Inbox
from .models import Interests, Notifications
from django.contrib.auth import get_user_model

# Create your views here.

@login_required(login_url='/accounts/login/')
def home_view(requests):
    hookies = Profile.objects.exclude(owner=requests.user)
    interests = Interests.objects.filter(seeker=requests.user)
    # if interests.count() == 0:
    #     to_omit = []
    # else:
    #     to_omit = interests

    
    return render(requests, 'home/home.html', {'hookies':hookies, 'to_omit': interests})

def notifications_view(requests):
    notifcations = Notifications.objects.filter(to_user=requests.user)
    return render(requests, 'home/notifications.html', {'notifications': notifcations})

@login_required(login_url='/accounts/login/')
def profile_detail_view(requests, slug):
    profile = Profile.objects.get(owner=slug)
    hostels = Profile.hostels
    schools = Profile.schools
    return render(requests, 'home/profile.html', {'hookie':profile, 'hostels': hostels, 'schools': schools})


@login_required(login_url='/accounts/login/')
def interested_action(requests, slug):
    User = get_user_model()
    seeked_id = User.objects.get(id=slug)

    notification_entry = Notifications()
    notification_entry.from_user = requests.user
    notification_entry.to_user = seeked_id

    # for the type we need to check wheter its a like or a like back
    interests =  Interests.objects.filter(seeked_id=requests.user, seeker=seeked_id)
    if interests.count() != 0:
        # it should be a like back
         notification_entry.type = "like-back"
        # these two can now chat
         inbox = Inbox(user1 = requests.user, user2 = seeked_id)
         inbox.save()
    else:
        # its a like
        notification_entry.type = "like"
    notification_entry.save()

    entry = Interests()
    entry.seeker = requests.user
    entry.seeked = seeked_id
    
    
    entry.save()
    return redirect('home:home_page')

@login_required(login_url='/accounts/login/')
def theme_swap_action(requests):
    try:
        if requests.session['theme'] =="dark":
            requests.session['theme'] = "light"
        else:
            requests.session['theme'] = "dark"
    except:
        requests.session['theme'] = "dark"
    # if 'theme' in requests.session:
    #     if requests.session['theme'] == "dark":
            
    #     else:
    #         requests.session['theme'] = "dark"
    return redirect(requests.META.get('HTTP_REFERER'))