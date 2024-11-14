from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *

# Get all reward
@api_view(['GET'])
def get_all_rewards(request):
    fetch_data = Rewards.objects.all()
    serializer = RewardsSerializer(fetch_data, many=True)
    return Response(serializer.data)

# Get all percent discount reward
@api_view(['GET'])
def get_all_percent_discount_rewards(request):
    fetch_data = Percentdiscountreward.objects.all()
    serializer = PercentDiscountRewardSerializer(fetch_data, many=True)
    return Response(serializer.data)

# Get all price discount reward
@api_view(['GET'])
def get_all_price_discount_rewards(request):
    fetch_data = Pricediscountreward.objects.all()
    serializer = PriceDiscountRewardSerializer(fetch_data, many=True)
    return Response(serializer.data)

# Get all product upgrade reward
@api_view(['GET'])
def get_all_product_upgrade_rewards(request):
    fetch_data = Productupgradereward.objects.all()
    serializer = ProductUpgradeRewardSerializer(fetch_data, many=True)
    return Response(serializer.data)

# Get all exclusive product reward
@api_view(['GET'])
def get_all_exclusive_product_rewards(request):
    fetch_data = Exclusiveproductreward.objects.all()
    serializer = ExclusiveProductRewardSerializer(fetch_data, many=True)
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
        serializer = RewardsSerializer(reward)
        return Response(serializer.data)
    
    #Update details of the specified reward
    elif request.method == 'PUT':
        serializer = RewardsSerializer(reward, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete the user
    elif request.method == 'DELETE':
        reward.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)