from django.db import models


class DiaryEntry(models.Model):
    # base elements of a post
    title = models.CharField(max_length=200)
    text_body = models.CharField(max_length=8000)
    # in game date elements
    in_game_month = models.CharField(max_length = 20)
    in_game_day = models.IntegerField()
    in_game_year = models.IntegerField()
    # real world dates
    date_created = models.DateField()
    date_updated = models.DateField()
    #     owner of the post
    post_owner = models.CharField(max_length = 50)
#     who can see the posts
    visible_to_all = models.BooleanField(default=True)
#     TODO: more of these regarding the individual users.

    def __str__(self):
        rep = 'Game-Date: '+str(self.in_game_day)+' '+self.in_game_month+', '+str(self.in_game_year)+'; Title: '+self.title+', Created: '+str(self.date_created)
        return rep





class TreasureCoinsBaseValue(models.Model):
    level = models.IntegerField()

    percent_lower = models.IntegerField()
    percent_upper = models.IntegerField()
    number_of_die = models.IntegerField()
    die_size = models.IntegerField()
    multiplier = models.IntegerField()
    coins_type = models.CharField(max_length=10)

    def __str__(self):
        rep = 'Level: '+str(self.level)+" | type:"+self.coins_type
        return rep


class TreasureGoodsBaseValue(models.Model):
    level = models.IntegerField()
    percent_lower = models.IntegerField()
    percent_upper = models.IntegerField()
    number_of_die = models.IntegerField()
    die_size = models.IntegerField()
    goods_type = models.CharField(max_length=3)

    def __str__(self):
        rep = 'Level: '+str(self.level)+" | type:"+self.goods_type
        return rep


class TreasureItemsBaseResults(models.Model):
    level = models.IntegerField()
    percent_lower = models.IntegerField()
    percent_upper = models.IntegerField()

    number_of_die = models.IntegerField()
    die_size = models.IntegerField()

    items_type_mundane = models.BooleanField()
    items_type_minor = models.BooleanField()
    items_type_medium = models.BooleanField()
    items_type_major = models.BooleanField()

    def __str__(self):
        rep = 'Level: '+str(self.level)+" | range:"+str(self.percent_lower)+'-'+str(self.percent_upper)
        return rep


class MundaneItemBaseTable(models.Model):
    percent_lower = models.IntegerField()
    percent_upper = models.IntegerField()

    isAlchemical = models.BooleanField()
    isArmor = models.BooleanField()
    isWeapon = models.BooleanField()
    isToolOrGear = models.BooleanField()

    def __str__(self):
        rep = "Percent Range:"+str(self.percent_lower)+'-'+str(self.percent_upper)
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


class Rod(models.Model):
    medium_percent_chance_lower = models.IntegerField()
    medium_percent_chance_upper = models.IntegerField()

    major_percent_chance_lower = models.IntegerField()
    major_percent_chance_upper = models.IntegerField()
    # if it isnt a potion it is an oil
    name = models.CharField(max_length=50)
    cost = models.IntegerField()

    def __str__(self):
        rep = ' Name: ' + self.name + \
              "Medium Range:" + str(self.medium_percent_chance_lower) + '-' + str(
            self.medium_percent_chance_upper) + ' | ' + \
              "Major Range:" + str(self.major_percent_chance_lower) + '-' + str(self.major_percent_chance_upper)
        return rep


class Staff(models.Model):
    medium_percent_chance_lower = models.IntegerField()
    medium_percent_chance_upper = models.IntegerField()

    major_percent_chance_lower = models.IntegerField()
    major_percent_chance_upper = models.IntegerField()
    # if it isnt a potion it is an oil
    name = models.CharField(max_length=50)
    cost = models.IntegerField()

    def __str__(self):
        rep = ' Name: ' + self.name + \
              "Medium Range:" + str(self.medium_percent_chance_lower) + '-' + str(
            self.medium_percent_chance_upper) + ' | ' + \
              "Major Range:" + str(self.major_percent_chance_lower) + '-' + str(self.major_percent_chance_upper)
        return rep


