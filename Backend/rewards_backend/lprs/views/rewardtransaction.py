from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *
import json

# Note: Update lprs/serializers.py and lprs/urls.py

# Get all reward transactions
@api_view(['GET'])
def get_all_rewardtransactions(request):
    rt_data = Rewardtransaction.objects.all()
    rt_serializer = RewardTransactionSerializer(rt_data, many=True)

    rt_list = list()

    for jsn in rt_serializer.data:
        r_id = jsn['reward']
        reward = Rewards.objects.filter(pk=r_id)
        r_serializer = RewardsSerializer(reward)
        data = jsn
        data.update(r_serializer.data)
        data.pop('reward')
        rt_list.append(data)

    return Response(rt_list)
# Get all reward transactions by user
@api_view(['GET'])
def get_all_reward_by_user(request, userid):
    rt_data = Rewardtransaction.objects.filter(user_id=userid)
    rt_serializer = RewardTransactionSerializer(rt_data, many=True)
    r_id = rt_serializer.data['reward_id']

    r_data = Rewards.objects.filter(pk=r_id)
    r_serializer = RewardsSerializer(r_data, many=True)

    viewdata = rt_serializer.data
    viewdata.update(r_serializer.data)

    return Response(viewdata)
# Get all reward transactions by reward
@api_view(['GET'])
def get_all_reward_by_reward(request, rewardid):
    rt_data = Rewardtransaction.objects.filter(reward_id=rewardid)
    rt_serializer = RewardTransactionSerializer(rt_data, many=True)
    r_id = rt_serializer.data['reward_id']

    r_data = Rewards.objects.filter(pk=r_id)
    r_serializer = RewardsSerializer(r_data, many=True)

    viewdata = rt_serializer.data
    viewdata.update(r_serializer.data)
# Create a new reward transaction
@api_view(['POST'])
def create_rewardtransaction(request):
    serializer = RewardTransactionSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Get / Update / Delete a specific reward transaction
@api_view(['GET', 'PUT', 'DELETE'])
def specific_rewardtransaction(request, pk):
     # Fetch the data of the reward using the primary key
    try:
        rewardtransaction = Rewardtransaction.objects.get(pk=pk)
    except Rewardtransaction.DoesNotExist:
        return Response(status=status.HTTP_404_BAD_REQUEST)
    
    # Get the specified user
    if request.method == 'GET':
        rt_serializer = RewardTransactionSerializer(rewardtransaction)

        reward = rt_serializer.validated_data.get('Rewards')
        r_serializer = RewardsSerializer(reward)

        viewdata = rt_serializer.data
        viewdata.update(r_serializer.data)
        return Response(viewdata)
    
    #Update details of the specified reward transaction
    elif request.method == 'PUT':
        serializer = RewardTransactionSerializer(rewardtransaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete the user
    elif request.method == 'DELETE':
        rewardtransaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    