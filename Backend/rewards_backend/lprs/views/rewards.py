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
    
    request_data = request.data
    reward_serializer = RewardsSerializer(data=request_data)
    if not reward_serializer.is_valid():
        return Response(reward_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    r_id = Rewards.objects.latest('reward_id').reward_id

    if(type == 0):
        
        # Create percent discount reward entry
        request_data["reward"] = r_id
        request_data["product"] = request_data["product_id"]
        request_data["percent"] = request_data["discountpercent"]

        percent = PercentDiscountRewardSerializer(data=request_data)
        if not percent.is_valid():
            return Response(percent.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_201_CREATED)

    elif(type == 1):
        
        # Create price discount reward entry
        request_data["reward"] = r_id
        request_data["product"] = request_data["product_id"]
        request_data["price"] = request_data["discountprice"]

        price = PriceDiscountRewardSerializer(data=request.data)
        if not price.is_valid():
            return Response(price.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_201_CREATED)
    
    elif(type == 2):
        
        # Create product upgrade reward entry
        request_data["reward"] = r_id
        request_data["prevproduct"] = request_data["prev_product_id"]
        request_data["nextproduct"] = request_data["next_product_id"]

        upgrade = ProductUpgradeRewardSerializer(data=request.data)
        if not upgrade.is_valid():
            return Response(upgrade.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_201_CREATED)
    
    elif(type == 3):
        
        # Create product upgrade reward entry
        request_data["reward"] = r_id
        request_data["product"] = request_data["product_id"]

        exclusive = ExclusiveProductRewardSerializer(data=request.data)
        if not exclusive.is_valid():
            return Response(exclusive.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(status=status.HTTP_201_CREATED)

# Get / Update a specific reward
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
    
        # Fetch reward serializer data
        reward_serializer = RewardsSerializer(reward)
        
        # Edit Reward Keys - Avoid Duplications in Join Operator
        reward_json = reward_serializer.data

        if(reward_json.get("reward")):
            reward_json["reward_id"] = reward_json.pop("reward")
        if(reward_json.get("title")):
            reward_json["rewardname"] = reward_json.pop("title")
        reward_json["rewardimage"] = reward_json.pop("image")
        reward_json["rewarddescription"] = reward_json.pop("description")

        if(Percentdiscountreward.objects.filter(pk=pk).exists()):
            # Fetch price reward serializer data
            percent_discount = Percentdiscountreward.objects.get(pk=pk)
            percent_serializer = PercentDiscountRewardSerializer(percent_discount)
            
            # Change key names in JSON for clear description
            percent_json = percent_serializer.data
            percent_json.pop("reward")
            percent_json["product_id"] = percent_json.pop("product")
            percent_json["discountpercent"] = percent_json.pop("percent")

            # Edit Product Keys - Avoid Duplications in Join Operator
            product = Products.objects.get(pk=percent_json['product_id'])
            products_serializer = ProductsSerializer(product)
            product_json = products_serializer.data

            product_json.pop("product_id")
            product_json["productprice"] = product_json.pop("price")
            product_json["productimage"] = product_json.pop("image")
            product_json["productdescription"] = product_json.pop("description")

            # Join Reward and Product to Percent Entry
            percent_json.update(reward_json.copy())
            percent_json.update(product_json.copy())
            return Response(percent_json)

        elif(Pricediscountreward.objects.filter(pk=pk).exists()):
            price_discount = Pricediscountreward.objects.get(pk=pk)
            price_serializer = PriceDiscountRewardSerializer(price_discount)

            # Change key names in JSON for clear description
            price_json = price_serializer.data
            price_json.pop("reward")
            price_json["product_id"] = price_json.pop("product")
            price_json["discountprice"] = price_json.pop("price")

            # Edit Product Keys - Avoid Duplications in Join Operator
            product = Products.objects.get(pk=price_json['product_id'])
            products_serializer = ProductsSerializer(product)
            product_json = products_serializer.data

            product_json.pop("product_id")
            product_json["productprice"] = product_json.pop("price")
            product_json["productimage"] = product_json.pop("image")
            product_json["productdescription"] = product_json.pop("description")

            # Join Reward and Product to Price Entry
            price_json.update(reward_json.copy())
            price_json.update(product_json.copy())
            return Response(price_json)
        
        elif(Productupgradereward.objects.filter(pk=pk).exists()):
            product_upgrade = Productupgradereward.objects.get(pk=pk)
            upgrade_serializer = ProductUpgradeRewardSerializer(product_upgrade)
            upgrade_json = upgrade_serializer.data
            upgrade_json.pop("reward")
            upgrade_json["prev_product_id"] = upgrade_json.pop("prevproduct")
            upgrade_json["next_product_id"] = upgrade_json.pop("nextproduct")

            # Edit Previous Product Keys - Avoid Duplications in Join Operator
            prev_product = Products.objects.get(pk=upgrade_json['prev_product_id'])
            prev_product_serializer = ProductsSerializer(prev_product)
            prev_product_json = prev_product_serializer.data

            prev_product_json.pop("product_id")
            prev_product_json["prevproductprice"] = prev_product_json.pop("price")
            prev_product_json["prevproductimage"] = prev_product_json.pop("image")
            prev_product_json["prevproductdescription"] = prev_product_json.pop("description")

            # Edit Next Product Keys - Avoid Duplications in Join Operator
            next_product = Products.objects.get(pk=upgrade_json['next_product_id'])
            next_products_serializer = ProductsSerializer(next_product)
            next_product_json = next_products_serializer.data

            next_product_json.pop("product_id")
            next_product_json["nextproductprice"] = next_product_json.pop("price")
            next_product_json["nextproductimage"] = next_product_json.pop("image")
            next_product_json["nextproductdescription"] = next_product_json.pop("description")

            # Join Reward and Product to Upgrade Entry
            upgrade_json.update(reward_json.copy())
            upgrade_json.update(prev_product_json.copy())
            upgrade_json.update(next_product_json.copy())

            return Response(upgrade_json)
        
        elif(Exclusiveproductreward.objects.filter(pk=pk).exists()):
            exclusive = Exclusiveproductreward.objects.get(pk=pk)
            exclusive_serializer = ExclusiveProductRewardSerializer(exclusive)
            exclusive_json = exclusive_serializer.data
        
            exclusive_json["reward_id"] = exclusive_json.pop("reward")
            exclusive_json["product_id"] = exclusive_json.pop("product")

            # Edit Product Keys - Avoid Duplications in Join Operator
            product = Products.objects.get(pk=exclusive_json['product_id'])
            products_serializer = ProductsSerializer(product)
            product_json = products_serializer.data

            product_json.pop("product_id")
            product_json["productprice"] = product_json.pop("price")
            product_json["productimage"] = product_json.pop("image")
            product_json["productdescription"] = product_json.pop("description")

            # Join Reward and Product to Exclusive Entry
            exclusive_json.update(reward_json.copy())
            exclusive_json.update(product_json.copy())

            return Response(exclusive_json)
        
        return Response(reward_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    #Update details of the specified reward
    elif request.method == 'PUT':
        request_data = request.data

        getRewards_serializer = RewardsSerializer(reward)
        reward_json = getRewards_serializer.data

        reward_json['reward'] = request_data['reward_id']
        reward_json['title'] = request_data.pop('rewardname')
        reward_json['image'] = request_data.pop('rewardimage')
        reward_json['description'] = request_data.pop('rewarddescription')

        rewards_serializer = RewardsSerializer(reward, data=reward_json)
        if rewards_serializer.is_valid():
            rewards_serializer.save()
        else:
            return Response(rewards_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        if(Pricediscountreward.objects.filter(pk=pk).exists()):
            price_discount = Pricediscountreward.objects.get(pk=pk)
            getPrice_serializer = PriceDiscountRewardSerializer(price_discount)
            price_json = getPrice_serializer.data
            
            price_json['reward'] = request_data.pop('reward_id')
            price_json["product"] = request_data.pop("product_id")
            price_json["price"] = request_data.pop("discountprice")

            price_serializer = PriceDiscountRewardSerializer(price_discount, data=price_json)
            if price_serializer.is_valid():
                price_serializer.save()
                return Response(price_serializer.data)
        elif(Percentdiscountreward.objects.filter(pk=pk).exists()):
            percent_discount = Percentdiscountreward.objects.get(pk=pk)
            getPercent_serializer = PercentDiscountRewardSerializer(percent_discount)
            percent_json = getPercent_serializer.data

            percent_json['reward'] = request_data.pop('reward_id')
            percent_json["product"] = request_data.pop("product_id")
            percent_json['percent'] = request_data.pop("discountpercent")

            percent_serializer = PercentDiscountRewardSerializer(percent_discount, data=percent_json)
            if percent_serializer.is_valid():
                percent_serializer.save()
                return Response(percent_serializer.data)
        elif(Productupgradereward.objects.filter(pk=pk).exists()):
            product_upgrade = Productupgradereward.objects.get(pk=pk)
            getUpgrade_serializer = ProductUpgradeRewardSerializer(product_upgrade)
            upgrade_json = getUpgrade_serializer.data

            upgrade_json['reward'] = request_data.pop('reward_id')
            upgrade_json["prevproduct"] = request_data["prev_product_id"]
            upgrade_json["nextproduct"] = request_data["next_product_id"]

            upgrade_serializer = ProductUpgradeRewardSerializer(product_upgrade, data=upgrade_json)
            if upgrade_serializer.is_valid():
                upgrade_serializer.save()
                return Response(upgrade_serializer.data)
        elif(Exclusiveproductreward.objects.filter(pk=pk).exists()):
            exclusive = Exclusiveproductreward.objects.get(pk=pk)
            getExclusive_serializer = ExclusiveProductRewardSerializer(exclusive)
            exclusive_json = getExclusive_serializer.data

            exclusive_json['reward'] = request_data.pop('reward_id')
            exclusive_json["product"] = request_data.pop("product_id")

            exclusive_serializer = ExclusiveProductRewardSerializer(exclusive, data=exclusive_json)
            if exclusive_serializer.is_valid():
                exclusive_serializer.save()
                return Response(exclusive_serializer.data)
        return Response(rewards_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete the user
    elif request.method == 'DELETE':
        reward.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    