class Ring(models.Model):
    minor_percent_chance_lower = models.IntegerField()
    minor_percent_chance_upper = models.IntegerField()

    medium_percent_chance_lower = models.IntegerField()
    medium_percent_chance_upper = models.IntegerField()

    major_percent_chance_lower = models.IntegerField()
    major_percent_chance_upper = models.IntegerField()
    # if it isnt a potion it is an oil
    name = models.CharField(max_length=50)
    cost = models.IntegerField()

    def __str__(self):
        rep = ' Name: ' + self.name + " | Minor Range:" + str(self.minor_percent_chance_lower) + '-' + str(
            self.minor_percent_chance_upper) + ' | ' + \
              "Medium Range:" + str(self.medium_percent_chance_lower) + '-' + str(
            self.medium_percent_chance_upper) + ' | ' + \
              "Major Range:" + str(self.major_percent_chance_lower) + '-' + str(self.major_percent_chance_upper)
        return rep


class PotionOrOil(models.Model):
    minor_percent_chance_lower = models.IntegerField()
    minor_percent_chance_upper = models.IntegerField()

    medium_percent_chance_lower = models.IntegerField()
    medium_percent_chance_upper = models.IntegerField()

    major_percent_chance_lower = models.IntegerField()
    major_percent_chance_upper = models.IntegerField()
    # if it isnt a potion it is an oil
    isPotion = models.BooleanField()
    name = models.CharField(max_length=50)
    cost = models.IntegerField()

    def __str__(self):
        rep = ' Name: '+self.name + " | Minor Range:"+str(self.minor_percent_chance_lower)+'-'+str(self.minor_percent_chance_upper)+' | ' + \
              "Medium Range:" + str(self.medium_percent_chance_lower)+'-'+str(self.medium_percent_chance_upper)+' | '+ \
            "Major Range:" + str(self.major_percent_chance_lower) + '-' + str(self.major_percent_chance_upper)
        return rep


class MinorWondrousItem(models.Model):
    percent_chance = models.IntegerField()

    name = models.CharField(max_length=50)
    cost = models.IntegerField()

    def __str__(self):
        rep = ' Name: '+self.name + ' %: '+str(self.percent_chance)+' Cost: '+str(self.cost)
        return rep


class MediumWondrousItem(models.Model):
    percent_chance = models.IntegerField()

    name = models.CharField(max_length=50)
    cost = models.IntegerField()

    def __str__(self):
        rep = ' Name: '+self.name + ' %: '+str(self.percent_chance)+' Cost: '+str(self.cost)
        return rep


class MajorWondrousItem(models.Model):
    percent_chance = models.IntegerField()

    name = models.CharField(max_length=50)
    cost = models.IntegerField()

    def __str__(self):
        rep = ' Name: '+self.name + ' %: '+str(self.percent_chance)+' Cost: '+str(self.cost)
        return rep


class MagicWeapon(models.Model):
    minor_percent_chance_lower = models.IntegerField()
    minor_percent_chance_upper = models.IntegerField()

    medium_percent_chance_lower = models.IntegerField()
    medium_percent_chance_upper = models.IntegerField()

    major_percent_chance_lower = models.IntegerField()
    major_percent_chance_upper = models.IntegerField()
    name = models.CharField(max_length=50)
    cost = models.IntegerField()

    def __str__(self):
        rep = ' Name: '+self.name + " | Minor Range:"+str(self.minor_percent_chance_lower)+'-'+str(self.minor_percent_chance_upper)+' | ' + \
              "Medium Range:" + str(self.medium_percent_chance_lower)+'-'+str(self.medium_percent_chance_upper)+' | '+ \
            "Major Range:" + str(self.major_percent_chance_lower) + '-' + str(self.major_percent_chance_upper)
        return rep


class Wand(models.Model):
    minor_percent_chance_lower = models.IntegerField()
    minor_percent_chance_upper = models.IntegerField()

    medium_percent_chance_lower = models.IntegerField()
    medium_percent_chance_upper = models.IntegerField()

    major_percent_chance_lower = models.IntegerField()
    major_percent_chance_upper = models.IntegerField()
    name = models.CharField(max_length=50)
    cost = models.IntegerField()

    def __str__(self):
        rep = ' Name: '+self.name + " | Minor Range:"+str(self.minor_percent_chance_lower)+'-'+str(self.minor_percent_chance_upper)+' | ' + \
              "Medium Range:" + str(self.medium_percent_chance_lower)+'-'+str(self.medium_percent_chance_upper)+' | '+ \
            "Major Range:" + str(self.major_percent_chance_lower) + '-' + str(self.major_percent_chance_upper)
        return rep


