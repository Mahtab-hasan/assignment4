from django.urls import path
from .views import show_tasks, add_task, edit_task, delete_task

urlpatterns = [
    path('', show_tasks, name='show_tasks'),
    path('add/', add_task, name='add_task'),
    path('edit/<int:id>', edit_task, name='edit_task'),
    path('delete/<int:id>', delete_task, name='delete_task'),
]
