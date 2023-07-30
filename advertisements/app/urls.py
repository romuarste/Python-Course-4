from django.urls import path

from .views import index, top_sellers, advertisement, advertisement_post, register, login, profile

urlpatterns = [
    path("", index),
    path("index.html", index, name='index'),
    path("top-sellers.html", top_sellers, name='top_sellers'),
    path("advertisement.html", advertisement, name='advertisement'),
    path("advertisement-post.html", advertisement_post, name='advertisement_post'),
    path("register.html", register, name='register'),
    path("login.html", login, name='login'),
    path("profile.html", profile, name='profile')
]