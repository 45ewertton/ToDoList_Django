from django.urls import path

from .views import taskList, yourName

urlpatterns = [
    path('', taskList, name='task-list'),
    path('yourname/<str:name>', yourName, name='your-name')
]