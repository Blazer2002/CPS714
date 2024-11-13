from django.urls import path
from .views.users import *
from .views.products import *
from .views.rewards import *
from .views.rewardtransaction import *

urlpatterns = [
    path('users/get-all/', get_all_users, name='get_all_users'),
    path('users/post/', create_user, name='create_user'),
    path('users/<int:pk>', specific_user, name='specific_user'),

    path('products/get-all/', get_all_products, name='get_all_products'),
    path('products/post/', create_product, name='create_product'),
    path('products/<int:pk>', specific_product, name='specific_product'),
]
