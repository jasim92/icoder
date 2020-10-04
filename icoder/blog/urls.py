from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogHome, name = 'BlogHome'),
    path('postComments', views.postComments, name = 'postComments'),
    path('<str:slug>', views.blogPost, name = 'BlogPost'),
]