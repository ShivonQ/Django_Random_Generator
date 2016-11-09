from django import forms

from Random_Gen.models import *


class TreasureForm(forms.IntegerField):
    class Meta:
        base_coins_model = TreasureCoinsBaseValue
        base_goods_model = TreasureGoodsBaseValue
        base_items_model = TreasureItemsBaseResults
        field = ('level',)
