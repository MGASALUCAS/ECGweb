from django.urls import path
from .import views


urlpatterns = [
    path('upload', views.upload, name='index'),
    path('download', views.download, name='download'),
    path('output', views.output, name='output'),
    path('', views.home, name='home'),
]
