from abc import abstractmethod
from enum import Enum


class MeasurementType(Enum):
	CUP = 1
	FLUID_OUNCE = 1/8
	TBSP = 1/16
	TSP = (1/16) / 3


class Measurement:
	def __init__(self, value):
		self._value = value
	
	def __repr__():
		return _value

	@abstractmethod
	def multiply_by(factor: int):
		pass

class StringMeasurement(Measurement):
	def __init__(self, value):
		if not isinstance(value, str):
			raise SyntaxError("This is illegal - should be a str")
	
	def multiply_by(factor: int):
		_value = f"{factor} * {self._value}"


class ArithmeticMeasurement(Measurement):
	def __init__(self, value):
		if not (isinstance(value, int) or isinstance(value, float)):
			raise SyntaxError("This is illegal - should be an int or float")

	def multiply_by(factor: int):
		_value *= factor
	

class ConvertibleArithmeticMeasurement(ArithmeticMeasurement):
	def __init__(self, value, measurement_type: MeasurementType):
		super().__init__(value)
		self._measurement_type = measurement_type

	def __repr__() -> str:
		return 





"""
what are we wanting to set up for?
- 


"""