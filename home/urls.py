from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.home_view, name="home_page"),
    path('profile/<slug:slug>/', views.profile_detail_view, name="profile_page"),
    path('notifications/', views.notifications_view, name="notifications"),
    path('interested/<slug:slug>/', views.interested_action, name="interested"),
    path('theme_swap/', views.theme_swap_action, name="theme-swap"),
]
