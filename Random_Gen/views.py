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


def treasure_gen(request):

    return render(request,'treasure_gen.html')

def treasure_result(request):
    if request.method == 'POST':
        print(request)
        encounter_level = request.POST.get('enc_level', 1)
        noCoins = request.POST.get('noCoins')
        print(noCoins)
        noGems = request.POST.get('noGems')
        print(noGems)
        noArt = request.POST.get('noArt')
        print(noArt)
        noItems = request.POST.get('noItems')
        print(noItems)
    else:
        encounter_level = 1
    coinsval = ''
    goodsval = ''
    itemsval = ''
    for index in range(0, len(base_results)):
        #
        random_percentage = d100()

        if index == 0 and noCoins == None:
            coin = get_model(random_percentage, encounter_level, coins)
            if coin == None:
                coinsval = 0
            else:
                coinsval = (get_coin_result(coin))

        if index == 1:
            good = get_model(random_percentage, encounter_level, goods)
            if good == None:
                goodsval = 0
            else:
                goodsval = (get_goods_result(good))

        if index == 2 and noItems == None:
            item = get_model(random_percentage, encounter_level, items)
            if item == None:
                itemsval = 'None'
            else:
                itemsval = (get_item_result(item))

                # all three are packed into a dictionary and sent to the html page to be displayed, maybe with a title.
        result = {'treasure': {'coins': coinsval, 'goods': goodsval, 'items': itemsval}}
        print(result)
    return render(request, 'treasure_result.html', result)


def get_model(random_percentage, encounter_level, model):
    for result in model.objects.filter(level=encounter_level).values():

        if result['percent_lower'] <= random_percentage <= result['percent_upper']:
            return result


# for the goods same first step, different second step, instead just see what string is there 'art' or 'gem'
def get_goods_result(good):
    good_type = good['goods_type']
    if good_type == 'gem':
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
    roll = randint(1, 101)
    return roll


def d20():
    roll = randint(1, 21)
    return roll


def roll_several_die(die_size, die_num):
    total = 0
    for num in range(die_num):
        total += randint(1, die_size + 1)
    return total


def find_value(die_size, die_num, multi):
    die_results = roll_several_die(die_size, die_num)
    die_results *= multi
    return die_results


# These two methods determine gem type and value
def get_gems(die_size, num_die):
    number_of_gems = roll_several_die(die_size, num_die)
    gem_dict = {'gems': []}
    for num in range(number_of_gems):
        gem = get_gem()
        gem_dict['gems'].append(gem)
    print(gem_dict)
    return gem_dict


def get_gem():
    dice_roll = d100()
    gem = {'name': '', 'value': 0}
    gems = Gems.objects.all()
    for results in gems:
        if dice_roll >= results.percent_lower and dice_roll <= results.percent_upper:
            all_gem_names = results.gem_name.split(',')
            gem['name'] = choice(all_gem_names)
            gem['value'] = find_value(results.value_dice_size, results.value_dice_number, results.value_multiplier)
    print(gem)
    return gem


# These two methods determine art value and type
def get_art_collection(die_size, num_die):
    number_of_art = roll_several_die(die_size, num_die)
    art_dict = {'art': []}
    for num in range(number_of_art):
        art = get_art()
        art_dict['art'].append(art)
    print(art_dict)
    return art_dict


def get_art():
    dice_roll = d100()
    art = {'name': '', 'value': 0}
    arts = Art.objects.all()
    for results in arts:
        if dice_roll >= results.percent_lower and dice_roll <= results.percent_upper:
            all_art_names = results.art_name.split(',')
            art['name'] = choice(all_art_names)
            art['value'] = find_value(results.value_dice_size, results.value_dice_number, results.value_multiplier)
    print(art)
    return art


