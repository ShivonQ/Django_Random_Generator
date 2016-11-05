from django.db import models
from random import randint
# Create your models here.


class TreasureCoinsBaseValue(models.Model):
    level = models.IntegerField()

    coins_percent_lower=models.IntegerField()
    coins_percent_upper = models.IntegerField()
    coins_number_of_die = models.IntegerField()
    coins_die_size = models.IntegerField()
    coins_multiplier = models.IntegerField()
    coins_type = models.CharField(max_length=10)

    def __str__(self):
        rep = 'Level: '+str(self.level)+" | type:"+self.coins_type
        return rep


class TreasureGoodsBaseValue(models.Model):
    level = models.IntegerField()
    goods_percent_lower = models.IntegerField()
    goods_percent_upper = models.IntegerField()
    goods_number_of_die = models.IntegerField()
    goods_die_size = models.IntegerField()
    goods_type = models.CharField(max_length=3)

    def __str__(self):
        rep = 'Level: '+str(self.level)+" | type:"+self.goods_type
        return rep



class TreasureItemsBaseResults(models.Model):
    level = models.IntegerField()
    items_percent_lower = models.IntegerField()
    items_percent_upper = models.IntegerField()

    items_number_of_die = models.IntegerField()
    items_die_size = models.IntegerField()

    items_type_mundane = models.BooleanField()
    items_type_minor = models.BooleanField()
    items_type_medium = models.BooleanField()
    items_type_major = models.BooleanField()

    def __str__(self):
        rep = 'Level: '+str(self.level)+" | range:"+str(self.items_percent_lower)+'-'+str(self.items_percent_upper)
        return rep


class MundaneItemBaseTable(models.Model):
    mundane_percent_lower = models.IntegerField()
    mundane_percent_upper = models.IntegerField()

    isAlchemical = models.BooleanField()
    isArmor = models.BooleanField()
    isWeapon = models.BooleanField()
    isToolOrGear = models.BooleanField()

    def __str__(self):
        rep = "Percent Range:"+str(self.mundane_percent_lower)+'-'+str(self.mundane_percent_upper)
        return rep

class MundaneAlchemical(models.Model):
    percent_lower = models.IntegerField()
    percent_upper = models.IntegerField()

    number_of_dice = models.IntegerField()
    size_of_dice = models.IntegerField()

    cost_per = models.IntegerField()
    item_name = models.CharField(max_length=50)

    def get_amount_cost_name(self):
        all = [self.item_name, self.cost_per, self.number_of_dice, self.size_of_dice]
        return all

    def __str__(self):
        rep = "Percent Range:"+str(self.percent_lower)+'-'+str(self.percent_upper)+' Name: '+self.item_name
        return rep


class MundaneArmor(models.Model):
    percent_lower = models.IntegerField()
    percent_upper = models.IntegerField()

    cost_per = models.IntegerField()
    item_name = models.CharField(max_length=50)

    def get_cost_name(self):
        all = [self.item_name, self.cost_per]
        return all

    def __str__(self):
        rep = "Percent Range:"+str(self.percent_lower)+'-'+str(self.percent_upper)+' Name: '+self.item_name
        return rep


class MundaneWeapons(models.Model):
    percent_lower = models.IntegerField()
    percent_upper = models.IntegerField()

    item_name = models.CharField(max_length=50)

    def get_item(self):
        all = [self.item_name]
        return all

    def __str__(self):
        rep = "Percent Range:"+str(self.percent_lower)+'-'+str(self.percent_upper)+' Name: '+self.item_name
        return rep

class MundaneToolOrGear(models.Model):
    percent_lower = models.IntegerField()
    percent_upper = models.IntegerField()

    item_value = models.IntegerField()
    item_name = models.CharField(max_length=50)

    def get_name_and_val(self):
        all =[self.item_name,self.item_value]
        return all

    def __str__(self):
        rep = "Percent Range:"+str(self.percent_lower)+'-'+str(self.percent_upper)+' Name: '+self.item_name
        return rep

class Art(models.Model):
    # All art values are in gp so no money type needed
    art_percent_lower = models.IntegerField()
    art_percent_upper = models.IntegerField()

    art_value_dice_number = models.IntegerField()
    art_value_dice_size = models.IntegerField()

    art_name = models.CharField(max_length=50)

    def get_val_and_name(self):
        all = [self.art_name, self.art_value_dice_number, self.art_value_dice_size]
        return all

    def __str__(self):
        rep = "Percent Range:"+str(self.percent_lower)+'-'+str(self.percent_upper)+' Name: '+self.art_name
        return rep


