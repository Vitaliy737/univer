from .views import index, about, contact
from django.urls import path

urlpatterns = [
    path('', index),
    path('index', index),
    path('about', about),
    path('contact', contact)
]