def get_item_result(item, item_type=''):
    if item != None:
        if item['items_type_mundane']:
            mund_items = get_mundane_items(item['die_size'], item['number_of_die'])
            print(mund_items,'----------> this came from get_item_result()')
            return mund_items
        elif item['items_type_minor']:
            minor_items = get_items(item['die_size'], item['number_of_die'], 0)
            print(minor_items,'----------> this came from get_item_result()')
            return minor_items
        elif item['items_type_medium']:
            medium_items = get_items(item['die_size'], item['number_of_die'], 1)
            print(medium_items,'----------> this came from get_item_result()')
            return medium_items
        elif item['items_type_major']:
            major_items = get_items(item['die_size'], item['number_of_die'],2)
            print(major_items,'----------> this came from get_item_result()')
            return major_items
        # else:
        #     # TODO: other 3 item types
        #     item_types = {'mundane item': item['items_type_mundane'],
        #                   'minor item': item['items_type_minor'],
        #                   'medium item': item['items_type_medium'],
        #                   'major item': item['items_type_major']}
        #
        #     for key, boolean in item_types.items():
        #         if boolean:
        #             item_type = key
        #             return item_type
        #         else:
        #             continue
    if item == None:
        item_type = 'None'

    return item_type


def roll_root_magic_item_table(minMedMaj):
    if minMedMaj == 0:
        # todo: ##############################################################################
        # dice_roll=3
        dice_roll = d100()
        mins = RootMagicItemsTable.objects.all()
        for record in mins:
            if record.minor_percent_chance_lower <= dice_roll <= record.minor_percent_chance_upper:
                print('minor item')
                print(record)
                #             TODO: sort out how to have it figure out which magic item table to call next
                if record.name == 'Armor and Shields':
                    result = {'A_o_S':[]}
                    result['A_o_S'].append(get_armor_and_shields(minMedMaj))
                    return result
                elif record.name == 'Potions':
                    result = {'pots': []}
                    result['pots'].append(get_potions(minMedMaj))
                    return result
                elif record.name == 'Rings':
                    result = {'rings':[]}
                    result['rings'].append(get_ring(minMedMaj))
                    return result
                elif record.name == 'Wands':
                    result = {'wands':[]}
                    result['wands'].append(get_wand(minMedMaj))
                    return result
                elif record.name == 'Wondrous Items':
                    result = {'wondrous':[]}
                    result = get_wondrous_items(minMedMaj)
                    return result
                else:

                    return record.name
    elif minMedMaj == 1:
        print('medium table')
        dice_roll = d100()
        mins = RootMagicItemsTable.objects.all()
        for record in mins:
            if record.medium_percent_chance_lower <= dice_roll <= record.medium_percent_chance_upper:
                print('medium item')
                print(record)
                #             TODO: sort out how to have it figure out which magic item table to call next
                if record.name == 'Armor and Shields':
                    result = {'A_o_S': []}
                    result['A_o_S'].append(get_armor_and_shields(minMedMaj))
                    return result
                elif record.name == 'Potions':
                    result = {'pots': []}
                    result['pots'].append(get_potions(minMedMaj))
                    return result
                elif record.name == 'Rings':
                    result = {'rings': []}
                    result['rings'].append(get_ring(minMedMaj))
                    return result
                elif record.name == 'Wands':
                    result = {'wands': []}
                    result['wands'].append(get_wand(minMedMaj))
                    return result
                elif record.name == 'Wondrous Items':
                    result = {'wondrous': []}
                    result = get_wondrous_items(minMedMaj)
                    return result
                elif record.name == 'Staffs':
                    result = {'staff':[]}
                    result['staff'].append(get_staff(minMedMaj))
                    return result
                elif record.name == 'Rods':
                    result = {'rods':[]}
                    result['rods'].append(get_rod(minMedMaj))
                    return result
                else:# TODO: CREATE ROD STUFF
                    return record.name
    else:
        print('major table')
        dice_roll = d100()
        mins = RootMagicItemsTable.objects.all()
        for record in mins:
            if record.major_percent_chance_lower <= dice_roll <= record.major_percent_chance_upper:
                print('major item')
                print(record)
                #             TODO: sort out how to have it figure out which magic item table to call next
                if record.name == 'Armor and Shields':
                    result = {'A_o_S': []}
                    result['A_o_S'].append(get_armor_and_shields(minMedMaj))
                    return result
                elif record.name == 'Potions':
                    result = {'pots': []}
                    result['pots'].append(get_potions(minMedMaj))
                    return result
                elif record.name == 'Rings':
                    result = {'rings': []}
                    result['rings'].append(get_ring(minMedMaj))
                    return result
                elif record.name == 'Wands':
                    result = {'wands': []}
                    result['wands'].append(get_wand(minMedMaj))
                    return result
                elif record.name == 'Wondrous Items':
                    result = {'wondrous': []}
                    result = get_wondrous_items(minMedMaj)
                    return result
                elif record.name == 'Staffs':
                    result = {'staff':[]}
                    result['staff'].append(get_staff(minMedMaj))
                    return result
                elif record.name == 'Rods':
                    result = {'rods':[]}
                    result['rods'].append(get_rod(minMedMaj))
                    return result
                else:
                    return record.name
    print('magic items!')



