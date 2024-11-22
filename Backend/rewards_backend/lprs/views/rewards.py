from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *

import requests
import json
from django.urls import include, path

# Get all reward
@api_view(['GET'])
def get_all_rewards(request):
    fetch_data = Rewards.objects.all()
    serializer = RewardsSerializer(fetch_data, many=True)
    return Response(serializer.data)

# Get all percent discount reward
@api_view(['GET'])
def get_all_percent_discount_rewards(request):
    fetch_percent_data = Percentdiscountreward.objects.all()
    percent_serializer = PercentDiscountRewardSerializer(fetch_percent_data, many=True)
    percent_json = percent_serializer.data

    # Create a view of Percent Discount Rewards Table
    for entry in percent_json:
        # Edit Percent Keys - Avoid Duplications in Join Operator
        entry["reward_id"] = entry.pop("reward")
        entry["product_id"] = entry.pop("product")
        entry["discountpercent"] = entry.pop("percent")

        # Edit Reward Keys - Avoid Duplications in Join Operator
        fetch_reward_data = Rewards.objects.get(pk=entry['reward_id'])
        reward_serializer = RewardsSerializer(fetch_reward_data)
        reward_json = reward_serializer.data

        reward_json.pop("reward_id")
        reward_json["rewardname"] = reward_json.pop("title")
        reward_json["rewardimage"] = reward_json.pop("image")
        reward_json["rewarddescription"] = reward_json.pop("description")

        # Edit Product Keys - Avoid Duplications in Join Operator
        fetch_product_data = Products.objects.get(pk=entry['product_id'])
        products_serializer = ProductsSerializer(fetch_product_data)
        product_json = products_serializer.data

        product_json.pop("product_id")
        product_json["productprice"] = product_json.pop("price")
        product_json["productimage"] = product_json.pop("image")
        product_json["productdescription"] = product_json.pop("description")

        # Join Reward and Product to Percent Entry
        entry.update(reward_json.copy())
        entry.update(product_json.copy())

    return Response(percent_json)

# Get all price discount reward
@api_view(['GET'])
def get_all_price_discount_rewards(request):
    fetch_price_data = Pricediscountreward.objects.all()
    price_serializer = PriceDiscountRewardSerializer(fetch_price_data, many=True)
    price_json = price_serializer.data

    # Create a view of Price Discount Rewards Table
    for entry in price_json:
        # Edit Percent Keys - Avoid Duplications in Join Operator
        entry["reward_id"] = entry.pop("reward")
        entry["product_id"] = entry.pop("product")
        entry["discountprice"] = entry.pop("price")

        # Edit Reward Keys - Avoid Duplications in Join Operator
        fetch_reward_data = Rewards.objects.get(pk=entry['reward_id'])
        reward_serializer = RewardsSerializer(fetch_reward_data)
        reward_json = reward_serializer.data

        reward_json.pop("reward_id")
        reward_json["rewardname"] = reward_json.pop("title")
        reward_json["rewardimage"] = reward_json.pop("image")
        reward_json["rewarddescription"] = reward_json.pop("description")

        # Edit Product Keys - Avoid Duplications in Join Operator
        fetch_product_data = Products.objects.get(pk=entry['product_id'])
        products_serializer = ProductsSerializer(fetch_product_data)
        product_json = products_serializer.data

        product_json.pop("product_id")
        product_json["productprice"] = product_json.pop("price")
        product_json["productimage"] = product_json.pop("image")
        product_json["productdescription"] = product_json.pop("description")

        # Join Reward and Product to Price Entry
        entry.update(reward_json.copy())
        entry.update(product_json.copy())

    return Response(price_json)

