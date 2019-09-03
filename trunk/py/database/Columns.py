from sqlalchemy import Column, Integer, ForeignKey, String, Float
from sqlalchemy.ext.declarative import DeclarativeMeta


"""
Some methods to simulate Column subclasses, allowing for more readable/less verbose Model class definitions
Originally I was creating subclasses with only __init__() methods, 
 but when I tried that approach for PrimaryKey(), the count() method failed.
"""

def PrimaryKey() -> Column:
	"""Create a primary key column."""
	return Column(Integer, primary_key=True)


def IntegerForeignKey(model: DeclarativeMeta, *, nullable: bool = False) -> Column:
	"""
	Create an integer foreign key column.
	Assumes that any model with table name "Item" will have "ItemID" as the primary key of that table.

	Note that foreign keys are not nullable by default for SQLAlchemy, and in some cases, I might allow nulls.
	But in most cases, we should know. All teams should know their sport, and all pitchers should know their teams, etc.
	"""
	table_name = model.__tablename__
	return Column(Integer, ForeignKey(f"{table_name}.{table_name.title()}ID"), nullable=nullable)


def IntegerNotNull() -> Column:
	return Column(Integer, nullable=False)


def FloatNotNull() -> Column:
	return Column(Float, nullable=False)


def StringNotNull() -> Column:
	return Column(String, nullable=False)