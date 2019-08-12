from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.Columns import PrimaryKey, IntegerForeignKey, IntegerNotNull, FloatNotNull, StringNotNull
from database.Setup import Base


class Recipe(Base):
    __tablename__ = "Recipe"

    RecipeID = PrimaryKey()
    Name = StringNotNull()

    Ingredients = relationship("Ingredient", back_populates="Recipe")
    Steps = relationship("Step", back_populates="Recipe")

    BasedOnLink = Column(String, nullable=True)
    AdditionalInfo = Column(String, nullable=True)

    # maybe could have another property here to determine if there are "ingredient sets"? I.e. two collections of ingredients


class Ingredient(Base):
    __tablename__ = "Ingredient"

    IngredientID = PrimaryKey()
    FoodItem = StringNotNull()
    Quantity = StringNotNull()  # this includes unit of measure

    RecipeID = IntegerForeignKey(Recipe, nullable=True)
    Recipe = relationship("Recipe", back_populates="Ingredients")

    def __repr__(self):
        return f"{self.Quantity} {self.FoodItem}"


class Step(Base):
    __tablename__ = "Step"

    StepID = PrimaryKey()
    StepOrder = IntegerNotNull()
    Description = StringNotNull()

    RecipeID = IntegerForeignKey(Recipe, nullable=True)
    Recipe = relationship("Recipe", back_populates="Steps")

    def __repr__(self):
        return self.Description