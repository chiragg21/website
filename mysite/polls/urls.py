# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('handle-button-click/', views.handle_button_click, name='handle_button_click'),
]
