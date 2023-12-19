from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/',include('task.urls')),
    path('category/',include('category.urls')),
    path('',lambda request: redirect('add_task'),name='home'),
]
