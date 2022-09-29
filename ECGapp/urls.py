from django.urls import path
from .import views


urlpatterns = [
    path('upload', views.upload, name='index'),
    path('download', views.download, name='download'),
    path('uploading', views.uploading, name='uploading'),
    path('output', views.output, name='output'),
    path('', views.home, name='home'),
    path('login', views.admin_login, name='login'),
]
