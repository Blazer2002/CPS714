from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *

# Get all user data
@api_view(['GET'])
def get_all_users(request):
    fetch_data = Users.objects.all()
    serializer = UsersSerializer(fetch_data, many=True)
    return Response(serializer.data)

# Create a new user
@api_view(['POST'])
def create_user(request):
    serializer = UsersSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get / Update / Delete a specific user
@api_view(['GET', 'PUT', 'DELETE'])
def specific_user(request, pk):
    # Fetch the data of the user using the primary key
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_BAD_REQUEST)

    # Get the specified user
    if request.method == 'GET':
        serializer = UsersSerializer(user)
        return Response(serializer.data)
    
    # Update details of the specified user
    elif request.method == 'PUT':
        serializer = UsersSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete the user
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