# TODO: Staves stuff

def get_wand(minMedMaj):
    print('wands')
    d_r = d100()
    wand = {'name':'','value':0}
    if minMedMaj == 0:
        print('min wand')
        wands = Wand.objects.all()
        for a_wand in wands:
            if a_wand.minor_percent_chance_lower <= d_r <= a_wand.minor_percent_chance_upper:
                wand['name'] = a_wand.name
                wand['value'] = a_wand.cost
                return wand
    elif minMedMaj == 1:
        print('med wand')
        wands = Wand.objects.all()
        for a_wand in wands:
            if a_wand.medium_percent_chance_lower <= d_r <= a_wand.medium_percent_chance_upper:
                wand['name'] = a_wand.name
                wand['value'] = a_wand.cost
                return wand
    else:
        print('maj wand')
        wands = Wand.objects.all()
        for a_wand in wands:
            if a_wand.major_percent_chance_lower <= d_r <= a_wand.major_percent_chance_upper:
                wand['name'] = a_wand.name
                wand['value'] = a_wand.cost
                return wand

def get_staff(minMedMaj):
    print('staffs')
    d_r = d100()
    staff = {'name':'','value':0}
    if minMedMaj == 0:
        return None
    elif minMedMaj == 1:
        print('medium')
        staffs = Staff.objects.all()
        for a_staff in staffs:
            if a_staff.medium_percent_chance_lower <= d_r <= a_staff.medium_percent_chance_upper:
                staff['name'] = a_staff.name
                staff['value'] = a_staff.cost
                return staff
    else:
        print('major')
        staffs = Staff.objects.all()
        for a_staff in staffs:
            if a_staff.major_percent_chance_lower <= d_r <= a_staff.major_percent_chance_upper:
                staff['name'] = a_staff.name
                staff['value'] = a_staff.cost
                return staff


def get_rod(minMedMaj):
    print('rods')
    d_r = d100()
    rod = {'name':'','value':0}
    if minMedMaj == 0:
        return None
    elif minMedMaj == 1:
        print('medium')
        rods = Rod.objects.all()
        for a_rod in rods:
            if a_rod.medium_percent_chance_lower <= d_r <= a_rod.medium_percent_chance_upper:
                rod['name'] = a_rod.name
                rod['value'] = a_rod.cost
                return rod
    else:
        print('major')
        rods = Rod.objects.all()
        for a_rod in rods:
            if a_rod.major_percent_chance_lower <= d_r <= a_rod.major_percent_chance_upper:
                rod['name'] = a_rod.name
                rod['value'] = a_rod.cost
                return rod


def get_wondrous_items(minMedMaj):
    print('wondrous')
    d_r = d100()
    w_i = {'name':'', 'value':0}
    if minMedMaj==0:
        print('minor')
        record = MinorWondrousItem.objects.get(percent_chance=d_r)

        w_i['name'] = record.name
        w_i['value'] = record.cost
    elif minMedMaj==1:
        print('medium')
        record = MediumWondrousItem.objects.get(percent_chance=d_r)
        w_i['name'] = record.name
        w_i['value'] = record.cost
    else:
        print('major')
        record = MajorWondrousItem.objects.get(percent_chance=d_r)
        w_i['name'] = record.name
        w_i['value'] = record.cost

    return w_i


