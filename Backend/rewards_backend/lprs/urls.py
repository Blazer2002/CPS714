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

    path('rewards/get-all/', get_all_rewards, name = 'get_all_rewards'),
    path('percentdisccountrewards/get-all/', get_all_percent_discount_rewards, name = 'get_all_percent_discount_rewards'),
    path('pricedisccountrewards/get-all/', get_all_price_discount_rewards, name = 'get_all_price_discount_rewards'),
    path('productupgraderewards/get-all/', get_all_product_upgrade_rewards, name = 'get_all_product_upgrade_rewards'),
    path('exclusiveupgraderewards/get-all/', get_all_exclusive_product_rewards, name = 'get_all_exclusive_product_rewards'),
    path('rewards/post/<int:type>', create_reward, name='create_reward'),
    path('rewards/<int:pk>', specific_reward, name='specific_reward'),

    path('rewardtransactions/get-all/', get_all_rewardtransactions, name = 'get_all_rewardtransactions'),
    path('rewardbyuser/<int:active>/<int:userid>', get_all_reward_by_user, name = 'get_all_reward_by_user'),
    # path('rewardtransactions/post/', create_rewardtransaction, name='create_rewardtransaction'),
    # path('rewardtransactions/<int:pk>', specific_rewardtransaction, name='specific_rewardtransaction'),
]