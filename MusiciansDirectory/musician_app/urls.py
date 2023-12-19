from django.urls import path
from .views import home, create_musician,edit_musician,delete_musician
urlpatterns = [
    path('', home , name='musician_home'),
    path('create/', create_musician , name='create_musician'),
    path('edit/<int:musician_id>/', edit_musician , name='edit_musician'),
    path('delete/<int:musician_id>/', delete_musician , name='delete_musician'),
]