def get_potions(minMedMaj):
    print('potions')
    # Rollfor the % result
    d_r = d100()
    # structure you will return
    P_or_O = {'name':'','value':0,'isPotion': True}
    if minMedMaj == 0:
        # grab the elements and then find the one with the right
        potions = PotionOrOil.objects.all()
        for pot in potions:
            if pot.minor_percent_chance_lower <= d_r <= pot.minor_percent_chance_upper:
                P_or_O['name']=pot.name
                P_or_O['isPotion']=pot.isPotion
                P_or_O['value']=pot.cost
                return P_or_O
    elif minMedMaj == 1:
        potions = PotionOrOil.objects.all()
        for pot in potions:
            if pot.medium_percent_chance_lower <= d_r <= pot.medium_percent_chance_upper:
                P_or_O['name'] = pot.name
                P_or_O['isPotion'] = pot.isPotion
                P_or_O['value'] = pot.cost
                return P_or_O

    else:
        potions = PotionOrOil.objects.all()
        for pot in potions:
            if pot.major_percent_chance_lower <= d_r <= pot.major_percent_chance_upper:
                P_or_O['name'] = pot.name
                P_or_O['isPotion'] = pot.isPotion
                P_or_O['value'] = pot.cost
                return P_or_O


def get_ring(minMedMaj):
    print('rings')
    d_r = d100()
    result = {'name': '', 'cost': 0}
    if minMedMaj == 0:
        print('minor ring')
        rings = PotionOrOil.objects.all()
        for ring in rings:
            if ring.minor_percent_chance_lower <= d_r <= ring.minor_percent_chance_upper:
                result['name'] = ring.name
                result['isPotion'] = ring.isPotion
                result['value'] = ring.cost
                return result

    elif minMedMaj == 1:
        print('med ring')
        rings = PotionOrOil.objects.all()
        for ring in rings:
            if ring.medium_percent_chance_lower <= d_r <= ring.medium_percent_chance_upper:
                result['name'] = ring.name
                result['isPotion'] = ring.isPotion
                result['value'] = ring.cost
                return result

    else:
        print('maj ring')
        rings = PotionOrOil.objects.all()
        for ring in rings:
            if ring.major_percent_chance_lower <= d_r <= ring.major_percent_chance_upper:
                result['name'] = ring.name
                result['isPotion'] = ring.isPotion
                result['value'] = ring.cost
                return result


def get_items(die_size, num_die, minMedMaj):
    number_of_items = roll_several_die(die_size, num_die)
    item_dict = {'items': []}
    for num in range(number_of_items):
        item = roll_root_magic_item_table(minMedMaj)
        item_dict['items'].append(item)
    return item_dict


