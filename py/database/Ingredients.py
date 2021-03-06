from typing import Optional

from py.database.Models import Ingredient

"""
The purpose of these methods is:
(1) When adding/modifying recipes, I can use auto-complete to add ingredients faster
(2) They also make the recipe inserts code a little more readable, perhaps
(3) I don't want to create a separate FoodItem table in the database and reference that every time I create an ingredient.
		Much better for scripting purposes to keep these methods in memory.
		
It is not the most elegant solution - I would love to have a more generic way of doing this - but it will work.
	And at the moment, that's all I care about. I don't need to spend R&D time implementing an elegant way right now.
"""

# region Butter and oils

def Butter(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Butter", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Margarine(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Margarine", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def CanolaOil(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Canola oil", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def CoconutOil(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Coconut oil", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def OliveOil(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Olive oil", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Tahini(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Tahini", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

# endregion


# region Canned ingredients

# Not sure what I want to do about beans - if I'm going to default to dried vs canned in some situations, etc.
def MixedBeans(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Mixed beans", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def DicedTomatoes(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Diced tomatoes", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def FireRoastedDicedTomatoes(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Diced tomatoes, fire-roasted", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

# endregion


# region Flour

def AlmondFlour(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Almond flour", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def CoconutFlour(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Coconut flour", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

# endregion


# region Fruit

def Banana(quantity: Optional[float], *, is_first_in_section: bool=False, section_name: str=""):
	return IngredientWithoutUnits("Banana", quantity, is_first_in_section=is_first_in_section, section_name=section_name)

def Blueberries(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Blueberries", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def DriedFruit(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Dried fruit", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def FrozenMixedBerries(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Frozen mixed berries", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

# endregion


# region Grains

def BrownRice(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Brown rice", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Oats(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Oats", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def RolledOats(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Rolled oats", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Quinoa(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Quinoa", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

# endregion


# region Ingredients with no units of measure

def Avocado(quantity: float, is_first_in_section: bool=False, section_name: str=""):
	return IngredientWithoutUnits("Avocado", quantity, is_first_in_section=is_first_in_section, section_name=section_name)

def Egg(quantity: float, is_first_in_section: bool=False, section_name: str=""):
	return IngredientWithoutUnits("Egg", quantity, is_first_in_section=is_first_in_section, section_name=section_name)

def Tomato(quantity: float, is_first_in_section: bool=False, section_name: str=""):
	return IngredientWithoutUnits("Tomato", quantity, is_first_in_section=is_first_in_section, section_name=section_name)

# endregion


# region Liquids

def AlmondMilk(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Almond milk", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Milk(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Milk", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)


def AppleCiderVinegar(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Apple cider vinegar", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Honey(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Honey", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def LemonJuice(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Lemon juice", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def LimeJuice(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Lime juice", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def MapleSyrup(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Maple syrup", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def SoySauce(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Soy sauce", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def VegetableBroth(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Vegetable broth", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Water(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Water", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

# endregion


# endregion Meats

def ChunkedChicken(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Chicken, cut into chunks", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def GroundTurkey(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Ground turkey", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

# endregion


# region Nuts and nut butters

def AlmondButter(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Almond butter", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def PeanutButter(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Peanut butter", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)


def Almonds(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Almonds", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Pecans(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Pecans", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Pistachios(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Pistachios", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Walnuts(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Walnuts", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

# endregion


# region Spices, herbs, and baking soda/powder

def BakingPowder(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Baking powder", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def BakingSoda(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Baking soda", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Basil(quantity: Optional[float], unit_of_measure="", *, is_fresh: bool, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	name = get_name_fresh_or_dried("Basil", is_fresh)
	return Ingredient(name, quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def CayennePepper(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Cayenne pepper", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Cilantro(quantity: Optional[float], unit_of_measure="", *, is_fresh: bool,  does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	name = get_name_fresh_or_dried("Cilantro", is_fresh)
	return Ingredient(name, quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Cinnamon(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Cinnamon", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Cloves(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Cloves", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Cumin(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Cumin", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)


def GarlicCloves(quantity: Optional[float], *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Garlic", quantity, "cloves", does_scale, is_first_in_section, section_name)

def MincedGarlic(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Garlic, minced", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)


def Ginger(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Ginger", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Nutmeg(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Nutmeg", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Oregano(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Oregano", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Pepper(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Pepper", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Salt(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Salt", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)


def get_name_fresh_or_dried(name: str, is_fresh: bool) -> str:
	return f"{name}, {('fresh' if is_fresh else 'dried')}"

# endregion


# region Seeds

def GroundFlaxSeed(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Ground flaxseed", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def FlaxSeeds(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Flax seeds", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def PumpkinSeeds(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Pumpkin seeds", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def SunflowerSeeds(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Sunflower seeds", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

# endregion


# region Sugar and other sweet things

def ChocolateChips(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Chocolate chips", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def BrownSugar(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Brown sugar", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def Sugar(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Sugar", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

# endregion


# region Vegetables

def Cucumber(quantity: Optional[float], *, is_first_in_section: bool=False, section_name: str=""):
	return IngredientWithoutUnits("Cucumber", quantity, is_first_in_section=is_first_in_section, section_name=section_name)

def DicedOnion(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Onion, diced", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def GreenBellPepper(quantity: Optional[float], *, is_first_in_section: bool=False, section_name: str=""):
	return IngredientWithoutUnits("Green bell pepper", quantity, is_first_in_section=is_first_in_section, section_name=section_name)

def RedBellPepper(quantity: Optional[float], *, is_first_in_section: bool=False, section_name: str=""):
	return IngredientWithoutUnits("Red bell pepper", quantity, is_first_in_section=is_first_in_section, section_name=section_name)

def Spinach(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Spinach", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

# endregion


# region Uncategorized / miscellaneous

def UnsweetenedCoconutFlakes(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Unsweetened coconut flakes", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

def VanillaExtract(quantity: Optional[float], unit_of_measure="", *, does_scale=True, is_first_in_section: bool=False, section_name: str=""):
	return Ingredient("Vanilla extract", quantity, unit_of_measure, does_scale, is_first_in_section, section_name)

# endregion


def IngredientWithoutUnits(name: str, quantity: float, is_first_in_section: bool=False, section_name: str="") -> Ingredient:
	name_possibly_pluralized = name if quantity == 1 \
		else f"{name}s" if not name.endswith("o") \
		else f"{name}es"

	return Ingredient(name_possibly_pluralized, quantity, does_scale=True, is_first_in_section=is_first_in_section, section_name=section_name)