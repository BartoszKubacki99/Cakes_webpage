from django.urls import path
from .views import login_user, logout_user, register_user

urlpatterns = [
    path('login_user/', login_user, name='login'),
    path('logout_user/', logout_user, name='logout'),
    path('register/', register_user, name='register_user')
]