def get_armor_and_shields(minMedMaj):
    item = {'name': '', 'type': ''}
    if minMedMaj == 0:
        print('minor item')
        # TODO: ##############################################################################
        # dice_roll=93
        dice_roll = d100()
        mins = ArmorAndShields.objects.all()
        for record in mins:
            if record.minor_percent_chance_lower <= dice_roll <= record.minor_percent_chance_upper:
                #             TODO: specific armor and specific shield triggers go here too!
                if 90 <= dice_roll <= 91:
                    spec_shields = SpecificShield.objects.all()
                    d=d100()
                    for shield in spec_shields:
                        if shield.minor_percent_chance_lower <= d <= shield.minor_percent_chance_upper:
                            item['name'] = shield.name
                            item['type'] = 'Shield'
                            return item
                if 88 <= dice_roll <= 89:
                    spec_arm = SpecificArmor.objects.all()
                    d=d100()
                    for armor in spec_arm:
                        if armor.minor_percent_chance_lower<= d <= armor.minor_percent_chance_upper:
                            item['name'] = armor.name
                            item['type'] = 'Armor'
                            return item

                print(record)
                # if the record has a special ability then roll the die for Armor or shield again, then for speciali ability
                if 92 <= dice_roll <= 100:
                    dice_roll = d100()
                    while 92 <= dice_roll <= 100:
                        dice_roll = d100()
                    mins = ArmorAndShields.objects.all()
                    # if the item has abilities then enter the folllowing loop
                    for record_rep in mins:
                        if record_rep.minor_percent_chance_lower <= dice_roll <= record_rep.minor_percent_chance_upper:
                            item['name'] = record_rep.item
                            type = record_rep.item[3:]
                            if type == 'Shield':
                                item['type'] = get_armor_type(1)
                                abilities = get_minor_shield_special_abilities(d100())
                                while None in abilities:
                                    abilities = get_minor_shield_special_abilities(d100())
                                if len(abilities) > 1:
                                    item['name'] += ', ' + abilities[0]['ab_name'] + ', ' + abilities[1]['ab_name']
                                else:
                                    item['name'] += ', ' + abilities['ab_name']
                            elif type == 'Armor':
                                item['type'] = get_armor_type(0)
                                abilities = get_minor_armor_special_abilities(d100())
                                while None in abilities:
                                    abilities = get_minor_shield_special_abilities(d100())
                                if len(abilities) > 1:
                                    item['name'] += ', ' + abilities[0]['ab_name'] + ', ' + abilities[1]['ab_name']
                                elif len(abilities) == 1:
                                    item['name'] += ', ' + abilities['ab_name']
                                else:
                                    print('no length or something')
                            return item
                            #               otherwise carry on with that basic item
                # special ability roll again

                else:
                    item['name']=record.item
                    type = record.item[3:]
                    if type == 'Shield':
                        item['type'] = get_armor_type(1)

                    elif type == 'Armor':
                        item['type'] = get_armor_type(0)

                    return item
    elif minMedMaj == 1:
        print('medium table')
        dice_roll = d100()
        mins = ArmorAndShields.objects.all()
        for record in mins:
            if record.medium_percent_chance_lower <= dice_roll <= record.medium_percent_chance_upper:
                #             TODO: specific armor and specific shield triggers go here too!
                print(record)
                if 61 <= dice_roll <= 63:
                    spec_shields = SpecificShield.objects.all()
                    d = d100()
                    for shield in spec_shields:
                        if shield.medium_percent_chance_lower <= d <= shield.medium_percent_chance_upper:
                            item['name'] = shield.name
                            item['type'] = 'Shield'
                            return item
                if 58 <= dice_roll <= 60:
                    spec_arm = SpecificArmor.objects.all()
                    d = d100()
                    for armor in spec_arm:
                        if armor.medium_percent_chance_lower <= d <= armor.medium_percent_chance_upper:
                            item['name'] = armor.name
                            item['type'] = 'Armor'
                            return item
                # if the record has a special ability then roll the die for Armor or shield again, then for speciali ability
                if dice_roll >= 92 and dice_roll <= 100:
                    dice_roll = d100()
                    while dice_roll >= 92 and dice_roll <= 100:
                        dice_roll = d100()
                    mins = ArmorAndShields.objects.all()
                    # if the item has abilities then enter the folllowing loop
                    for record in mins:
                        if record.medium_percent_chance_lower <= dice_roll and record.medium_percent_chance_upper >= dice_roll:
                            item['name'] = record.item
                            type = record.item[3:]
                            if type == 'Shield':
                                item['type'] = get_armor_type(1)
                                abilities = get_medium_shield_special_abilities(d100())
                                if len(abilities) > 1:
                                    item['name'] += ', ' + abilities[0]['ab_name'] + ', ' + abilities[1]['ab_name']
                                else:
                                    item['name'] += ', ' + abilities['ab_name']
                            elif type == 'Armor':
                                item['type'] = get_armor_type(0)
                                abilities = get_medium_armor_special_abilities(d100())
                                if len(abilities) > 1:
                                    item['name'] += ', ' + abilities[0]['ab_name'] + ', ' + abilities[1]['ab_name']
                                else:
                                    item['name'] += ', ' + abilities[0]['ab_name']
                            return item
                            #               otherwise carry on with that basic item

                else:
                    item['name'] = record.item
                    type = record.item[3:]
                    if type == 'Shield':
                        item['type'] = get_armor_type(1)

                    elif type == 'Armor':
                        item['type'] = get_armor_type(0)

                    return item
    else:
        print('major table')
        dice_roll = d100()
        mins = ArmorAndShields.objects.all()
        for record in mins:
            if record.major_percent_chance_lower <= dice_roll <= record.major_percent_chance_upper:
                #             TODO: specific armor and specific shield triggers go here too!
                if 61 <= dice_roll <= 63:
                    spec_shields = SpecificShield.objects.all()
                    d = d100()
                    for shield in spec_shields:
                        if shield.major_percent_chance_lower <= d <= shield.major_percent_chance_upper:
                            item['name'] = shield.name
                            item['type'] = 'Shield'
                            return item
                if 58 <= dice_roll <= 60:
                    spec_arm = SpecificArmor.objects.all()
                    d = d100()
                    for armor in spec_arm:
                        if armor.major_percent_chance_lower <= d <= armor.major_percent_chance_upper:
                            item['name'] = armor.name
                            item['type'] = 'Armor'
                            return item
                print(record)
                # if the record has a special ability then roll the die for Armor or shield again, then for speciali ability
                if dice_roll >= 92 and dice_roll <= 100:
                    dice_roll = d100()
                    while dice_roll >= 92 and dice_roll <= 100:
                        dice_roll = d100()
                    mins = ArmorAndShields.objects.all()
                    # if the item has abilities then enter the folllowing loop
                    for record in mins:
                        if record.major_percent_chance_lower <= dice_roll and record.major_percent_chance_upper >= dice_roll:
                            item['name'] = record.item
                            type = record.item[3:]
                            if type == 'Shield':
                                item['type'] = get_armor_type(1)
                                abilities = get_major_shield_special_abilities(d100())
                                if len(abilities) > 1:
                                    item['name'] += ', ' + abilities[0]['ab_name'] + ', ' + abilities[1]['ab_name']
                                else:
                                    item['name'] += ', ' + abilities['ab_name']
                            elif type == 'Armor':
                                item['type'] = get_armor_type(0)
                                abilities = get_medium_armor_special_abilities(d100())
                                if len(abilities) > 1:
                                    item['name'] += ', ' + abilities[0]['ab_name'] + ', ' + abilities[1]['ab_name']
                                else:
                                    item['name'] += ', ' + abilities[0]['ab_name']
                            return item
                            #               otherwise carry on with that basic item

                else:
                    item['name'] = record.item
                    type = record.item[3:]
                    if type == 'Shield':
                        item['type'] = get_armor_type(1)

                    elif type == 'Armor':
                        item['type'] = get_armor_type(0)

                    return item