class SpecificWeapon(models.Model):
    minor_percent_chance_lower = models.IntegerField()
    minor_percent_chance_upper = models.IntegerField()

    medium_percent_chance_lower = models.IntegerField()
    medium_percent_chance_upper = models.IntegerField()

    major_percent_chance_lower = models.IntegerField()
    major_percent_chance_upper = models.IntegerField()
    name = models.CharField(max_length=50)
    cost = models.IntegerField()

    def __str__(self):
        rep = ' Name: '+self.name + " | Minor Range:"+str(self.minor_percent_chance_lower)+'-'+str(self.minor_percent_chance_upper)+' | ' + \
              "Medium Range:" + str(self.medium_percent_chance_lower)+'-'+str(self.medium_percent_chance_upper)+' | '+ \
            "Major Range:" + str(self.major_percent_chance_lower) + '-' + str(self.major_percent_chance_upper)
        return rep


class RangedWeaponSpecialAbility(models.Model):

    minor_percent_chance_lower = models.IntegerField()
    minor_percent_chance_upper = models.IntegerField()

    medium_percent_chance_lower = models.IntegerField()
    medium_percent_chance_upper = models.IntegerField()

    major_percent_chance_lower = models.IntegerField()
    major_percent_chance_upper = models.IntegerField()

    item_ability = models.CharField(max_length=120)
    base_enhancement_bonus_modifier = models.IntegerField()

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


class MeleeWeaponSpecialAbility(models.Model):

    minor_percent_chance_lower = models.IntegerField()
    minor_percent_chance_upper = models.IntegerField()

    medium_percent_chance_lower = models.IntegerField()
    medium_percent_chance_upper = models.IntegerField()

    major_percent_chance_lower = models.IntegerField()
    major_percent_chance_upper = models.IntegerField()

    item_ability = models.CharField(max_length=120)
    base_enhancement_bonus_modifier = models.IntegerField()

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


class SpecificArmor(models.Model):
    minor_percent_chance_lower = models.IntegerField()
    minor_percent_chance_upper = models.IntegerField()

    medium_percent_chance_lower = models.IntegerField()
    medium_percent_chance_upper = models.IntegerField()

    major_percent_chance_lower = models.IntegerField()
    major_percent_chance_upper = models.IntegerField()
    name = models.CharField(max_length=50)
    cost = models.IntegerField()

    def __str__(self):
        rep = ' Name: '+self.name + " | Minor Range:"+str(self.minor_percent_chance_lower)+'-'+str(self.minor_percent_chance_upper)+' | ' + \
              "Medium Range:" + str(self.medium_percent_chance_lower)+'-'+str(self.medium_percent_chance_upper)+' | '+ \
            "Major Range:" + str(self.major_percent_chance_lower) + '-' + str(self.major_percent_chance_upper)
        return rep


class SpecificShield(models.Model):
    minor_percent_chance_lower = models.IntegerField()
    minor_percent_chance_upper = models.IntegerField()

    medium_percent_chance_lower = models.IntegerField()
    medium_percent_chance_upper = models.IntegerField()

    major_percent_chance_lower = models.IntegerField()
    major_percent_chance_upper = models.IntegerField()
    name = models.CharField(max_length=50)
    cost = models.IntegerField()

    def __str__(self):
        rep = ' Name: '+self.name + " | Minor Range:"+str(self.minor_percent_chance_lower)+'-'+str(self.minor_percent_chance_upper)+' | ' + \
              "Medium Range:" + str(self.medium_percent_chance_lower)+'-'+str(self.medium_percent_chance_upper)+' | '+ \
            "Major Range:" + str(self.major_percent_chance_lower) + '-' + str(self.major_percent_chance_upper)
        return rep


