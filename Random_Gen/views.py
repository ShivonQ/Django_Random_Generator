from django.shortcuts import render
# from django.shortcuts import *
from Random_Gen.models import *
from django.db import models
from .models import TreasureItemsBaseResults
from .models import *

coins = TreasureCoinsBaseValue
goods = TreasureGoodsBaseValue
items = TreasureItemsBaseResults
base_results = [coins, goods, items]


def treasure_result(request, item=''):
    if request.method == 'POST':
        encounter_level = request.POST.get('enc_level', 1)
    else:
        encounter_level = 1

    treasure = {'treasure': []}
    for index in range(1, len(base_results)):
        #
        random_percentage = randint(1, 100)

        if index == 0:
            coin = get_model(random_percentage, encounter_level, coins)
            get_coin_result(coin)

        if index == 1:
            good = get_model(random_percentage, encounter_level, goods)
            get_goods_result(good)

        if index == 2:
            item = get_model(random_percentage, encounter_level, items)
            item = get_item_result(item)

        # all three are packed into a dictionary and sent to the html page to be displayed, maybe with a title.

    return render(request, 'treasure_result.html', {"item": item})


def get_model(random_percentage, encounter_level, model):
    for result in model.objects.filter(level=encounter_level).values():

        if result['percent_lower'] <= random_percentage <= result['percent_upper']:
            return result


# for the goods same first step, different second step, instead just see what string is there 'art' or 'gem'
def get_goods_result(good):
    pass


def get_item_result(item, item_type=''):

    item_types = {'mundane item': item['items_type_mundane'],
                  'minor item': item['items_type_minor'],
                  'medium item': item['items_type_medium'],
                  'major item': item['items_type_major']}

    for key, boolean in item_types.items():
        if boolean:
            item_type = key
            return item_type
        else:
            continue

    return {'item_type': item_type}


# for model.coins take die size and number of die, for each number in number_of_die:randint(1,die_size)
# add the die rolls together and multiply them by the multiplier
# add on the coin_type, pack into a dictionary
def get_coin_result(coin):
    number_of_die = coin['number_of_die']
    die_size = coin['die_size']
    multiplier = coin['multiplier']
    coin_type = coin['coins_type']

    # for each dice in die, randint(1, die_size)
    roll_total = 0
    for dice in range(1, number_of_die):
        dice_roll = randint(1, die_size)
        # add the die rolls together
        roll_total += dice_roll

    # multiply them by the multiplier
    result = roll_total * multiplier
    coins_type = str(result).join(coin_type)
    return {'coin_type': coins_type}


def base(request):
    title = {'title': 'Welcome to the Treasure Generator!'}
    return render(request, 'base.html', title)
