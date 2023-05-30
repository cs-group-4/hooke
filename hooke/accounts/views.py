from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .models import Profile
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup_view(requests):
  if requests.method == 'POST':
    form = UserCreationForm(requests.POST)
    if form.is_valid():
      user = form.save()
      login(requests, user)
      return redirect('accounts:create-profile')

  else:
    form = UserCreationForm()  
  return render(requests, 'accounts/signup.html', { 'form': form })

def login_view(requests):
  if requests.method == 'POST':
    form = AuthenticationForm(data=requests.POST)
    if form.is_valid():
      user = form.get_user()
      login(requests, user)
      return redirect('home:home_page')
  else:
    form = AuthenticationForm()  
  return render(requests, 'accounts/login.html', { 'form': form })

@login_required(login_url='/accounts/login/')
def create_profile_view(requests):
  if requests.method == "POST":
    profile_form = forms.Profile_form(requests.POST, requests.FILES)
    if profile_form.is_valid():
      # save to db
      instance = profile_form.save(commit=False)
      instance.owner = requests.user
      instance.save()
      return redirect('home:home_page')
  else:
    profile_form = forms.Profile_form()
  return render(requests, 'accounts/create_profile.html', {'form': profile_form})