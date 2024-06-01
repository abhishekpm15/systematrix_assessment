from django.urls import path
from .views import button_view

urlpatterns = [
    path('button/', button_view, name='button_view'),
]
