from enum import Enum

class Unit(Enum):
	CUP = (1, "cup")
	FL_OZ = (1/8, "oz")
	DRY_OZ = (0, "oz")  # not using the conversion factor currently; this wouldn't be uniform across dry ingredients
	POUND = (0, "lb")  # also would not convert to cup uniformly
	TBSP = (1/16, "tbsp")
	TSP = (1/(16*3), "tsp")

	def __init__(self, conversion_factor: float, unit_ui: str):
		self.conversion_factor = conversion_factor
		self.unit_ui = unit_ui

	def __repr__(self):
		return self.unit_ui


# Items to be imported in order to be (needlessly? not sure) strongly typed and avoid typos (maybe...)

FourCups = (4, Unit.CUP)
ThreeCups = (3, Unit.CUP)
FiveHalvesCup = (5/2, Unit.CUP)
TwoCups = (2, Unit.CUP)
FiveThirdsCup = (5/3, Unit.CUP)
ThreeHalvesCup = (3/2, Unit.CUP)
FiveFourthsCup = (5/4, Unit.CUP)
OneCup = (1, Unit.CUP)
ThreeQuartersCup = (3/4, Unit.CUP)
TwoThirdsCup = (2/3, Unit.CUP)
OneHalfCup = (1/2, Unit.CUP)
OneThirdCup = (1/3, Unit.CUP)
OneQuarterCup = (1/4, Unit.CUP)

ThreeTablespoons = (3, Unit.TBSP)
TwoTablespoons = (2, Unit.TBSP)
ThreeHalvesTablespoons = (3 / 2, Unit.TBSP)
OneTablespoon = (1, Unit.TBSP)
OneHalfTablespoon = (1 / 2, Unit.TBSP)

TwoTeaspoons = (2, Unit.TSP)
ThreeHalvesTeaspoons = (3 / 2, Unit.TSP)
OneTeaspoon = (1, Unit.TSP)
OneHalfTeaspoon = (1/2, Unit.TSP)
OneQuarterTeaspoon = (1/4, Unit.TSP)
OneEighthTeaspoon = (1/8, Unit.TSP)