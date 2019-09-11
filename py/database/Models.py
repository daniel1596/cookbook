from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from typing import Optional

from py.database.Columns import PrimaryKey, IntegerForeignKey, IntegerNotNull, FloatNotNull, StringNotNull
from py.database.Setup import Base
from py.database.Unit import Unit


class Recipe(Base):
	__tablename__ = "Recipe"

	RecipeID = PrimaryKey()
	Name = StringNotNull()
	# Todo at some point: add images to the db? Probably good to do, presumably just the file path of the images.
	#  Also a little concerned about taking up a bunch of space in RiouxSVN with images... maybe I'd need the Pi, then, as a home server

	Ingredients = relationship("Ingredient", back_populates="Recipe")
	Steps = relationship("Step", back_populates="Recipe")

	BasedOnLink = Column(String, nullable=True)
	AdditionalInfo = Column(String, nullable=True)  # todo - make this a list of items with 1-many relationship, and render them in HTML as a <ul>


class Ingredient(Base):
	__tablename__ = "Ingredient"

	def __init__(self, food_item: str, quantity: Optional[float], unit_of_measure="", does_scale: bool=True,
				 is_first_in_section: bool=False, section_name: str=""):
		self.FoodItem = food_item
		self.Quantity = quantity if quantity else -1
		self.UnitOfMeasure = unit_of_measure.__repr__() if isinstance(unit_of_measure, Unit) else unit_of_measure
		self.DoesScale = does_scale and self.Quantity > -1
		self.IsFirstInSection = is_first_in_section
		self.SectionName = section_name

	IngredientID = PrimaryKey()
	FoodItem = StringNotNull()
	Quantity = FloatNotNull()
	UnitOfMeasure = StringNotNull()
	DoesScale = Column(Boolean, nullable=True)
	IsFirstInSection = Column(Boolean, nullable=True)
	SectionName = Column(String, nullable=True)

	RecipeID = IntegerForeignKey(Recipe, nullable=True)
	Recipe = relationship("Recipe", back_populates="Ingredients")

	# I'm not including a __repr__(self) method override here because Vue is handling the UI part


class Step(Base):
	__tablename__ = "Step"

	StepID = PrimaryKey()
	StepOrder = IntegerNotNull()
	Description = StringNotNull()

	RecipeID = IntegerForeignKey(Recipe, nullable=True)
	Recipe = relationship("Recipe", back_populates="Steps")

	def __repr__(self):
		return self.Description  # leave this in - this method is used on the front-end
