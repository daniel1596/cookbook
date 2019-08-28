from typing import List

from database.Models import *
from database.Setup import reset_data, session # create_session  
from database.Unit import Unit

""" 
New way of doing things - importing the session from Setup and not using the lovely contextmanager. At least, for now.
"""

def __make_recipe(name: str, ingredients: List[Ingredient], steps_list: List[str], *, based_on_link: str = "", additional_info: str = ""):
    #ingredients = [Ingredient(FoodItem=k, Quantity=v) for k, v in ingredients_kv.items()]
    steps = [Step(StepOrder=i, Description=description) for i, description in enumerate(steps_list)]

    recipe = Recipe(Name=name, Steps=steps, Ingredients=ingredients, BasedOnLink=based_on_link, AdditionalInfo=additional_info)

    session.add(recipe)
    session.commit()


def insert_all():  
    reset_data()
    __make_bean_based()
    #__make_breads()
    #__make_breakfast()

#def Ing()


def __make_bean_based():
    __make_recipe("Bean burgers", [
        Ingredient("Beans", 1, "15-oz can"),
        Ingredient("Quinoa", 1/4, Unit.CUP),
        Ingredient("Oats", 1/2, Unit.CUP),
        Ingredient("Water", 1/2, Unit.CUP),
        Ingredient("Bell pepper (or tomato), minced", 1/4, Unit.CUP),
        Ingredient("Onion, minced", 2, Unit.TBSP),
        Ingredient("Garlic, minced", 2, "cloves"),
        Ingredient("Cumin, ground", 3/2, Unit.TSP),
        Ingredient("Salt", 1/2, Unit.TSP),
        Ingredient("Paprika/cayenne", None, "A bit of", doesScale=False),
        Ingredient("Egg", 1, ""),
        Ingredient("Oil (for sauteeing)", 3, Unit.TBSP, doesScale=False)
    ], [
        "Heat up the quinoa (bring to boil, simmer for 15-20 minutes)",
        "Mash the beans with a fork",
        "Mix all dry ingredients + egg",
        "Form the mixture into about 5 patties",
        "Cook the patties in the oil in a large skillet for a few minutes per side."
    ],
    additional_info="These save fine a couple days, at least, in the fridge.",
    based_on_link="https://www.allrecipes.com/recipe/220661/quinoa-black-bean-burgers/")

    __make_recipe("Mexican bean salad", [
        Ingredient("Canned beans (Simple Truth organic three-bean)", 2, "cans"),
        Ingredient("Green bell pepper, diced", 1, ""),
        Ingredient("Onion, diced", 1, ""),
        Ingredient("Corn, frozen", 10, Unit.DRY_OZ),
        Ingredient("Diced tomatoes, canned", 14.5, Unit.DRY_OZ),
        Ingredient("Olive oil", 1/4, Unit.CUP),
        Ingredient("Cilantro, dried", 1/4, Unit.CUP),
        Ingredient("Apple cider vinegar", 3, Unit.TBSP),
        Ingredient("Lime juice", 2, Unit.TBSP),
        Ingredient("Lemon juice", 1, Unit.TBSP),
        Ingredient("Cumin, ground", 2, Unit.TSP),
        Ingredient("Dried minced garlic", 1, Unit.TSP),
        Ingredient("Sugar", 1, Unit.TSP),
        Ingredient("Salt", 1, Unit.TSP),
        Ingredient("Cayenne pepper", 1/2, Unit.TSP),
        Ingredient("Black pepper", None, "A few sprinkles", doesScale=False),
    ], [
        "Dice bell pepper and onion. Drain beans and diced tomatoes. Heat up frozen corn.",
        "Mix these ingredients (top half of the list) together in a large bowl.",
        "Mix the lower half of the ingredients (wet + spices/herbs) together in a small bowl.",
        "Pour wet over dry and stir."
    ],
    based_on_link="http://allrecipes.com/recipe/14169/mexican-bean-salad/")

    __make_recipe("Roasted chickpeas", {
        Ingredient("Chickpeas", 2, Unit.CUP),
        Ingredient("Olive oil", 2, Unit.TBSP),
        Ingredient("Ground cumin", 1, Unit.TBSP),
        Ingredient("Garlic powder", 1, Unit.TBSP),
        Ingredient("Chili powder", 1/2, Unit.TBSP),
        Ingredient("Sea salt", 1, "pinch"),
        Ingredient("Pepper", 1, "pinch"),
        Ingredient("Red pepper flakes", 1, "pinch")
    }, [
        "Preheat an oven to 350 degrees F",
        "Whisk the oil, cumin, garlic powder, chili powder, sea salt, black pepper, and red pepper together in a small bowl; add the chickpeas and toss to coat.",
        "Spread into a single layer on a baking sheet.",
        "Roast for about 45 minutes in the oven, stirring occasionally, until nicely browned and slightly crispy."
    ],
    additional_info="Overall I liked them, but I felt like despite the amount of spice, the flavor didn't really \"soak in\" to the chickpeas.\
    Apparently some people bake at 400 for 40 minutes (instead of 350) to make them crunchier.\
    Maybe too much cumin?\
    But at the same time I wonder if it would be a good idea to let the spices (after being coated) soak in a little more before baking?\
    Apparently it is actually a good idea not to add the olive oil until partway through baking (and probably spices too). I should try that.\
    Also - before putting in the oven originally, should rinse the beans and pat them dry.",
    based_on_link="https://www.allrecipes.com/recipe/197683/simple-roasted-chickpea-snack")