class RootMagicItemsTable(models.Model):
    minor_percent_chance_lower = models.IntegerField()
    minor_percent_chance_upper = models.IntegerField()

    medium_percent_chance_lower = models.IntegerField()
    medium_percent_chance_upper = models.IntegerField()

    major_percent_chance_lower = models.IntegerField()
    major_percent_chance_upper = models.IntegerField()
    name = models.CharField(max_length=50)

    def __str__(self):
        rep = ' Name: '+self.name + " | Minor Range:"+str(self.minor_percent_chance_lower)+'-'+str(self.minor_percent_chance_upper)+' | ' + \
              "Medium Range:" + str(self.medium_percent_chance_lower)+'-'+str(self.medium_percent_chance_upper)+' | '+ \
            "Major Range:" + str(self.major_percent_chance_lower) + '-' + str(self.major_percent_chance_upper)
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
    percent_lower = models.IntegerField()
    percent_upper = models.IntegerField()

    value_dice_number = models.IntegerField()
    value_dice_size = models.IntegerField()
    value_multiplier = models.IntegerField()

    art_name = models.CharField(max_length=800)

    def get_val_and_name(self):
        all = [self.art_name, self.art_value_dice_number, self.art_value_dice_size]
        return all

    def __str__(self):
        rep = "Percent Range:"+str(self.percent_lower)+'-'+str(self.percent_upper)+' Name: '+self.art_name
        return rep


class Darkwood(models.Model):
    percent_lower = models.IntegerField()
    percent_upper = models.IntegerField()

    type = models.CharField(max_length = 80)
    value = models.IntegerField()

    def __str__(self):
        rep = "Percent Range:"+str(self.percent_lower)+'-'+str(self.percent_upper)+' Name: '+self.type
        return rep

        
class Masterwork_Shield(models.Model):
    percent_lower = models.IntegerField()
    percent_upper = models.IntegerField()

    type = models.CharField(max_length=80)
    value = models.IntegerField()

    def __str__(self):
        rep = "Percent Range:"+str(self.percent_lower)+'-'+str(self.percent_upper)+' Name: '+self.type
        return rep


class Gems(models.Model):
    # All gem values are in gp so no money type needed
    percent_lower = models.IntegerField()
    percent_upper = models.IntegerField()
    value_dice_number = models.IntegerField()
    value_dice_size = models.IntegerField()
    value_multiplier = models.IntegerField()
    # will be a long string of gems names, that can be split for final display
    gem_name = models.CharField(max_length=6000)

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


class BaseMagicItemGenTable(models.Model):
    minor_percent_chance_lower = models.IntegerField()
    minor_percent_chance_upper = models.IntegerField()

    medium_percent_chance_lower = models.IntegerField()
    medium_percent_chance_upper = models.IntegerField()

    major_percent_chance_lower = models.IntegerField()
    major_percent_chance_upper = models.IntegerField()

    table_to_use = models.CharField(max_length=300)

    def __str__(self):
        rep = ' Name: ' + self.table_to_use + " | Minor Range:" + str(self.minor_percent_chance_lower) + '-' + str(
            self.minor_percent_chance_upper) + ' | ' + \
              "Medium Range:" + str(self.medium_percent_chance_lower) + '-' + str(
            self.medium_percent_chance_upper) + ' | ' + \
              "Major Range:" + str(self.major_percent_chance_lower) + '-' + str(self.major_percent_chance_upper)
        return rep


class ShieldSpecialAbility(models.Model):

    minor_percent_chance_lower = models.IntegerField()
    minor_percent_chance_upper = models.IntegerField()

    medium_percent_chance_lower = models.IntegerField()
    medium_percent_chance_upper = models.IntegerField()

    major_percent_chance_lower = models.IntegerField()
    major_percent_chance_upper = models.IntegerField()

    item_ability = models.CharField(max_length=120)
    base_price_modifier = models.IntegerField()
    base_enhancement_bonus_modifier = models.IntegerField()

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


class ArmorSpecialAbility(models.Model):

    minor_percent_chance_lower = models.IntegerField()
    minor_percent_chance_upper = models.IntegerField()

    medium_percent_chance_lower = models.IntegerField()
    medium_percent_chance_upper = models.IntegerField()

    major_percent_chance_lower = models.IntegerField()
    major_percent_chance_upper = models.IntegerField()

    item_ability = models.CharField(max_length=120)
    base_price_modifier = models.IntegerField()
    base_enhancement_bonus_modifier = models.IntegerField()

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