def get_armor_type(a_o_s):
    print('fetching armor or shield')
    all_armor_types = ArmorType.objects.all()
    type = ''
    if a_o_s == 0:
        print('Its armor')
        d = d100()
        while d >= 80:
            d = d100()
        for record in all_armor_types:
            if record.percent_chance_lower <= d <= record.percent_chance_upper:
                type = record.type
                return type
    elif a_o_s == 1:
        print('its a shield')
        d = d100()
        while d <= 81:
            d = d100()
        for record in all_armor_types:
            if record.percent_chance_lower <= d <= record.percent_chance_upper:
                type = record.type
                return type


def get_minor_armor_special_abilities(d_r):
    ab1 = {'ab_name': ''}

    abs = ArmorSpecialAbility.objects.all()
    # IF D_R IS 100, Roll Twice and return those
    if d_r == 100:
        ab2 = {'ab_name': ''}
        # make sure d_r can never be 100 in this section
        while d_r == 100:
            d_r = d100()
        ab1 = get_minor_armor_special_abilities(d_r)
        d_r = d100()
        # make sure d_r can never be 100 in this section
        while d_r == 100:
            d_r = d100()
        ab2 = get_minor_armor_special_abilities(d_r)

        return [ab1, ab2]
    for ability in abs:
        if ability.minor_percent_chance_lower <= d_r <= ability.minor_percent_chance_upper and d_r != 100:
            print('ability')
            ab1['ab_name'] = ability.item_ability
            return ab1


