from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', include('myapp.urls')),
    path('', views.task_view),  # This makes the homepage load your task page
]