# Get all product upgrade reward
@api_view(['GET'])
def get_all_product_upgrade_rewards(request):
    fetch_upgrade_data = Productupgradereward.objects.all()
    upgrade_serializer = ProductUpgradeRewardSerializer(fetch_upgrade_data, many=True)
    upgrade_json = upgrade_serializer.data

    # Create a view of Upgrade Product Rewards Table
    for entry in upgrade_json:
        # Edit Percent Keys - Avoid Duplications in Join Operator
        entry["reward_id"] = entry.pop("reward")
        entry["prev_product_id"] = entry.pop("prevproduct")
        entry["next_product_id"] = entry.pop("nextproduct")

        # Edit Reward Keys - Avoid Duplications in Join Operator
        fetch_reward_data = Rewards.objects.get(pk=entry['reward_id'])
        reward_serializer = RewardsSerializer(fetch_reward_data)
        reward_json = reward_serializer.data

        reward_json.pop("reward_id")
        reward_json["rewardname"] = reward_json.pop("title")
        reward_json["rewardimage"] = reward_json.pop("image")
        reward_json["rewarddescription"] = reward_json.pop("description")

        # Edit Previous Product Keys - Avoid Duplications in Join Operator
        fetch_prev_product_data = Products.objects.get(pk=entry['prev_product_id'])
        prev_products_serializer = ProductsSerializer(fetch_prev_product_data)
        prev_product_json = prev_products_serializer.data

        prev_product_json.pop("product_id")
        prev_product_json["prevproductprice"] = prev_product_json.pop("price")
        prev_product_json["prevproductimage"] = prev_product_json.pop("image")
        prev_product_json["prevproductdescription"] = prev_product_json.pop("description")

        # Edit Next Product Keys - Avoid Duplications in Join Operator
        fetch_next_product_data = Products.objects.get(pk=entry['next_product_id'])
        next_products_serializer = ProductsSerializer(fetch_next_product_data)
        next_product_json = next_products_serializer.data

        next_product_json.pop("product_id")
        next_product_json["nextproductprice"] = next_product_json.pop("price")
        next_product_json["nextproductimage"] = next_product_json.pop("image")
        next_product_json["nextproductdescription"] = next_product_json.pop("description")

        # Join Reward and Product to Upgrade Entry
        entry.update(reward_json.copy())
        entry.update(prev_product_json.copy())
        entry.update(next_product_json.copy())

    return Response(upgrade_json)


# Get all exclusive product reward
@api_view(['GET'])
def get_all_exclusive_product_rewards(request):
    fetch_exclusive_data = Exclusiveproductreward.objects.all()
    exclusive_serializer = ExclusiveProductRewardSerializer(fetch_exclusive_data, many=True)
    exclusive_json = exclusive_serializer.data

    # Create a view of Exclusive Product Rewards Table
    for entry in exclusive_json:
        # Edit Percent Keys - Avoid Duplications in Join Operator
        entry["reward_id"] = entry.pop("reward")
        entry["product_id"] = entry.pop("product")

        # Edit Reward Keys - Avoid Duplications in Join Operator
        fetch_reward_data = Rewards.objects.get(pk=entry['reward_id'])
        reward_serializer = RewardsSerializer(fetch_reward_data)
        reward_json = reward_serializer.data

        reward_json.pop("reward_id")
        reward_json["rewardname"] = reward_json.pop("title")
        reward_json["rewardimage"] = reward_json.pop("image")
        reward_json["rewarddescription"] = reward_json.pop("description")

        # Edit Product Keys - Avoid Duplications in Join Operator
        fetch_product_data = Products.objects.get(pk=entry['product_id'])
        products_serializer = ProductsSerializer(fetch_product_data)
        product_json = products_serializer.data

        product_json.pop("product_id")
        product_json["productprice"] = product_json.pop("price")
        product_json["productimage"] = product_json.pop("image")
        product_json["productdescription"] = product_json.pop("description")

        # Join Reward and Product to Exclusive Entry
        entry.update(reward_json.copy())
        entry.update(product_json.copy())

    return Response(exclusive_json)

# Create a new reward
# Make sure to update the discount/upgrade/exclusive table
@api_view(['POST'])
def create_reward(request, type):
    # Create reward entry

    print(request.data['points'])




    # reward = Rewards.objects.create(
    #     points = request.data['points'],
    #     end = request.data['end'],
    #     title = request.data['rewardname'],
    #     image = request.data['rewardimage'],
    #     description = request.data['rewarddescription']
    # )

    # # Check if reward data is valid
    # reward_serializer = RewardsSerializer(reward)
    # if not reward_serializer.is_valid():
    #     reward.delete()
    #     return Response(reward_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # # Create percent discount reward entry
    # percent = Percentdiscountreward.objects.create(
    #     reward = reward.id,
    #     product_id = request.data['product_id'],
    #     discountpercent = request.data['discountpercent']
    # )

    # # Check if percent data is valid
    # percent_serializer = PercentDiscountRewardSerializer(percent)
    # if not percent_serializer.is_valid():
    #     percent.delete()
    #     return Response(percent_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    







    idk = Rewards.objects.create(
        points = 100,
        end = None,
        title = "idk",
        image = None,
        description = None
    )
    idk_serializer = RewardsSerializer(idk)

    return Response(data=idk_serializer.data, status=status.HTTP_201_CREATED)






