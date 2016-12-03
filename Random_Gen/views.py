from django.shortcuts import render
# from django.shortcuts import *
from Random_Gen.models import *
from django.db import models
from .models import TreasureItemsBaseResults
from .models import *
from random import randint
from random import choice

coins = TreasureCoinsBaseValue
goods = TreasureGoodsBaseValue
items = TreasureItemsBaseResults
base_results = [coins, goods, items]


def treasure_result(request):
    if request.method == 'POST':
        encounter_level = request.POST.get('enc_level', 1)
    else:
        encounter_level = 1
    coinsval = ''
    goodsval = ''
    itemsval = ''
    for index in range(0, len(base_results)):
        #
        random_percentage = d100()

        if index == 0:
            coin = get_model(random_percentage, encounter_level, coins)
            if coin==None:
                coinsval = 0
            else:
                coinsval = (get_coin_result(coin))

        if index == 1:
            good = get_model(random_percentage, encounter_level, goods)
            if good==None:
                goodsval=0
            else:
                goodsval = (get_goods_result(good))

        if index == 2:
            item = get_model(random_percentage, encounter_level, items)
            if item == None:
                itemsval ='None'
            else:
                itemsval = (get_item_result(item))

        # all three are packed into a dictionary and sent to the html page to be displayed, maybe with a title.

    return render(request, 'treasure_result.html',{'treasure': {'coins':coinsval, 'goods':goodsval, 'items':itemsval} } )


def get_model(random_percentage, encounter_level, model):
    for result in model.objects.filter(level=encounter_level).values():

        if result['percent_lower'] <= random_percentage <= result['percent_upper']:
            return result


# for the goods same first step, different second step, instead just see what string is there 'art' or 'gem'
def get_goods_result(good):
    good_type = good['goods_type']
    if good_type=='gem':
        print('GEMS!!!!')
        result = get_gems(good['die_size'], good['number_of_die'])
        return result
    elif good_type == 'art':
        result = get_art_collection(good['die_size'], good['number_of_die'])
        return result
    else:
        good_type = 'None' if good_type == 'N/A' else good_type
        return good_type


# '''These three methods are to simplify somewhat the creation of a number of items'''
def d100():
    roll=randint(1,101)
    return roll


def roll_several_die(die_size, die_num):
    total=0
    for num in range(die_num):
        total+=randint(1, die_size+1)
    return total


def find_value(die_size, die_num, multi):
    die_results=roll_several_die(die_size,die_num)
    die_results*=multi
    return die_results


# These two methods determine gem type and value
def get_gems(die_size,num_die):
    number_of_gems=roll_several_die(die_size,num_die)
    gem_dict={'gems':[]}
    for num in range(number_of_gems):
        gem = get_gem()
        gem_dict['gems'].append(gem)
    return gem_dict


def get_gem():
    dice_roll=d100()
    gem={'name':'','value':0}
    gems=Gems.objects.all()
    for results in gems:
        if dice_roll >=results.percent_lower and dice_roll<=results.percent_upper:
            all_gem_names=results.gem_name.split(',')
            gem['name'] = choice(all_gem_names)
            gem['value'] = find_value(results.value_dice_size, results.value_dice_number, results.value_multiplier)
    print(gem)
    return gem


# These two methods determine art value and type
def get_art_collection(die_size, num_die):
    number_of_art=roll_several_die(die_size,num_die)
    art_dict={'art':[]}
    for num in range(number_of_art):
        art = get_art()
        art_dict['art'].append(art)
    return art_dict


def get_art():
    dice_roll=d100()
    art={'name':'','value':0}
    arts=Art.objects.all()
    for results in arts:
        if dice_roll >=results.percent_lower and dice_roll<=results.percent_upper:
            all_art_names=results.art_name.split(',')
            art['name'] = choice(all_art_names)
            art['value'] = find_value(results.value_dice_size, results.value_dice_number, results.value_multiplier)
    print(art)
    return art



def get_item_result(item, item_type=''):
    if item != None:
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
    if item == None:
        item_type = 'None'

    return item_type
# def get_mundane_items():
#

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
    if result == 0:
        coin_type='None'
        coins_total = 'No Coins'
    else:
        coins_total = str(result)+" "+coin_type
    return coins_total


def base(request):
    title = {'title': 'Welcome to the Treasure Generator!'}
    return render(request, 'base.html', title)
