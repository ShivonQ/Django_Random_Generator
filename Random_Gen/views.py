from django.shortcuts import render
# from django.shortcuts import *
# import pdb
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

    # result = {'result': []}
    # second_list = []
    for index in range(1, len(base_results)):
        #
        random_percentage = randint(1, 100)

        if index == 0:
            coin = get_model(random_percentage, encounter_level, coins)
            get_coin_result(coin)

        if index == 1:

            get_goods_result()

        if index == 2:
            item = get_model(random_percentage, encounter_level, items)
            item = get_item_result(item)

        # for model.coins take die size and number of die, for each number in number_of_die:randint(1,die_size)
        # add the die rolls together and multiply them by the multiplier
        # add on the coin_type, pack into a dictionary

        # for the goods same first step, different second step, instead just see what string is there 'art' or 'gem'

        # for the items one, same first step, then check for the 'True' value in the 4 booleans.
        # Depending on which is True make that the item type

        # all three are packed into a dictionary and sent to the html page to be displayed, maybe with a title.

    # model.objects

    # result['result'].append(get_item_result(dice_roll, encounter_level))
    # these_models = model.objects.filter(level=encounter_level).values()
    #
    # for thing in these_models:
    #     p_up = thing['percent_upper']
    #     p_dn = thing['percent_lower']
    #     if p_dn <= dice_roll <= p_up:
    #         result['result'].append(thing)
    #         # print(these_models)
    # # result.append(these_models)

    return render(request, 'treasure_result.html', {"item": item})


def get_model(random_percentage, encounter_level, model):
    for result in model.objects.filter(level=encounter_level).values():

        if result['percent_lower'] <= random_percentage <= result['percent_upper']:
            return result


def get_goods_result():
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


def get_coin_result(coin):
    # possible_coin_rows = items.objects.filter(level=encounter_level).values()
    # selected_coin = None
    # #
    # for coin in coins.objects.filter(level=encounter_level).values():
    #     #
    #     if coin['percent_lower'] <= percentage <= coin['percent_upper']:
    #         selected_coin = coin
    #         # item_id = item['id']

    number_of_die = coin['number_of_die']
    die_size = coin['die_size']
    multiplier = coin['multiplier']

    # for each dice in die, randint(1, die_size)
    roll_total = 0
    for dice in range(1, number_of_die):
        dice_roll = randint(1, die_size)
        # add the die rolls together
        roll_total += dice_roll

    # multiply them by the multiplier
    result = roll_total * multiplier


def base(request):
    title = {'title': 'Welcome to the Treasure Generator!'}
    return render(request, 'base.html', title)
