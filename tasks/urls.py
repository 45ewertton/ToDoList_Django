from django.urls import path

from .views import taskList, yourName, taskView, newTask

urlpatterns = [
    path('', taskList, name='task-list'),
    path('task/<int:id>', taskView, name="task-view"),
    path('newTask/', newTask, name="new-task"),


    path('yourname/<str:name>', yourName, name='your-name'),
]