def get_medium_armor_special_abilities(d_r):
    ab1 = {'ab_name': ''}

    abs = ArmorSpecialAbility.objects.all()
    # IF D_R IS 100, Roll Twice and return those
    if d_r == 100:
        ab2 = {'ab_name': ''}
        # make sure d_r can never be 100 in this section
        while d_r == 100:
            d_r = d100()
        ab1 = get_medium_armor_special_abilities(d_r)
        d_r = d100()
        # make sure d_r can never be 100 in this section
        while d_r == 100:
            d_r = d100()
        ab2 = get_medium_armor_special_abilities(d_r)

        return [ab1, ab2]
    for ability in abs:
        if ability.medium_percent_chance_lower <= d_r <= ability.medium_percent_chance_upper and d_r != 100:
            print('ability')
            ab1['ab_name'] = ability.item_ability
            return ab1


def get_major_armor_special_abilities(d_r):
    ab1 = {'ab_name': ''}

    abs = ArmorSpecialAbility.objects.all()
    # IF D_R IS 100, Roll Twice and return those
    if d_r == 100:
        ab2 = {'ab_name': ''}
        # make sure d_r can never be 100 in this section
        while d_r == 100:
            d_r = d100()
        ab1 = get_major_armor_special_abilities(d_r)
        d_r = d100()
        # make sure d_r can never be 100 in this section
        while d_r == 100:
            d_r = d100()
        ab2 = get_major_armor_special_abilities(d_r)

        return [ab1, ab2]
    for ability in abs:
        if ability.major_percent_chance_lower <= d_r <= ability.major_percent_chance_upper and d_r != 100:
            print('ability')
            ab1['ab_name'] = ability.item_ability
            return ab1


def get_minor_shield_special_abilities(d_r):
    ab1 = {'ab_name': ''}

    abs = ShieldSpecialAbility.objects.all()
    # IF D_R IS 100, Roll Twice and return those
    if d_r == 100:
        ab2 = {'ab_name': ''}
        # make sure d_r can never be 100 in this section
        while d_r == 100:
            d_r = d100()
        ab1 = get_minor_shield_special_abilities(d_r)
        d_r = d100()
        # make sure d_r can never be 100 in this section
        while d_r == 100:
            d_r = d100()
        ab2 = get_minor_shield_special_abilities(d_r)

        return [ab1, ab2]
    for ability in abs:
        if ability.minor_percent_chance_lower <= d_r and ability.minor_percent_chance_upper >= d_r and d_r != 100:
            print('ability')
            ab1['ab_name'] = ability.item_ability
            return ab1


def get_medium_shield_special_abilities(d_r):
    ab1 = {'ab_name': ''}
    abs = ShieldSpecialAbility.objects.all()
    # IF D_R IS 100, Roll Twice and return those
    if d_r == 100:
        ab2 = {'ab_name': ''}
        # make sure d_r can never be 100 in this section
        while d_r == 100:
            d_r = d100()
        ab1 = get_medium_shield_special_abilities(d_r)
        d_r = d100()
        # make sure d_r can never be 100 in this section
        while d_r == 100:
            d_r = d100()
        ab2 = get_medium_shield_special_abilities(d_r)

        return [ab1, ab2]
    for ability in abs:
        if ability.medium_percent_chance_lower <= d_r <= ability.medium_percent_chance_upper and d_r != 100:
            print('ability')
            ab1['ab_name'] = ability.item_ability
            return ab1


def get_major_shield_special_abilities(d_r):
    ab1 = {'ab_name': ''}
    abs = ShieldSpecialAbility.objects.all()
    # IF D_R IS 100, Roll Twice and return those
    if d_r == 100:
        ab2 = {'ab_name': ''}
        # make sure d_r can never be 100 in this section
        while d_r == 100:
            d_r = d100()
        ab1 = get_major_shield_special_abilities(d_r)
        d_r = d100()
        # make sure d_r can never be 100 in this section
        while d_r == 100:
            d_r = d100()
        ab2 = get_major_shield_special_abilities(d_r)

        return [ab1, ab2]
    for ability in abs:
        if ability.major_percent_chance_lower <= d_r <= ability.major_percent_chance_upper and d_r != 100:
            print('ability')
            ab1['ab_name'] = ability.item_ability
            return ab1


