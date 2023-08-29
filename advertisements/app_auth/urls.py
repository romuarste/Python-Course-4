from django.urls import path

from .views import register, login_view, profile, logout_view


urlpatterns = [   
    path("register.html", register, name='register'),
    path("login.html", login_view, name='login'),
    path("profile.html", profile, name='profile'),
    path("logout", logout_view, name='logout' )
]