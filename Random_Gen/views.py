from django.shortcuts import *
# import pdb
from Random_Gen.models import *

coins = TreasureCoinsBaseValue
goods = TreasureGoodsBaseValue
items = TreasureItemsBaseResults
base_results=[coins,goods,items]


def treasure_result(request):
    if request.method == 'POST':
        enc_level = request.POST.get('enc_level',1)
    else:
        enc_level = 1

    result = {'result':[]}
    # second_list = []
    for model in base_results:
        # for model.coins take die size and number of die, for each number in number_of_die:randint(1,die_size)
        # add the die rolls together and multiply them by the multiplier
        # add on the coin_type, pack into a dictionary

        # foor the goods same first step, different second step, instead just see what string is there "art' or 'gem'

        # for the items one, same first step, then check for the 'True' value in the 4 booleans.
        # Depending on which is True make that the item type

        # all three are packed into a dictionary and sent to the html page to be displayed, maybe with a title.
        dice_roll = randint(1, 100)
        # model.objects
        these_models = model.objects.filter(level=enc_level).values()

        for thing in these_models:
            p_up = thing['percent_upper']
            p_dn = thing['percent_lower']
            if dice_roll>=p_dn and dice_roll<=p_up:
                result['result'].append(thing)
                # print(these_models)
        # result.append(these_models)


    return render(request, 'treasure_result.html', result)

def base(request):
    title = {'title': 'Welcome to the Treasure Generator!'}
    return render(request, 'base.html', title)
