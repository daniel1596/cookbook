from typing import Optional

from py.database.Models import Ingredient

"""
These are just some shortcuts for common ingredients
They actually do help as far as 
"""


def Egg(quantity: float):
    return Ingredient("Egg", quantity)


# region Butter and oils

def Butter(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Butter", quantity, unit_of_measure, does_scale)

def Margarine(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Margarine", quantity, unit_of_measure, does_scale)

def CanolaOil(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Canola oil", quantity, unit_of_measure, does_scale)

def OliveOil(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Olive oil", quantity, unit_of_measure, does_scale)

# endregion


# region Milk, water, broth

def AlmondMilk(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Almond milk", quantity, unit_of_measure, does_scale)

def Milk(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Milk", quantity, unit_of_measure, does_scale)

def VegetableBroth(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Vegetable broth", quantity, unit_of_measure, does_scale)

# endregion


# region Nuts

def Walnuts(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Walnuts", quantity, unit_of_measure, does_scale)

# endregion


# region Oats

def Oats(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Oats", quantity, unit_of_measure, does_scale)

# endregion


# region Spices and baking soda/powder

def BakingPowder(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Baking powder", quantity, unit_of_measure, does_scale)

def BakingSoda(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Baking soda", quantity, unit_of_measure, does_scale)

def Basil(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Basil", quantity, unit_of_measure, does_scale)

def Cilantro(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Cilantro", quantity, unit_of_measure, does_scale)

def Cinnamon(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Cinnamon", quantity, unit_of_measure, does_scale)

def Pepper(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Pepper", quantity, unit_of_measure, does_scale)

def Salt(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Salt", quantity, unit_of_measure, does_scale)

# endregion


# region Sugar and other sweet things

def ChocolateChips(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Chocolate chips", quantity, unit_of_measure, does_scale)

def BrownSugar(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Brown sugar", quantity, unit_of_measure, does_scale)

def Sugar(quantity: Optional[float], unit_of_measure="", *, does_scale=True):
    return Ingredient("Sugar", quantity, unit_of_measure, does_scale)

# endregion