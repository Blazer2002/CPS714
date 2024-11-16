from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *
import json

# Get all reward
@api_view(['GET'])
def get_all_rewards(request):
    fetch_data = Rewards.objects.all()
    serializer = RewardsSerializer(fetch_data, many=True)
    return Response(serializer.data)

# Get all percent discount reward
@api_view(['GET'])
def get_all_percent_discount_rewards(request):
    fetch_data = Percentdiscountrewardview.objects.all()
    serializer = PercentDiscountRewardViewSerializer(fetch_data, many=True)
    return Response(serializer.data)

# Get all price discount reward
@api_view(['GET'])
def get_all_price_discount_rewards(request):
    fetch_data = Pricediscountrewardview.objects.all()
    serializer = PriceDiscountRewardViewSerializer(fetch_data, many=True)
    return Response(serializer.data)

# Get all product upgrade reward
@api_view(['GET'])
def get_all_product_upgrade_rewards(request):
    fetch_data = Productupgraderewardview.objects.all()
    serializer = ProductUpgradeRewardViewSerializer(fetch_data, many=True)
    return Response(serializer.data)

# Get all exclusive product reward
@api_view(['GET'])
def get_all_exclusive_product_rewards(request):
    fetch_data = Exclusiveproductrewardview.objects.all()
    serializer = ExclusiveProductRewardViewSerializer(fetch_data, many=True)
    return Response(serializer.data)

# Create a new reward
# Make sure to update the discount/upgrade/exclusive table
@api_view(['POST'])
def create_reward(request, type):
    if type == 0:
        serializer = PercentDiscountRewardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        serializer = RewardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif type == 1:
        serializer = PriceDiscountRewardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        serializer = RewardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        
    elif type == 2:
        serializer = ProductUpgradeRewardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        serializer = RewardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
  
    elif type == 3:
        serializer = ExclusiveProductRewardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        serializer = RewardsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
  
    else:
        print("not a valid type input")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

# Get / Update / Delete a specific reward
# Make sure to update the discount/upgrade/exclusive table
@api_view(['GET', 'PUT', 'DELETE'])
def specific_reward(request, pk):
     # Fetch the data of the reward using the primary key
    try:
        reward = Rewards.objects.get(pk=pk)
    except Rewards.DoesNotExist:
        return Response(status=status.HTTP_404_BAD_REQUEST)
    
    # Get the specified user
    if request.method == 'GET':
        if(Pricediscountrewardview.objects.filter(pk=pk).exists()):
            price_discount = Pricediscountrewardview.objects.get(pk=pk)
            serializer = PriceDiscountRewardViewSerializer(price_discount)
        elif(Percentdiscountrewardview.objects.filter(pk=pk).exists()):
            percent_discount = Percentdiscountrewardview.objects.get(pk=pk)
            serializer = PercentDiscountRewardViewSerializer(percent_discount)
        elif(Productupgraderewardview.objects.filter(pk=pk).exists()):
            product_upgrade = Productupgraderewardview.objects.get(pk=pk)
            serializer = ProductUpgradeRewardViewSerializer(product_upgrade)
        elif(Exclusiveproductrewardview.objects.filter(pk=pk).exists()):
            exclusive = Exclusiveproductrewardview.objects.get(pk=pk)
            serializer = ExclusiveProductRewardViewSerializer(exclusive)

        return Response(serializer.data)
    
    #Update details of the specified reward
    elif request.method == 'PUT':
        serializer = RewardsSerializer(reward, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if(Pricediscountreward.objects.filter(pk=pk).exists()):
            price_discount = Pricediscountreward.objects.get(pk=pk)
            serializer = PriceDiscountRewardSerializer(price_discount, data=request.data)
            if serializer.is_valid():
                serializer.save()
            price_discount = Pricediscountrewardview.objects.get(pk=pk)
            serializer = PriceDiscountRewardViewSerializer(price_discount)
            return Response(serializer.data)
        elif(Percentdiscountreward.objects.filter(pk=pk).exists()):
            percent_discount = Percentdiscountreward.objects.get(pk=pk)
            serializer = PercentDiscountRewardSerializer(percent_discount, data=request.data)
            if serializer.is_valid():
                serializer.save()
            percent_discount = Percentdiscountrewardview.objects.get(pk=pk)
            serializer = PercentDiscountRewardViewSerializer(percent_discount)
            return Response(serializer.data)
        elif(Productupgradereward.objects.filter(pk=pk).exists()):
            product_upgrade = Productupgradereward.objects.get(pk=pk)
            serializer = ProductUpgradeRewardSerializer(product_upgrade, data=request.data)
            if serializer.is_valid():
                serializer.save()
            product_upgrade = Productupgraderewardview.objects.get(pk=pk)
            serializer = ProductUpgradeRewardViewSerializer(product_upgrade)
            return Response(serializer.data)
        elif(Exclusiveproductreward.objects.filter(pk=pk).exists()):
            exclusive = Exclusiveproductreward.objects.get(pk=pk)
            serializer = ExclusiveProductRewardSerializer(exclusive, data=request.data)
            if serializer.is_valid():
                serializer.save()
            exclusive = Exclusiveproductrewardview.objects.get(pk=pk)
            serializer = ExclusiveProductRewardViewSerializer(exclusive)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete the user
    elif request.method == 'DELETE':
        reward.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)