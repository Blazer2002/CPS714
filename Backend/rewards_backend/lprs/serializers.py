from rest_framework import serializers
from .models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class RewardTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rewardtransaction
        fields = '__all__'

class RewardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rewards
        fields = '__all__'

class PercentDiscountRewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Percentdiscountreward
        fields = '__all__'

class PriceDiscountRewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricediscountreward
        fields = '__all__'

class ProductUpgradeRewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productupgradereward
        fields = '__all__'

class ExclusiveProductRewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exclusiveproductreward
        fields = '__all__'
