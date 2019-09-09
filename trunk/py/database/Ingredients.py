from typing import Optional

from py.database.Models import Ingredient

"""
These are just some shortcuts for common ingredients
They actually do help as far as 
"""



# region Butter and oils

def Butter(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Butter", quantity, unit_of_measure, does_scale)

def Margarine(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Margarine", quantity, unit_of_measure, does_scale)

def CanolaOil(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Canola oil", quantity, unit_of_measure, does_scale)

def CoconutOil(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Coconut oil", quantity, unit_of_measure, does_scale)

def OliveOil(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Olive oil", quantity, unit_of_measure, does_scale)

# endregion


# region Canned ingredients

def DicedTomatoes(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Diced tomatoes", quantity, unit_of_measure, does_scale)

def FireRoastedDicedTomatoes(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Diced tomatoes, fire-roasted", quantity, unit_of_measure, does_scale)

# endregion


# region Fruit

def DriedFruit(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Dried fruit", quantity, unit_of_measure, does_scale)

# endregion


# region Ingredients with no units of measure

def Avocado(quantity: float):
    return IngredientWithoutUnits("Avocado", quantity)

def Egg(quantity: float):
    return IngredientWithoutUnits("Egg", quantity)

def Tomato(quantity: float):
    return IngredientWithoutUnits("Tomato", quantity)

def IngredientWithoutUnits(name: str, quantity: float) -> Ingredient:
    name_possibly_pluralized = name if quantity == 1 \
        else f"{name}s" if not name.endswith("o") \
        else f"{name}es"

    return Ingredient(name_possibly_pluralized, quantity)

# endregion


# region Liquids

def AlmondMilk(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Almond milk", quantity, unit_of_measure, does_scale)

def Milk(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Milk", quantity, unit_of_measure, does_scale)


def Honey(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Honey", quantity, unit_of_measure, does_scale)

def LemonJuice(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Lemon juice", quantity, unit_of_measure, does_scale)

def LimeJuice(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Lime juice", quantity, unit_of_measure, does_scale)

def MapleSyrup(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Maple syrup", quantity, unit_of_measure, does_scale)

def VegetableBroth(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Vegetable broth", quantity, unit_of_measure, does_scale)

# endregion


# region Nuts and nut butters

def AlmondButter(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Almond butter", quantity, unit_of_measure, does_scale)

def PeanutButter(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Peanut butter", quantity, unit_of_measure, does_scale)


def Almonds(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Almonds", quantity, unit_of_measure, does_scale)

def Pecans(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Pecans", quantity, unit_of_measure, does_scale)

def Pistachios(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Pistachios", quantity, unit_of_measure, does_scale)

def Walnuts(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Walnuts", quantity, unit_of_measure, does_scale)

# endregion


# region Oats

def Oats(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Oats", quantity, unit_of_measure, does_scale)

def RolledOats(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Rolled oats", quantity, unit_of_measure, does_scale)

# endregion


# region Spices and baking soda/powder

def BakingPowder(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Baking powder", quantity, unit_of_measure, does_scale)

def BakingSoda(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Baking soda", quantity, unit_of_measure, does_scale)

def Basil(quantity: Optional[float], unit_of_measure="", *, is_fresh: bool, does_scale=True):
    name = get_name_fresh_or_dried("Basil", is_fresh)
    return Ingredient(name, quantity, unit_of_measure, does_scale)

def CayennePepper(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Cayenne pepper", quantity, unit_of_measure, does_scale)

def Cilantro(quantity: Optional[float], unit_of_measure="", *, is_fresh: bool,  does_scale=True):
    name = get_name_fresh_or_dried("Cilantro", is_fresh)
    return Ingredient(name, quantity, unit_of_measure, does_scale)

def Cinnamon(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Cinnamon", quantity, unit_of_measure, does_scale)

def Cloves(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Cloves", quantity, unit_of_measure, does_scale)


def GarlicCloves(quantity: Optional[float], *, does_scale=True):
    return Ingredient("Garlic", quantity, "cloves", does_scale)

def MincedGarlic(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Garlic, minced", quantity, unit_of_measure, does_scale)


def Ginger(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Ginger", quantity, unit_of_measure, does_scale)

def Nutmeg(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Nutmeg", quantity, unit_of_measure, does_scale)

def Pepper(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Pepper", quantity, unit_of_measure, does_scale)

def Salt(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Salt", quantity, unit_of_measure, does_scale)


def get_name_fresh_or_dried(name: str, is_fresh: bool) -> str:
    return f"Cilantro, {('fresh' if is_fresh else 'dried')}"

# endregion


# region Seeds

def GroundFlaxSeed(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Ground flaxseed", quantity, unit_of_measure, does_scale)

def FlaxSeeds(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Flax seeds", quantity, unit_of_measure, does_scale)

def PumpkinSeeds(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Pumpkin seeds", quantity, unit_of_measure, does_scale)

def SunflowerSeeds(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Sunflower seeds", quantity, unit_of_measure, does_scale)

# endregion


# region Sugar and other sweet things

def ChocolateChips(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Chocolate chips", quantity, unit_of_measure, does_scale)

def BrownSugar(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Brown sugar", quantity, unit_of_measure, does_scale)

def Sugar(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Sugar", quantity, unit_of_measure, does_scale)

# endregion


# region Vegetables

def DicedOnion(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Onion, diced", quantity, unit_of_measure, does_scale)

# endregion


# region Uncategorized / miscellaneous

def UnsweetenedCoconutFlakes(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Unsweetened coconut flakes", quantity, unit_of_measure, does_scale)

# endregion