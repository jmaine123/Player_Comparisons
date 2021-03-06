from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('follow/<int:user_id>&<int:u_id>', views.follow, name='follow'),
    path('unfollow/<int:user_id>&<int:u_id>', views.unfollow, name='unfollow')
]