# serializer = ProductsSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




    # if type == 0:
    #     serializer = PercentDiscountRewardViewSerializer(data=request.data)

    #     if serializer.is_valid():

    #         rewardentry = Rewards(
    #             points=serializer.validated_data.get('points'),
    #             end=serializer.validated_data.get('end'),
    #             title=serializer.validated_data.get('title'),
    #             image=serializer.validated_data.get('image'),
    #             description=serializer.validated_data.get('description')
    #         )
    #         rewardentry.save()

    #         percententry = Percentdiscountreward(
    #             pk=Rewards.objects.latest('reward_id').reward_id,
    #             product_id=Products.objects.get('product_id').product_id,
    #             percent=serializer.validated_data.get('percent')
    #         )
    #         percententry.save()

    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # elif type == 1:
    #     serializer = PriceDiscountRewardViewSerializer(data=request.data)

    #     if serializer.is_valid():

    #         rewardentry = Rewards(
    #             points=serializer.validated_data.get('points'),
    #             end=serializer.validated_data.get('end'),
    #             title=serializer.validated_data.get('title'),
    #             image=serializer.validated_data.get('image'),
    #             description=serializer.validated_data.get('description')
    #         )
    #         rewardentry.save()

    #         priceentry = Pricediscountreward(
    #             pk=Rewards.objects.latest('reward_id').reward_id,
    #             product_id=Products.objects.get('product_id').product_id,
    #             price=serializer.validated_data.get('price')
    #         )
    #         priceentry.save()

    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # elif type == 2:
    #     rewardserializer = RewardsSerializer(data=request.data)
    #     if not rewardserializer.is_valid():
    #         return Response(rewardserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #     reward = Rewards(
    #         points=rewardserializer.validated_data.get('points'),
    #         end=rewardserializer.validated_data.get('end'),
    #         title=rewardserializer.validated_data.get('title'),
    #         image=rewardserializer.validated_data.get('image'),
    #         description=rewardserializer.validated_data.get('description')
    #     )
    #     reward.save()

    #     rewardpk=Rewards.objects.latest('reward_id').reward_id
    #     prevfk=request.data['prevproduct_id']
    #     nextfk=request.data['nextproduct_id']
    #     upgrade = Productupgradereward(
    #         pk=rewardpk,
    #         prevproduct_id=Products.objects.get(pk=prevfk).product_id,
    #         nextproduct_id=Products.objects.get(pk=nextfk).product_id
    #     )
    #     upgrade.save()

    #     upgradeview = Productupgraderewardview.objects.get(pk=rewardpk)
    #     serializer = ProductUpgradeRewardViewSerializer(upgradeview)

    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


    # elif type == 3:
    #     rewardserializer = RewardsSerializer(data=request.data)
    #     if not rewardserializer.is_valid():
    #         return Response(rewardserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #     reward = Rewards(
    #         points=rewardserializer.validated_data.get('points'),
    #         end=rewardserializer.validated_data.get('end'),
    #         title=rewardserializer.validated_data.get('title'),
    #         image=rewardserializer.validated_data.get('image'),
    #         description=rewardserializer.validated_data.get('description')
    #     )
    #     reward.save()

    #     rewardpk=Rewards.objects.latest('reward_id').reward_id
    #     exclusive = Exclusiveproductreward(
    #         pk=rewardpk,
    #         product_id=request.data['product_id']
    #     )
    #     exclusive.save()

    #     exclusiveview = Exclusiveproductrewardview.objects.get(pk=rewardpk)
    #     serializer = ExclusiveProductRewardViewSerializer(exclusiveview)

    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # else:
    #     return Response(status=status.HTTP_400_BAD_REQUEST) 

# Get / Update a specific reward
# Make sure to update the discount/upgrade/exclusive table
@api_view(['GET', 'PUT'])
def specific_reward(request, pk):
     # Fetch the data of the reward using the primary key
    try:
        reward = Rewards.objects.get(pk=pk)
    except Rewards.DoesNotExist:
        return Response(status=status.HTTP_404_BAD_REQUEST)
    
    # Get the specified user
    if request.method == 'GET':
        serializer = RewardsSerializer(reward)

        reward_exist = False

        domain = request.get_host()
        appname = 'lprs'
        requestpath = lambda reward_type : "http://" + domain + "/" + appname + "/" + reward_type + "/get-all/"

        response = requests.get(requestpath('percentdisccountrewards'))
        if (response.status_code == 200):
            data = json.loads(response.text)

            for entry in data:
                if entry["reward_id"] == pk:
                    return entry

                









        # response = requests.get(requestpath('pricedisccountrewards'))
        # response = requests.get(requestpath('productupgraderewards'))
        # response = requests.get(requestpath('exclusiveupgraderewards'))


        # print(response.text)
        # print("Response: ", response.status_code) # Code 200

        
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