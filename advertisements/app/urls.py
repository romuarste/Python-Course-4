from django.urls import path

from .views import index, top_sellers, advertisement, advertisement_post

urlpatterns = [
    path("", index),
    path("index.html", index, name='index'),
    path("top-sellers.html", top_sellers, name='top_sellers'),
    path("advertisement.html/<int:pk>", advertisement, name='advertisement'),
    path("advertisement-post.html", advertisement_post, name='advertisement_post'),
]