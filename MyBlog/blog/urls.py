from django.urls import path
from .views import home, register, login_view, logout_view, create_post

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create/', create_post, name='create_post'),
]