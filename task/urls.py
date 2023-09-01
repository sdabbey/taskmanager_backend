from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('create_task/', create_task, name='create_task'),
    path('delete_task/<int:id>/', delete_task, name='delete_task'),
]