class Gems(models.Model):
    # All gem values are in gp so no money type needed
    gems_percent_lower = models.IntegerField()
    gems_percent_upper = models.IntegerField()
    gem_value_dice_number = models.IntegerField()
    gem_value_dice_size = models.IntegerField()
    # will be a long string of gems names, that can be split for final display
    gem_name = models.CharField(max_length=500)

    def get_val_and_name(self):
        all = [self.gem_name, self.gem_value_dice_number, self.gem_value_dice_size]
        return all

    def __str__(self):
        rep = "Percent Range:"+str(self.percent_lower)+'-'+str(self.percent_upper)+' Name: '+self.gem_name
        return rep


class Items(models.Model):
    minor_percent_chance_lower = models.IntegerField()
    minor_percent_chance_upper = models.IntegerField()

    medium_percent_chance_lower = models.IntegerField()
    medium_percent_chance_upper = models.IntegerField()

    major_percent_chance_lower = models.IntegerField()
    major_percent_chance_upper = models.IntegerField()

    item_type = models.CharField(max_length=120)

    def __str__(self):
        return 'Item Name : '+self.item_type


class ArmorAndShields(models.Model):
    minor_percent_chance_lower = models.IntegerField()
    minor_percent_chance_upper = models.IntegerField()

    medium_percent_chance_lower = models.IntegerField()
    medium_percent_chance_upper = models.IntegerField()

    major_percent_chance_lower = models.IntegerField()
    major_percent_chance_upper = models.IntegerField()

    item = models.CharField(max_length=130)
    price = models.IntegerField()

    def get_cost_and_type(self):
        c_and_t = [self.item, self.price]
        return c_and_t

    def __str__(self):
        rep = ' Name: '+self.item + " | Minor Range:"+str(self.minor_percent_chance_lower)+'-'+str(self.minor_percent_chance_upper)+' | ' + \
              "Medium Range:" + str(self.medium_percent_chance_lower)+'-'+str(self.medium_percent_chance_upper)+' | '+ \
            "Major Range:" + str(self.major_percent_chance_lower) + '-' + str(self.major_percent_chance_upper)
        return rep


class ArmorType(models.Model):
    percent_chance_lower = models.IntegerField()
    percent_chance_upper = models.IntegerField()

    type = models.CharField(max_length=120)
    cost = models.IntegerField()

    def get_cost_and_type(self):
        c_and_t = [self.type, self.cost]
        return c_and_t

    def __str__(self):
        rep = ' Name: '+self.type +"Percent Range:"+str(self.percent_chance_lower)+'-'+str(self.percent_chance_upper)
        return rep



class ShieldType(models.Model):
    percent_chance_lower = models.IntegerField()
    percent_chance_upper = models.IntegerField()

    type = models.CharField(max_length=120)
    cost = models.IntegerField()

    def get_cost_and_type(self):
        c_and_t = [self.type, self.cost]
        return c_and_t

    def __str__(self):
        rep = ' Name: '+self.type +"Percent Range:"+str(self.percent_chance_lower)+'-'+str(self.percent_chance_upper)
        return rep


class ArmorSpecialAbility(models.Model):

    minor_percent_chance_lower = models.IntegerField()
    minor_percent_chance_upper = models.IntegerField()

    medium_percent_chance_lower = models.IntegerField()
    medium_percent_chance_upper = models.IntegerField()

    major_percent_chance_lower = models.IntegerField()
    major_percent_chance_upper = models.IntegerField()

    item_ability = models.CharField(max_length=120)
    base_price_modifier = models.IntegerField()

    def get_cost_and_type(self):
        c_and_t = [self.item_ability, self.base_price_modifier]
        return c_and_t

    def __str__(self):
        rep = ' Name: ' + self.item_ability + " | Minor Range:" + str(self.minor_percent_chance_lower) + '-' + str(
            self.minor_percent_chance_upper) + ' | ' + \
              "Medium Range:" + str(self.medium_percent_chance_lower) + '-' + str(
            self.medium_percent_chance_upper) + ' | ' + \
              "Major Range:" + str(self.major_percent_chance_lower) + '-' + str(self.major_percent_chance_upper)
        return rep
