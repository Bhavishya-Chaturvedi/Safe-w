from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('voice_input/', views.voice_input, name='voice_input'),
]
