from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from database.Columns import PrimaryKey, IntegerForeignKey, IntegerNotNull, FloatNotNull, StringNotNull
from database.Setup import Base
from database.Unit import Unit


class Recipe(Base):
    __tablename__ = "Recipe"

    RecipeID = PrimaryKey()
    Name = StringNotNull()

    Ingredients = relationship("Ingredient", back_populates="Recipe")
    Steps = relationship("Step", back_populates="Recipe")

    BasedOnLink = Column(String, nullable=True)
    AdditionalInfo = Column(String, nullable=True)


class Ingredient(Base):
    __tablename__ = "Ingredient"

    def __init__(self, foodItem: str, quantity: float, unitOfMeasure, doesScale=True):
        self.FoodItem = foodItem
        self.Quantity = quantity if quantity else -1
        self.UnitOfMeasure = unitOfMeasure.__repr__() if isinstance(unitOfMeasure, Unit) else unitOfMeasure
        self.DoesScale = doesScale

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