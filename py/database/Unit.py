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