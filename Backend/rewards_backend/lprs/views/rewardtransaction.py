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
    # Edit keys to match reward transaction format
    json_data = request.data
    json_data["user"] = json_data["user_id"]
    json_data["reward"] = json_data["reward_id"]

    # Check if entry is correct
    serializer = RewardTransactionSerializer(data=json_data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Save entry to database
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


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
        rewardtransaction_data = RewardTransactionSerializer(rewardtransaction).data

        # Get the Rewards Entry
        reward = Rewards.objects.get(pk=rewardtransaction_data["reward"])
        reward_data = RewardsSerializer(reward).data

        # Remove Duplicate Rewards ID
        rewardtransaction_data.pop("reward")

        # Join Reward to Transaction Entry
        rewardtransaction_data.update(reward_data.copy())

        return Response(rewardtransaction_data)
    
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
    