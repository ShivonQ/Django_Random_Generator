from django.shortcuts import *

from Random_Gen.models import *

coins = TreasureCoinsBaseValue
goods = TreasureGoodsBaseValue
items = TreasureItemsBaseResults
base_results=[coins,goods,items]

def treasure_result(request):
    treasure_result = []
    for model in base_results:

        dice_roll = randint(1, 100)
        level = request.level
        this_model = (model.objects.where('level')==level)
        print(this_model)
        treasure_result.append(this_model)

    return render(request, 'treasure_result.html', treasure_result)

def base(request):
    title = {'title': 'Welcome to the Treasure Generator!'}
    return render(request, 'base.html', title)
