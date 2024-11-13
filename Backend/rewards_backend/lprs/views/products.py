from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *

# Get all product data
@api_view(['GET'])
def get_all_products(request):
    fetch_data = Products.objects.all()
    serializer = ProductsSerializer(fetch_data, many=True)
    return Response(serializer.data)

# Create a new product
@api_view(['POST'])
def create_product(request):
    serializer = ProductsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get / Update / Delete a specific product
@api_view(['GET', 'PUT', 'DELETE'])
def specific_product(request, pk):
    # Fetch the data of the product using the primary key
    try:
        product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_BAD_REQUEST)

    # Get the specified product
    if request.method == 'GET':
        serializer = ProductsSerializer(product)
        return Response(serializer.data)
    
    # Update details of the specified product
    elif request.method == 'PUT':
        serializer = ProductsSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete the product
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
