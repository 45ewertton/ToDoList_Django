from django.urls import path

from .views import taskList, yourName, taskView, newTask, editTask, deleteTask

urlpatterns = [
    path('', taskList, name='task-list'),
    path('task/<int:id>', taskView, name="task-view"),
    path('newTask/', newTask, name="new-task"),
    path('editTask/<int:id>', editTask, name="edit-task"),
    path('deleteTask/<int:id>', deleteTask, name="delete-task"),


    path('yourname/<str:name>', yourName, name='your-name'),
]