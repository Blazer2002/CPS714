from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *

# Note: Update lprs/serializers.py and lprs/urls.py

# Get all reward transactions
@api_view(['GET'])
def get_all_rewardtransactions(request):
    fetch_data = Rewardtransactionview.objects.all()
    serializer = RewardTransactionViewSerializer(fetch_data, many=True)
    return Response(serializer.data)
# Get all reward transactions by user
@api_view(['GET'])
def get_all_reward_by_user(request, userid):
    fetch_data = Rewardtransactionview.objects.filter(user_id=userid)
    serializer = RewardTransactionViewSerializer(fetch_data, many=True)
    return Response(serializer.data)
# Get all reward transactions by reward
@api_view(['GET'])
def get_all_reward_by_reward(request, rewardid):
    fetch_data = Rewardtransactionview.objects.filter(reward_id=rewardid)
    serializer = RewardTransactionViewSerializer(fetch_data, many=True)
    return Response(serializer.data)
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
        serializer = RewardTransactionViewSerializer(rewardtransaction)
        return Response(serializer.data)
    
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
    