def get_mundane_items(die_size, num_die):
    number_of_items = roll_several_die(die_size, num_die)
    item_dict = {'items': []}
    for num in range(number_of_items):
        item = get_single_mundane_items()
        item_dict['items'].append(item)
    return item_dict


def get_single_mundane_items():
    dice_roll = d100()
    m_items = MundaneItemBaseTable.objects.all()
    final_result = {}
    for item_type in m_items:
        if dice_roll >= item_type.percent_lower and dice_roll <= item_type.percent_upper:
            #             TODO: Make the weapon table happen properly
            if item_type.isAlchemical:
                final_result = get_alchemical_items()
                print(final_result)
            elif item_type.isArmor:
                final_result = get_mundane_armor()
                print(final_result)
            elif item_type.isWeapon:
                final_result = get_mundane_weapon()
                print(final_result)
            elif item_type.isToolOrGear:
                final_result = get_mundane_tool_or_gear()
                print(final_result)
            #         EVENTUALLY RETURN an END RESULT
    return final_result


# THE FOLLOWING 6 Methods are for Mundane Items
def get_alchemical_items():
    dice_roll = d100()
    alch_item = {'quantity': 0, 'name': '', 'value_per': 0}
    alch_items = MundaneAlchemical.objects.all()
    for results in alch_items:
        if dice_roll >= results.percent_lower and dice_roll <= results.percent_upper:
            alch_item['quantity'] = roll_several_die(results.size_of_dice, results.number_of_dice)
            alch_item['name'] = results.item_name
            alch_item['value_per'] = results.cost_per
    print(alch_item)
    return alch_item


def get_mundane_armor():
    dice_roll = d100()
    mund_armor = {'name': '', 'value': 0, 'size': ''}
    size_roll = d100()
    # size (not in database 10% chance for small item)
    if size_roll in [4, 18, 19, 34, 45, 56, 67, 78, 89, 90]:
        mund_armor['size'] = 'Small'
    else:
        mund_armor['size'] = 'Medium'
    # The rest of this is for type and cost
    armors = MundaneAlchemical.objects.all()
    for results in armors:
        if dice_roll >= results.percent_lower and dice_roll <= results.percent_upper:
            mund_armor['name'] = results.item_name
            mund_armor['value'] = results.cost_per
    # TODO:        if mund_armor['name']=='Darkwood' ==> do that table
    # TODO:        elif mund_armor['name']=='Masterwork Shield' ==> do that table
    #
    print(mund_armor)
    return mund_armor


def get_mundane_weapon():
    dice_roll = d100()
    # Eventually this will be mund_wep = {'name':'','value':0, 'size':''} once the other 3 weapons tables are made. Til then this is fine
    mund_wep = {'name': ''}
    weapons = MundaneWeapons.objects.all()
    for results in weapons:
        if dice_roll >= results.percent_lower and dice_roll <= results.percent_upper:
            mund_wep['name'] = results.item_name
            # mund_wep['value'] = results.cost_per
    print(mund_wep)
    return mund_wep


def get_mundane_tool_or_gear():
    dice_roll = d100()
    mtog = {'name': '', 'value': 0}
    all_mtog = MundaneToolOrGear.objects.all()
    for results in all_mtog:
        if dice_roll >= results.percent_lower and dice_roll <= results.percent_upper:
            mtog['name'] = results.item_name
            mtog['value'] = results.item_value
    print(mtog)
    return mtog


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
        coin_type = 'None'
        coins_total = 'No Coins'
    else:
        coins_total = str(result) + " " + coin_type
    return coins_total


def base(request):
    title = {'title': 'Welcome to the Treasure Generator!'}
    return render(request, 'home.html', title)