def __make_breads():
    __make_recipe("Banana oat bread", {
        "bananas": "3",
        "rolled oats": "1 cup",
        "flour": "1 cup",
        "flaxseed meal": "1/4 cup",
        "eggs": "2",
        "olive oil": "1/4 cup",
        "milk": "1/4 cup",
        "margarine": "1/4 cup",
        "brown sugar": "1/2 cup",
        "walnuts": "1/2 cup",
        "vanilla": "1 tsp",
        "cinnamon": "1 tsp",
        "baking soda" :"1 tsp",
        "nutmeg": "1/2 tsp",
        "salt": "1/2 tsp"    
    }, [
        "Preheat oven to 350 degrees F (175 degrees C). Grease a 9x5-inch loaf pan and set aside.",
        "Beat together the oil, sugar, eggs, and vanilla.",
        "Add all dry ingredients, alternating with bananas and milk.", 
        "Fold in walnuts/chocolate chips and pour into prepared pan. Bake for 55 minutes."
    ],
    based_on_link="http://allrecipes.com/Recipe/Banana-Oatmeal-Bread/",
    additional_info="Variation on this per Molly Kate's wishes: reducing sugar to 1/4 cup and adding 1/2 cup chocolate chips")

    __make_recipe("Cranberry walnut bread", {
        "Cranberries/raisins": "1/2 cup",
        "Flour": "2 cups",
        "Eggs": 1,
        "Olive oil": "2 tbsp",
        "Milk": "3/4 cup",
        "Brown sugar": "5/8 cup",
        "Walnuts": "1/2 cup",
        "Salt": "1/2 tsp",
        "Baking soda": "1/2 tsp",
        "Baking powder": "3/2 tsp",
        "Cinnamon": "A few sprinkles",
        "Nutmeg": "One sprinkle or so"
    }, [
        "Combine dry, add wet",
        "Sprinkle a few oats/berries on top (can reserve 1/4c of the 1/2c of berries/raisins for the top)",
        "Bake at 350 for 45 minutes"
    ])

    __make_recipe("Pumpkin bread", {
        "Pumpkin puree": "1 cup",
        "Flour": "1.75 cups - note - haven't tried with gf flour apparently? not sure if that's still true",
        "Eggs": "2",
        "Canola oil": "1/3 cup",
        "Milk (or water)": "1/4 cup",
        "Maple syrup": "1/2 cup",
        "Walnuts": "1/3 cup",
        "Salt": "1/2 tsp",
        "Baking soda": "1/2 tsp",
        "Cinnamon": "1 tsp",
        "Nutmeg": "1/4 tsp (suggested: move to 1/2 tsp maybe and add ginger or pumpkin pie spice or something",
        "Vanilla extract": "1 tsp"
    }, [
        "Preheat oven to 325",
        "Beat together oil, syrup, eggs",
        "Stir in pumpkin and vanilla, then all dry",
        "Stir in the water and mix well",
        "Bake for 60-65 minutes"
    ],
    based_on_link="http://cookieandkate.com/2011/whole-wheat-pumpkin-bread/")

    __make_recipe("Apple bread", {
        "Apples": "2",
        "Buckwheat flour": "2/3 cup", 
        "Sorghum flour": "2/3 cup",
        "Tapioca starch": "1/3 cup",
        "Walnuts": "1/2 cup",
        "Baking soda": "1 tsp",
        "Cinnamon": "1 tsp",
        "Salt": "1/4 tsp",
        "Unsweetened applesauce": "1/2 cup",
        "Canola oil": "2 tbsp",
        "Milk": "2 tbsp",
        "Sugar": "1/2 cup",
        "Egg": 1,
        "Vanilla extract": "1 tsp"
    }, [
        "Preheat oven to 350F and lightly coat a 9x5 loaf pan with baking spray.",
        "In a large mixing bowl, combine flour, baking soda, cinnamon, and salt. Separately, mix all wet ingredients + sugar.",
        "Add wet to dry. Fold in apples and walnuts.",
        "Pour batter into loaf pan. Bake for 45 minutes."
    ],
    based_on_link="https://www.wellplated.com/apple-bread/")


