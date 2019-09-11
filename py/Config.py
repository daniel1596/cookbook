from abc import abstractmethod


class ConfigBase:  # not inheriting from Enum because you can't extend the Enum class
	database_location = 'sqlite:///db/recipes.db?check_same_thread=False'

	@property
	@abstractmethod
	def vue_file(self) -> str:
		pass


class DevelopmentConfig(ConfigBase):
	@property
	def vue_file(self) -> str:
		return "vue.js"


class ProductionConfig(ConfigBase):
	@property
	def vue_file(self) -> str:
		return "vue.min.js"


# global object for imports
Config = DevelopmentConfig()
