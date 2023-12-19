from django.urls import path 
from .views import add_category, delete_category

urlpatterns = [
    path('add/', add_category,name='add_category'),
    path('delete/<int:id>', delete_category,name='delete_category'),
]
