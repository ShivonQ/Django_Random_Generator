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

    result = []
    for model in base_results:

        dice_roll = randint(1, 100)
        model.objects
        this_model = model(level=enc_level)
        print(this_model)
        result.append(this_model)

    return render(request, 'treasure_result.html', result)

def base(request):
    title = {'title': 'Welcome to the Treasure Generator!'}
    return render(request, 'base.html', title)
