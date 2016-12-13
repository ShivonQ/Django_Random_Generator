from django.contrib import admin

from Random_Gen.models import *

# Register your models here.
admin.site.register(TreasureCoinsBaseValue)
admin.site.register(TreasureGoodsBaseValue)
admin.site.register(TreasureItemsBaseResults)

admin.site.register(RootMagicItemsTable)
admin.site.register(PotionOrOil)
admin.site.register(Ring)
admin.site.register(Rod)
admin.site.register(Staff)
admin.site.register(Wand)
admin.site.register(ArmorAndShields)
admin.site.register(ArmorType)
admin.site.register(ArmorSpecialAbility)
admin.site.register(Darkwood)
admin.site.register(Masterwork_Shield)
admin.site.register(ShieldSpecialAbility)
admin.site.register(MinorWondrousItem)
admin.site.register(MediumWondrousItem)
admin.site.register(MajorWondrousItem)

admin.site.register(MundaneItemBaseTable)
admin.site.register(MundaneAlchemical)
admin.site.register(MundaneArmor)
admin.site.register(MundaneWeapons)
admin.site.register(MundaneToolOrGear)
admin.site.register(Art)
admin.site.register(Gems)
admin.site.register(Items)

# admin.site.register(ShieldType)


admin.site.register(SpecificArmor)
admin.site.register(SpecificShield)
admin.site.register(MagicWeapon)
admin.site.register(SpecificWeapon)
admin.site.register(MeleeWeaponSpecialAbility)
admin.site.register(RangedWeaponSpecialAbility)

# Next Sprints Models
admin.site.register(DiaryEntry)