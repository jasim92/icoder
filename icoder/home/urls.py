from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'Home'),
    path('about/', views.about, name = 'About'),
    path('contact/', views.contact, name = 'Contact'),
    path('search/', views.search, name = 'Search'),
    path('signup/', views.handleSignUp, name = 'Handle SignUp'),
    path('login/', views.handleLogin, name = 'Handle Login'),
    path('logout/', views.handleLogout, name = 'Handle Logout'),
]