from django.urls import path
from .views.users import *

urlpatterns = [
    path('users/get-all/', get_all_users, name='get_all_users'),
    path('users/post/', create_user, name='create_user'),
    path('users/<int:pk>', specific_user, name='specific_user'),
]
