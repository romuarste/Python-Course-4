from django.urls import path

from .views import index, top_sellers

urlpatterns = [
    path("", index),
    path("index.html", index),
    path("top-sellers.html", top_sellers)
]