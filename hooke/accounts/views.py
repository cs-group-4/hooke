from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(requests):
  if requests.method == 'POST':
    form = UserCreationForm(requests.POST)
    if form.is_valid():
      form.save()
  else:
    form = UserCreationForm()  
  return render(requests, 'accounts/signup.html', { 'form': form })