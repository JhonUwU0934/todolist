from django.urls import path 
from . import views
from .views import UserLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name= 'login'),
    path('logout/', LogoutView.as_view(next_page= 'login'), name= 'logout'),
    path('', views.index, name="index"),
    path('register/',RegisterPage.as_view(), name='register')
]
