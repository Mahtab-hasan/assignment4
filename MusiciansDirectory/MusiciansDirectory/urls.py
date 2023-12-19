from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/',include('musician_app.urls')),
    path('',include('album_app.urls')),

]