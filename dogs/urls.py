from django.urls import path

from dogs.views import index

urlpatterns = [
    path('', index),
]