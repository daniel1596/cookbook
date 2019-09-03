from enum import Enum

class Config(Enum):
    DB_LOCATION = 'sqlite:///db/recipes.db?check_same_thread=False'