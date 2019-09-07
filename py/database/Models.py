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

    # todo - want to have sections in the list of ingredients (nullable).
    #  If not null, this would be just something to insert an end of a </ul>, the title of a new section, and then a starting <ul>.

    Ingredients = relationship("Ingredient", back_populates="Recipe")
    Steps = relationship("Step", back_populates="Recipe")

    BasedOnLink = Column(String, nullable=True)
    AdditionalInfo = Column(String, nullable=True)  # todo - make this a list of items with 1-many relationship, and render them in HTML as a <ul>


class Ingredient(Base):
    __tablename__ = "Ingredient"

    def __init__(self, food_item: str, quantity: Optional[float], unit_of_measure="", does_scale=True):
        self.FoodItem = food_item
        self.Quantity = quantity if quantity else -1
        self.UnitOfMeasure = unit_of_measure.__repr__() if isinstance(unit_of_measure, Unit) else unit_of_measure
        self.DoesScale = does_scale and self.Quantity > -1

    IngredientID = PrimaryKey()
    FoodItem = StringNotNull()
    Quantity = FloatNotNull()
    UnitOfMeasure = StringNotNull()
    DoesScale = Column(Boolean, nullable=True)

    RecipeID = IntegerForeignKey(Recipe, nullable=True)
    Recipe = relationship("Recipe", back_populates="Ingredients")


class Step(Base):
    __tablename__ = "Step"

    StepID = PrimaryKey()
    StepOrder = IntegerNotNull()
    Description = StringNotNull()

    RecipeID = IntegerForeignKey(Recipe, nullable=True)
    Recipe = relationship("Recipe", back_populates="Steps")

    def __repr__(self):
        return self.Description
