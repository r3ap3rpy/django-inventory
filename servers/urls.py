from django.urls import path
from . import views

urlpatterns = [
    path('',views.servers, name = 'servers'),
    path('create-server/', views.createServer, name = 'create-server'),
    path('update-server/<str:pk>/', views.updateServer, name = 'update-server'),
    path('delete-server/<str:pk>/', views.deleteServer, name = 'delete-server'),
]