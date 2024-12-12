# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),           
    path('post/<int:id>/', views.post_detail, name='post_detail'), 
    path('post/new/', views.post_create, name='post_create'), 
    path('post/<int:id>/edit/', views.post_edit, name='post_edit'),  
]
