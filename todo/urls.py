from django.urls import path
from .views import index, add_task, complete_task, delete_task

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_task, name='add_task'),
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]
