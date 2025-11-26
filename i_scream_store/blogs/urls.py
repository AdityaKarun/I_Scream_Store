from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.blogs_home, name='blogs_home'),
    path('signin/', views.blogs_signin, name='blogs_signin'),
    path('signup/', views.blogs_signup, name='blogs_signup'),
    path('signout/', views.blogs_signout, name='blogs_signout'),
]