from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *
import json

# Get all reward transactions
@api_view(['GET'])
def get_all_rewardtransactions(request):
    rewardtransaction = Rewardtransaction.objects.all().order_by('-date')
    rewardtransaction_data = RewardTransactionSerializer(rewardtransaction, many=True).data
    
    for entry in rewardtransaction_data:
        # Get the User and Reward Entry by Foreign Key
        user = Users.objects.get(pk=entry["user"])
        user_data = UsersSerializer(user).data

        reward = Rewards.objects.get(pk=entry["reward"])
        reward_data = RewardsSerializer(reward).data

        # Remove Duplicate Users and Rewards ID
        entry.pop("user")
        entry.pop("reward")

        # Join User and Reward to Transaction Entry
        entry.update(user_data.copy())
        entry.update(reward_data.copy())

    return Response(rewardtransaction_data)

# Get all reward transactions by user
# Query by active or inactive transactions
@api_view(['GET'])
def get_all_reward_by_user(request, active, userid):
    rewardtransaction = Rewardtransaction.objects.filter(user_id=userid, active=active).order_by('-date')
    rewardtransaction_data = RewardTransactionSerializer(rewardtransaction, many=True).data
    
    for entry in rewardtransaction_data:
        # Get the Rewards Entry
        reward = Rewards.objects.get(pk=entry["reward"])
        reward_data = RewardsSerializer(reward).data

        # Remove Duplicate Rewards ID
        entry.pop("reward")

        # Join Reward to Transaction Entry
        entry.update(reward_data.copy())

    return Response(rewardtransaction_data)


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
    