from django.urls import path
from .views import home as album_home, create_album, edit_album, delete_album

urlpatterns = [
    path('', album_home,name="album_home"),
    path('create/',create_album,name='create_album'),
    path('edit/<int:album_id>/',edit_album,name='edit_album'),
    path('delte/<int:album_id>/',delete_album,name='delete_album'),

]