def __make_breakfast():
    __make_recipe("Berry-oatmeal bake", {
        # for the oatmeal
        "Unsalted butter": "2 tbsp",
        "Rolled oats": "5/4 cups",
        "Brown sugar": "2 tbsp", 
        "Salt": "A pinch",
        "Unsweetened almond milk": "5/3 cups",
        "Egg": "1 (large)",
        "vanilla extract": "1 tsp",

        # for the topping
        "Mixed berries": "12 oz frozen (5/2 cups frozen; 3/2 cups thawed)",
        "Sliced almonds or pecans": "1/3 cup",
        "Old-fashioned rolled oats": "1/3 cup",
        "Light brown sugar": "1/3 cup",
        "Unsalted butter, melted": "2 tbsp",
        "Gf flour": "1 tbsp",
        "Ground cinnamon": "1/8 tsp",
        "Salt": "A pinch"
    }, [
        "Preheat the oven to 350 degrees F. Grease a 2-quart baking dish or 8-inch square baking pan with the butter.",
        "For the oatmeal: Stir together the oats, sugar and 1/8 teaspoon salt in a large bowl. Whisk together the almond milk, egg, vanilla and almond extract in a medium bowl.\
         Pour the milk mixture into the oat mixture and stir well to combine.",
        "For the topping: Stir together the almonds, oats, sugar, butter, flour, cinnamon and 1/8 teaspoon salt in a medium bowl until evenly combined.",
        "To assemble: Pour the oatmeal into the prepared baking dish. Arrange the berries (including any juices) over the oatmeal. Sprinkle with the topping.\
         Bake until lightly browned and just set, about 50 minutes. Let cool on a rack for 10 to 15 minutes. Serve warm with a dollop of yogurt or a splash of milk if using."
    ],
    based_on_link="https://www.foodnetwork.com/recipes/food-network-kitchen/berry-oatmeal-bake-3362604")

    __make_recipe("Pumpkin Oat Pancakes", {
        "Pumpkin puree": "1 cup (or 3/4 cup, finishing off a can, and add 1/8 cup milk or something)",
        "Milk of choice": "1/4 cup",
        "Coconut oil (or butter), melted": "2 tbsp",
        "Lemon juice": "1 tbsp",
        'Maple syrup (or honey)': '1 tsp',
        'Vanilla extract': '1 tsp',
        "Eggs": "2",
        "Sorghum flour": "1 cup",
        "Baking soda": "1/2 tsp",
        "Salt": "1/2 tsp",
        "Ground cinnamon": "1/2 tsp",
        "Ground ginger": "1/2 tsp",
        "Ground nutmeg": "1/4 tsp",
        "Ground cloves or allspice": "1/4 tsp"
    }, [
        "In a small mixing bowl, stir together the pumpkin puree, milk, coconut oil, lemon juice, maple syrup and vanilla. Beat in the eggs. \
         (If your coconut oil goes back to its solid state like mine did at this point, just warm the mixture for short 20 second bursts in the microwave, \
         stirring between each, until it is melted again.)",
        "In a medium bowl, whisk together the flour, baking soda, salt and spices.",
        "Form a well in the center of the dry ingredients and pour in the wet ingredients. With a big spoon, stir just until the dry ingredients are thoroughly moistened.\
         Do not overmix! Let the batter sit for 10 minutes.",
        "Heat a heavy cast iron skillet/non-stick pan over medium-low heat, or heat an electric griddle to 350 degrees Fahrenheit. \
         Lightly oil the surface of your pan with coconut oil, butter or cooking spray.",
        "Once the surface of the pan is hot enough that a drop of water sizzles on it, pour ¼ cup of batter onto the pan. \
         Let the pancake cook for about 3 minutes, until bubbles begin to form around the edges of the cake.",
        "Once the underside is lightly golden, flip it with a spatula and cook for another 90 seconds or so, until golden brown on both sides. \
         You may need to adjust the heat up or down at this point.",
        "Serve the pancakes immediately or keep warm in a 200 degree Fahrenheit oven."
    ],
    based_on_link="https://cookieandkate.com/pumpkin-oat-pancakes/")