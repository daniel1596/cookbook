from typing import List

from py.database.Ingredients import *
from py.database.Models import *
from py.database.Setup import reset_data, session
from py.database.Unit import Unit

""" 
New way of doing things - importing the session from Setup and not using the lovely contextmanager. At least, for now.
"""

def __make_recipe(name: str, ingredients: List[Ingredient], steps_description: List[str], *, based_on_link: str = "", additional_info: str = ""):
    steps = [Step(StepOrder=i, Description=description) for i, description in enumerate(steps_description)]

    recipe = Recipe(Name=name, Steps=steps, Ingredients=ingredients, BasedOnLink=based_on_link, AdditionalInfo=additional_info)

    session.add(recipe)
    session.commit()


def insert_all():
    reset_data()
    __make_bean_based()
    __make_breads()
    __make_breakfast()
    __make_casseroles()
    __make_desserts()
    __make_dips()
    __make_granola()

    """
    Haven't made yet:
    - granola/trail mix (in progress)
    - meats (not sure if I'll add all these but we'll see)
    - pasta 
    - rice
    - smoothies
    - soups
    """
    __make_salads()


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
        Ingredient("Paprika/cayenne", None, "A bit of"),
        Ingredient("Egg", 1, ""),
        Ingredient("Oil (for sauteeing)", 3, Unit.TBSP, does_scale=False)
    ], [
        "Heat up the quinoa (bring to boil, simmer for 15-20 minutes)",
        "Mash the beans with a fork",
        "Mix all dry ingredients + egg",
        "Form the mixture into about 5 patties",
        "Cook the patties in the oil in a large skillet for a few minutes per side."
    ],
    additional_info="These save fine a couple days, at least, in the fridge.",
    based_on_link="https,//www.allrecipes.com/recipe/220661/quinoa-black-bean-burgers/")

    __make_recipe("Mexican bean salad", [
        Ingredient("Canned beans (Simple Truth organic three-bean)", 2, "cans"),
        Ingredient("Green bell pepper, diced", 1, ""),
        Ingredient("Onion, diced", 1, ""),
        Ingredient("Corn, frozen", 10, Unit.DRY_OZ),
        Ingredient("Diced tomatoes, canned", 14.5, Unit.DRY_OZ),
        Ingredient("Olive oil", 1/4, Unit.CUP),
        Cilantro(1/4, Unit.CUP, is_fresh=False),
        Ingredient("Apple cider vinegar", 3, Unit.TBSP),
        Ingredient("Lime juice", 2, Unit.TBSP),
        Ingredient("Lemon juice", 1, Unit.TBSP),
        Ingredient("Cumin, ground", 2, Unit.TSP),
        Ingredient("Dried minced garlic", 1, Unit.TSP),
        Ingredient("Sugar", 1, Unit.TSP),
        Ingredient("Salt", 1, Unit.TSP),
        Ingredient("Cayenne pepper", 1/2, Unit.TSP),
        Ingredient("Black pepper", None, "A few sprinkles"),
    ], [
        "Dice bell pepper and onion. Drain beans and diced tomatoes. Heat up frozen corn.",
        "Mix these ingredients (top half of the list) together in a large bowl.",
        "Mix the lower half of the ingredients (wet + spices/herbs) together in a small bowl.",
        "Pour wet over dry and stir."
    ],
    based_on_link="http,//allrecipes.com/recipe/14169/mexican-bean-salad/")

    __make_recipe("Roasted chickpeas", [
        Ingredient("Chickpeas", 2, Unit.CUP),
        Ingredient("Olive oil", 2, Unit.TBSP),
        Ingredient("Ground cumin", 1, Unit.TBSP),
        Ingredient("Garlic powder", 1, Unit.TBSP),
        Ingredient("Chili powder", 1/2, Unit.TBSP),
        Ingredient("Sea salt", 1, "pinch", does_scale=False),
        Ingredient("Pepper", 1, "pinch", does_scale=False),
        Ingredient("Red pepper flakes", 1, "pinch", does_scale=False)
    ], [
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
    based_on_link="https,//www.allrecipes.com/recipe/197683/simple-roasted-chickpea-snack")


def __make_breads():
    __make_recipe("Banana oat bread", [
        Ingredient("bananas", 3),
        Ingredient("rolled oats", 1, Unit.CUP),
        Ingredient("flour", 1, Unit.CUP),
        Ingredient("flaxseed meal", 1/4, Unit.CUP),
        Ingredient("eggs", 2),
        Ingredient("olive oil", 1/4, Unit.CUP),
        Ingredient("milk", 1/4, Unit.CUP),
        Ingredient("margarine", 1/4, Unit.CUP),
        Ingredient("brown sugar", 1/2, Unit.CUP),
        Ingredient("walnuts", 1/2, Unit.CUP),
        Ingredient("vanilla", 1, Unit.TSP),
        Ingredient("cinnamon", 1, Unit.TSP),
        Ingredient("baking soda" ,1, Unit.TSP),
        Ingredient("nutmeg", 1/2, Unit.TSP),
        Ingredient("salt", 1/2, Unit.TSP)
    ], [
        "Preheat oven to 350 degrees F (175 degrees C). Grease a 9x5-inch loaf pan and set aside.",
        "Beat together the oil, sugar, eggs, and vanilla.",
        "Add all dry ingredients, alternating with bananas and milk.",
        "Fold in walnuts/chocolate chips and pour into prepared pan. Bake for 55 minutes."
    ],
    based_on_link="http,//allrecipes.com/Recipe/Banana-Oatmeal-Bread/",
    additional_info="Variation on this per Molly Kate's wishes, reducing sugar to 1/4 cup and adding 1/2 cup chocolate chips")

    __make_recipe("Cranberry walnut bread", [
        Ingredient("Cranberries/raisins", 1/2, Unit.CUP),
        Ingredient("Flour", 2, Unit.CUP),
        Ingredient("Eggs", 1, ""),
        Ingredient("Olive oil", 2, Unit.TBSP),
        Ingredient("Milk", 3/4, Unit.CUP),
        Ingredient("Brown sugar", 5/8, Unit.CUP),
        Ingredient("Walnuts", 1/2, Unit.CUP),
        Ingredient("Salt", 1/2, Unit.TSP),
        Ingredient("Baking soda", 1/2, Unit.TSP),
        Ingredient("Baking powder", 3/2, Unit.TSP),
        Ingredient("Cinnamon", None, "A few sprinkles"),
        Ingredient("Nutmeg", 1, "sprinkle")
    ], [
        "Combine dry, add wet",
        "Sprinkle a few oats/berries on top (can reserve 1/4c of the 1/2c of berries/raisins for the top)",
        "Bake at 350 for 45 minutes"
    ])

    __make_recipe("Pumpkin bread", [
        Ingredient("Pumpkin puree", 1, Unit.CUP),
        Ingredient("Flour", 1.75, Unit.CUP),
        Ingredient("Eggs", 2),
        Ingredient("Canola oil", 1/3, Unit.CUP),
        Ingredient("Milk (or water)", 1/4, Unit.CUP),
        Ingredient("Maple syrup", 1/2, Unit.CUP),
        Ingredient("Walnuts", 1/3, Unit.CUP),
        Ingredient("Salt", 1/2, Unit.TSP),
        Ingredient("Baking soda", 1/2, Unit.TSP),
        Ingredient("Cinnamon", 1, Unit.TSP),
        Ingredient("Nutmeg", 1/4, Unit.TSP),
        Ingredient("Vanilla extract", 1, Unit.TSP)
    ], [
        "Preheat oven to 325",
        "Beat together oil, syrup, eggs",
        "Stir in pumpkin and vanilla, then all dry",
        "Stir in the water and mix well",
        "Bake for 60-65 minutes"
    ],
    based_on_link="http,//cookieandkate.com/2011/whole-wheat-pumpkin-bread/",
    additional_info="Have not tried this yet with gluten-free flour. Also, should go up to 1/2 tsp nutmeg and maybe ginger or pumpkin pie spice.")

    __make_recipe("Apple bread", [
       Ingredient("Apples", 2),
       Ingredient("Buckwheat flour", 2/3, Unit.CUP),
       Ingredient("Sorghum flour", 2/3, Unit.CUP),
       Ingredient("Tapioca starch", 1/3, Unit.CUP),
       Ingredient("Walnuts", 1/2, Unit.CUP),
       Ingredient("Baking soda", 1, Unit.TSP),
       Ingredient("Cinnamon", 1, Unit.TSP),
       Ingredient("Salt", 1/4, Unit.TSP),
       Ingredient("Unsweetened applesauce", 1/2, Unit.CUP),
       Ingredient("Canola oil", 2, Unit.TBSP),
       Ingredient("Milk", 2, Unit.TBSP),
       Ingredient("Sugar", 1/2, Unit.CUP),
       Ingredient("Egg", 1),
       Ingredient("Vanilla extract", 1, Unit.TSP)
    ], [
        "Preheat oven to 350F and lightly coat a 9x5 loaf pan with baking spray.",
        "In a large mixing bowl, combine flour, baking soda, cinnamon, and salt. Separately, mix all wet ingredients + sugar.",
        "Add wet to dry. Fold in apples and walnuts.",
        "Pour batter into loaf pan. Bake for 45 minutes."
    ],
    based_on_link="https,//www.wellplated.com/apple-bread/")


def __make_breakfast():
    __make_recipe("Berry-oatmeal bake", [
        # for the oatmeal
        Ingredient("Unsalted butter", 2, Unit.TBSP),
        Ingredient("Rolled oats", 5/4, Unit.CUP),
        Ingredient("Brown sugar", 2, Unit.TBSP),
        Ingredient("Salt", 1, "pinch"),
        Ingredient("Unsweetened almond milk", 5/3, Unit.CUP),
        Ingredient("Egg", 1),
        Ingredient("vanilla extract", 1, Unit.TSP),

        # for the topping
        Ingredient("Mixed berries", 12, "oz frozen (5/2 cups frozen; 3/2 cups thawed)"),
        Ingredient("Sliced almonds or pecans", 1/3, Unit.CUP),
        Ingredient("Old-fashioned rolled oats", 1/3, Unit.CUP),
        Ingredient("Light brown sugar", 1/3, Unit.CUP),
        Ingredient("Unsalted butter, melted", 2, Unit.TBSP),
        Ingredient("Gf flour", 1, Unit.TBSP),
        Ingredient("Ground cinnamon", 1/8, Unit.TSP),
        Ingredient("Salt", None, "A pinch")
    ], [
        "Preheat the oven to 350 degrees F. Grease a 2-quart baking dish or 8-inch square baking pan with the butter.",
        "For the oatmeal, Stir together the oats, sugar and 1/8 teaspoon salt in a large bowl. Whisk together the almond milk, egg, vanilla and almond extract in a medium bowl.\
         Pour the milk mixture into the oat mixture and stir well to combine.",
        "For the topping, Stir together the almonds, oats, sugar, butter, flour, cinnamon and 1/8 teaspoon salt in a medium bowl until evenly combined.",
        "To assemble, Pour the oatmeal into the prepared baking dish. Arrange the berries (including any juices) over the oatmeal. Sprinkle with the topping.\
         Bake until lightly browned and just set, about 50 minutes. Let cool on a rack for 10 to 15 minutes. Serve warm with a dollop of yogurt or a splash of milk if using."
    ],
    based_on_link="https,//www.foodnetwork.com/recipes/food-network-kitchen/berry-oatmeal-bake-3362604")

    __make_recipe("Pumpkin oat pancakes", [
        Ingredient("Pumpkin puree", 1, Unit.CUP),
        Ingredient("Milk of choice", 1/4, Unit.CUP),
        Ingredient("Coconut oil (or butter), melted", 2, Unit.TBSP),
        Ingredient("Lemon juice", 1, Unit.TBSP),
        Ingredient('Maple syrup (or honey)', 1, Unit.TSP),
        Ingredient('Vanilla extract', 1, Unit.TSP),
        Ingredient("Eggs", 2),
        Ingredient("Sorghum flour", 1, Unit.CUP),
        Ingredient("Baking soda", 1/2, Unit.TSP),
        Ingredient("Salt", 1/2, Unit.TSP),
        Ingredient("Ground cinnamon", 1/2, Unit.TSP),
        Ingredient("Ground ginger", 1/2, Unit.TSP),
        Ingredient("Ground nutmeg", 1/4, Unit.TSP),
        Ingredient("Ground cloves or allspice", 1/4, Unit.TSP)
    ], [
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
    based_on_link="https,//cookieandkate.com/pumpkin-oat-pancakes/",
    additional_info="Have also done this with 3/4 cup pumpkin puree and 1/8 extra cup of almond milk, and that worked fine.")


def __make_casseroles():
    __make_recipe("Egg casserole", [
        Ingredient("Eggs", 6),
        Ingredient("Cubed/diced ham", 8, Unit.DRY_OZ),
        Ingredient("Shredded cheese (probably any kind - have done Mexican usually)", 1, Unit.CUP),
        Ingredient("Diced potatoes", 1, Unit.CUP),
        Ingredient("Diced onion", 1, Unit.CUP),
        Ingredient("Flour", 1, Unit.TBSP),
        Ingredient("Milk (almond is fine)", 1/2, Unit.CUP),
        Ingredient("Canola oil", 2, Unit.TBSP),
        Ingredient("Italian seasoning", 1, Unit.TSP)
    ], [
        "Mix all dry ingredients together",
        "Spread mixture in 8x8 baking dish (or 9x13 - thinner or thicker, has worked either way)",
        "Pour canola oil over this",
        "Whisk eggs and milk, pour on top",
        "Sprinkle seasoning on top (and cheese - do go over the 1 cup mark suggested here)",
        "Bake uncovered at 350 for 40 minutes"
    ],
    based_on_link="http://pocketchangegourmet.com/ham-and-egg-casserole/")

    __make_recipe("Green bean casserole", [
        Ingredient("Green beans", 4, Unit.CUP),
        Ingredient("Chicken, pre-cooked", 1.5, Unit.CUP),
        Ingredient("Butter", 3, Unit.TBSP),
        Ingredient("Flour", 2, Unit.TBSP),
        Ingredient("Greek yogurt", 5.3, Unit.DRY_OZ),
        Ingredient("Cheddar cheese", 2, Unit.CUP),
        Ingredient("Crumbled crackers", 1/2, Unit.CUP),
        Ingredient("Sugar", 1/4, Unit.TSP),
        Ingredient("Almonds, slivered", 1/4, Unit.CUP),
        Ingredient("Cumin, garlic powder, and pepper", None, "A little"),
    ], [
        "Preheat the oven to 350 F",
        "Cook the chicken in a big pan with spices (I used cumin, garlic powder, and pepper last time - great choices, not too much pepper is needed though)",
        "Sautee the onion in a mixture of flour and 2 (of the 3) tbsp butter",
        "Stir in the salt, sugar, Greek yogurt, and green beans - and maybe include something else next time? (Internet suggests things like lemon juice, ginger, and red pepper flakes)",
        "Once mixed, transfer to a 13x9 pan",
        "Mix together the last tbsp of butter, cracker crumbs, and slivered almonds in a little bowl",
        "Spread this mixture and the cheese on top of the casserole",
        "Bake at 350 for for 30 minutes"
    ],
    based_on_link="http://allrecipes.com/recipe/13717/grandmas-green-bean-casserole/",
    additional_info="Chicken has generally been 1 cup but I'm putting it at 1.5 for the future")

    __make_recipe("Mexican casserole", [
        Ingredient("Ground meat or substitute", 1, Unit.POUND),
        Ingredient("Medium salsa", 3/2, Unit.CUP),
        Ingredient("Tortillas (or crushed-up chips)", None, "enough to fill the pan"),
        Ingredient("Canned beans", 1, Unit.CUP),
        Ingredient("Greek yogurt", 5.3, Unit.DRY_OZ),
        Ingredient("Mexican cheese", 2, Unit.CUP),
        Ingredient("Diced onion", 1/2, "large onion"),
        Ingredient("Tomatoes, diced, fire-roasted", 1, "can"),
        Ingredient("Garlic/powder", None, "several sprinkles (of powder) or a few cloves"),
        Ingredient("Pepper and other spices (last time was: negligable amounts of cumin, Italian seasoning, and cayenne)", None, "as desired")
    ], [
        "Brown the meat in a large pan; drain. If using meat substitute, just add it to the pan.",
        "Add salsa and let simmer",
        "Add beans, onion, and tomato",
        "Layer tortillas (or chips) in the bottom of a 9x13 baking dish",
        "Pour mixture from pan onto tortillas",
        "Spread Greek yogurt on top of that",
        "Spread cheese on the top",
        "Bake at 350 for 30 minutes"
    ],
    additional_info="For next time: could (1) add 2 oz black olives, (2) maybe a bell pepper, (3) any other spices?"
                    "But it also doesn't need a ton of other spices to be tasty - it already has a lot of spices from "
                    "the salsa (mainly) and fire-roasted diced tomatoes.")


def __make_desserts():
    __make_recipe("Oatmeal raisin / chocolate chip cookies", [
        Ingredient("Oats", 3/2, Unit.CUP),
        Ingredient("Flour", 3/4, Unit.CUP),
        Ingredient("Sugar", 1/4, Unit.CUP),
        Ingredient("Butter", 1/2, Unit.CUP),
        Ingredient("Baking soda", 1/2, Unit.TSP),
        Ingredient("Cinnamon", 1/2, Unit.TSP),
        Ingredient("Salt", 1/4, Unit.TSP),
        Ingredient("Vanilla", 1, Unit.TSP),
        Ingredient("Egg", 1),
        Ingredient("Pecans", 1/4, Unit.CUP),
        Ingredient("Raisins or chocolate chips", 3/4, Unit.CUP)
    ], [
        "Heat oven to 350°F.",
        "In large bowl, stir sugars, butter, baking soda, cinnamon, salt, vanilla and eggs with spoon until well blended.",
        "Stir in oats, flour and raisins.",
        "Place the dough in tablespoonfuls about 2 inches apart on cookie sheets",
        "Bake 9-11 minutes or until golden brown."
    ],
    based_on_link="https://www.bettycrocker.com/recipes/best-whole-wheat-oatmeal-raisin-cookies/8331bf27-c5f8-4f89-8883-90296373b701",
    additional_info="The 3/4 cup raisins/chocolate chips is a suggestion for next time. Taking down the sugar to 1/4 cup made it not as tasty as 1/2 haha.")

    __make_recipe("Cinnamon apple crumb cake", [
        # for the cake
        Ingredient("Butter", 6, Unit.TBSP),
        Ingredient("Sugar", 1/3, Unit.CUP),
        Ingredient("Eggs", 2),
        Ingredient("Vanilla extract", 1, Unit.TSP),
        Cinnamon(1, Unit.TSP),
        Salt(None, "A pinch"),
        Ingredient("Almond flour", 1/2, Unit.CUP),
        Ingredient("Gluten-free baking mix", 1/2, Unit.CUP),
        Ingredient("Coconut flour", 1/3, Unit.CUP),
        Ingredient("Ground flaxseed", 1, Unit.TBSP),
        BakingPowder(2, Unit.TSP),
        AlmondMilk(1/2, Unit.CUP),

        # for the streusel layer
        Butter(3, Unit.TBSP),
        Ingredient("Granny smith apples, peeled and chopped into 1/2 inch pieces", 1, Unit.CUP),
        Sugar(1/4, Unit.CUP),
        Cinnamon(1, Unit.TSP),
        Ingredient("Almond flour", 3/4, Unit.CUP),
        Walnuts(1/4, Unit.CUP),
        Salt(None, "A pinch")
    ], [
        "TO MAKE THE CAKE LAYER:",
        "Cream the butter and sweetener together until smooth and fluffy.",
        "Add the eggs one at a time, beating well after each, then add the vanilla extract.",
        "In a medium-sized bowl, combine the almond flour, coconut flour, cinnamon, baking powder, xanthan gum and salt and mix well.",
        "Add the dry ingredients to the wet ingredients and mix.",
        "Pour in the almond milk and mix until just blended.",
        "Spread the batter into a greased 9×9 baking pan.",
        "TO MAKE THE APPLE STREUSEL LAYER:",
        "Melt the butter in a medium skillet.",
        "Add the apples, cinnamon and sweetener and cook for 2 minutes, stirring the entire time.",
        "Remove from the heat and stir in the almond flour, pinch of salt and chopped walnuts. Stir well until a crumbly dough forms.",
        "Spoon the topping evenly over the cake batter and spread out.",
        "Bake the cake in a 375 degree oven for 35 minutes. If you find the topping getting too brown, cover it loosely with parchment or aluminum foil for the final 10 minutes.",
        "Remove from the oven and cool before slicing into 3 inch squares.",
        "Alternatively, you can bake these in 9 large muffin cups for about 20 minutes at 375 degrees (F) or until a knife inserted in the center comes out clean."
    ],
    based_on_link="https://www.ibreatheimhungry.com/cinnamon-apple-crumb-cake-low-carb/print/16669/",
    additional_info="Eat within 5 days. It didn't have a ton of crumb topping, like an apple crisp would, so be prepared for that")

    __make_recipe("Apple oat cookies", [
        Oats(1, Unit.CUP),
        Ingredient("Flour (1/2c sorghum, 1/8c each flaxseed meal and tapioca starch)", 3/4, Unit.CUP),
        BakingPowder(1/2, Unit.TSP),
        Salt(1/4, Unit.TSP),
        Cinnamon(1/4, Unit.TSP),
        Ingredient("Apple", 1/3, Unit.CUP),
        BrownSugar(1/3, Unit.CUP),
        Ingredient("Walnuts or pecans", 1/4, Unit.CUP),
        Ingredient("Chia seeds", 1, Unit.TBSP),
        Ingredient("Oil/margarine", 1/4, Unit.CUP),
        AlmondMilk(1/4, Unit.CUP)
    ], [
        "Preheat oven to 350F",
        "Mix dry in bowl",
        "Mix wet in tiny bowl and then add to dry.",
        "Mix it all up.",
        "Drop about a tbsp-sized mound of cookie onto a baking sheet.",
        "Bake at 350F for 12-15 minutes or until edges of cookies are slightly browned"
    ],
    additional_info="The amount of sugar is experimental, but 1/2 cup of honey was far too sweet, so this should be decent now.")

    __make_recipe("Pumpkin chocolate chip cookies", [
        CanolaOil(1/2, Unit.CUP),
        BrownSugar(2/3, Unit.CUP),
        Ingredient("Pumpkin puree", 3/4, Unit.CUP),
        Ingredient("Flour (was all-purpose - haven't made gf)", 4/3, Unit.CUP),
        Egg(1),
        Oats(2/3, Unit.CUP),
        ChocolateChips(2/3, Unit.CUP),
        Walnuts(1/4, Unit.CUP),
        Cinnamon(3/4, Unit.TSP),
        Salt(1/4, Unit.TSP),
        BakingSoda(1/4, Unit.TSP),
        BakingPowder(3/4, Unit.TSP)
    ], [
        "Beat oil, brown sugar, pumpkin, eggs together",
        "In separate bowl: mix dry (except chips/walnuts)",
        "Add wet to dry, then chips/walnuts",
        "Drop 1-2 tbsp per cookie onto a baking sheet",
        "Bake at 375F for 10-12 minutes"
    ],
    based_on_link="http://allrecipes.com/Recipe/Pumpkin-Oatmeal-Chocolate-Chip-Cookies",
    additional_info="Add some vanilla extract or maybe nutmeg or pumpkin pie spice if making again")

    __make_recipe("Peach crisp", [
        Ingredient("Peaches", 5, Unit.CUP),
        BrownSugar(1/2, Unit.CUP),
        Ingredient("Flour", 1/4, Unit.CUP),
        CanolaOil(1/4, Unit.CUP),
        RolledOats(1, Unit.CUP),
        Ingredient("Slivered almonds", 1/4, Unit.CUP),
        Cinnamon(1, Unit.TSP)
    ], [
        "In a medium bowl, combine everything but the peaches",
        "Place peach slices in 8x8 dish",
        "Sprinkle topping over peaches",
        "Bake at 375 for 30 minutes"
    ],
    based_on_link="http://allrecipes.com/Recipe/Peach-Crisp-III/",
    additional_info="For next time: Add another 1/4c of oats, use nutmeg, reduce brown sugar to 3/8c, add 2 tbsp flour for 3/8 cup?\
     Haven't tried this with apples or any fruit besides peaches (at least, not yet)")

    __make_recipe("Fruit cobbler", [
        Ingredient("Fruit, frozen", 12, Unit.DRY_OZ),
        Sugar(5/8, Unit.CUP),
        Ingredient("Flour, all-purpose (gf substitute)", 3/4, Unit.CUP),
        Butter(3, Unit.TBSP),
        AlmondMilk(3/4, Unit.CUP),
        Ingredient("Slivered almonds", 1/4, Unit.CUP),
        BakingPowder(1, Unit.TSP),
        Salt(1/4, Unit.TSP)
    ], [
        "Heat oven to 350 degrees",
        "Put butter in an 8-inch square or 9-inch round pan; set in oven to melt. When butter has melted, remove pan from oven.",
        "Whisk flour, sugar, baking powder and salt in small bowl. Add milk; whisk to form a smooth batter.",
        "Pour batter into pan, then scatter fruit over batter.",
        "Sprinkle with remaining 1 Tb. of sugar.",
        "Bake until batter browns and fruit bubbles, 50 to 60 minutes."
    ],
    based_on_link="https://www.allrecipes.com/recipe/88354/easy-batter-fruit-cobbler/",
    additional_info="For next time: Possibly add some oats to the top? And possibly substitute oil for butter?")


def __make_dips():
    __make_recipe("Guacamole", [
        Avocado(3),
        LimeJuice(2, Unit.TBSP),
        Salt(1, Unit.TSP),
        DicedOnion(1/2, Unit.CUP),
        Cilantro(3, Unit.TBSP, is_fresh=True),
        FireRoastedDicedTomatoes(1/2, "can"),
        Ingredient("Minced garlic", 1, Unit.TSP),
        CayennePepper(1, "pinch")
    ], [
        "In a medium bowl, mash together the avocados, lime juice, and salt. Mix in the rest of the ingredients.",
        "Refrigerate 1 hour for best flavor, or serve immediately."
    ],
    based_on_link="https://www.allrecipes.com/recipe/14231/guacamole/",
    additional_info="Need to add 1/2 tsp cumin next time! Based on what other reviewers have said.\
    Had a little too much lime flavor - probably take down salt from 1 tsp --> 1/2 tsp. \
    Didn't use onion in this rendition.")


def __make_granola():
    __make_recipe("Original granola", [
        RolledOats(5/2, Unit.CUP),
        FlaxSeeds(1/2, Unit.CUP),
        PeanutButter(1/4, Unit.CUP),
        Ingredient("Almonds/pecans", 3/4, Unit.CUP),
        OliveOil(1/3, Unit.CUP),
        MapleSyrup(1/3, Unit.CUP),
        Salt(1/2, Unit.TSP),
        Cinnamon(1, Unit.TSP),
        Nutmeg(1/4, Unit.TSP),
        Ginger(1, "pinch"),
        Cloves(1, "pinch"),
    ], [
      "Mix all dry ingredients, then add wet and stir",
      "Bake at 300 for 35ish minutes total",
      "Stir in the pan after about 20 minutes",
      "Use wax paper on the pan!"
    ],
    additional_info="Can also sub in 1/2 cup peanuts for 1/4 cup peanut butter; I've switched to peanut butter lately simply so I can buy organic.")

    __make_recipe("Coconut granola", [
        RolledOats(5/2, Unit.CUP),
        FlaxSeeds(1/4, Unit.CUP),
        Walnuts(1/4, Unit.CUP),
        UnsweetenedCoconutFlakes(1, Unit.CUP),
        Almonds(1/2, Unit.CUP),
        PumpkinSeeds(1/2, Unit.CUP),
        Pecans(3/4, Unit.CUP),
        SunflowerSeeds(1/4, Unit.CUP),
        Salt(1/2, Unit.TSP),
        CoconutOil(1/3, Unit.CUP),
        MapleSyrup(1/3, Unit.CUP),
        AlmondButter(2, Unit.TBSP)
    ], [
        "Preheat oven to 325 degrees F (162 C).",
        "Add all dry (and I added the almond butter, too) to a large mixing bowl and stir to combine.",
        "To a small saucepan, add coconut oil and maple syrup. Warm over medium heat for 2-3 minutes, whisking frequently until the two are \
          totally combined and there is no visible separation.",
        "Immediately pour over the dry ingredients and stir to combine until all oats and nuts are thoroughly coated.",
        "Arrange on a large baking sheet and spread into an even layer.",
        "Bake for 20 minutes, then remove from oven and turn the pan around so the other end goes into the oven first (so it bakes evenly).",
        "Bake 5-7 minutes more, watching carefully as to not let it burn. You'll know it's done when the granola is golden brown and very fragrant."
    ],
    based_on_link="https://minimalistbaker.com/super-chunky-coconut-granola/",
    additional_info="Can also sub in 1/2 cup peanuts for 1/4 cup peanut butter; I've switched to peanut butter lately simply so I can buy organic.")

    # __make_recipe("Premium granola", [
    #
    # ])


def __make_salads():
    __make_recipe("Broccoli salad", [
        Ingredient("Bacon", 10, "slices"),
        Ingredient("Broccoli", 1, "10 oz bag (frozen)"),
        Ingredient("Onion, red or yellow", 1/4, Unit.CUP),
        Ingredient("Raisins", 1/2, Unit.CUP),
        Ingredient("Greek yogurt", 1, Unit.CUP),
        Ingredient("Apple cider vinegar", 3, Unit.TBSP),
        Ingredient("Sugar", 3/2, Unit.TBSP),
        Ingredient("Sunflower seeds/slivered almonds/flaxseeds", 1, Unit.CUP)
    ], [
        "Place bacon in a large, deep skillet. Cook over medium high heat until evenly brown. Drain, crumble and set aside.",
        "In a medium bowl, combine the broccoli, onion and raisins. In a small bowl, whisk together the vinegar, sugar and mayonnaise.\
            Pour over broccoli mixture, and toss until well mixed. Refrigerate for at least two hours.",
        "Before serving, toss salad with crumbled bacon and sunflower seeds."
    ],
    based_on_link="https://www.allrecipes.com/recipe/16098/alysons-broccoli-salad/",
    additional_info="I had written down to sub in 1 tbsp of oil for one of the tbsps of vinegar.\
        (The original recipe called for white wine vinegar, btw).\
        Also note that you may need a big sheet pan or two skillets for the bacon. (I've used a sheet pan.)\
        Also I've wondered before if a tsp of lemon juice or any other spices would help anything. Not sure what we used last time (July 2019).")

    __make_recipe("Chicken salad", [
        Ingredient("Chicken", 9, Unit.DRY_OZ),
        Ingredient("Greek yogurt", 1, Unit.CUP),
        Ingredient("Apple", 1),
        Ingredient("Walnuts", 1, Unit.CUP),
        Ingredient("Cranberries/raisins", 1/3, Unit.CUP),
        Ingredient("Green pepper/onion", 1.5, Unit.CUP),
        Ingredient("Lemon juice", 1, Unit.TSP),
        Ingredient("Salt", 1/2, Unit.TSP),
        Ingredient("Pepper", 1/2, Unit.TSP),
        Ingredient("Paprika (or similar)", 1/2, Unit.TSP)
    ], [
        "Combine ingredients in large mixing bowl and eat."
    ],
    based_on_link="http://allrecipes.com/Recipe/Holiday-Chicken-Salad/",
    additional_info="Have done onion w/o green pepper and green pepper w/o onion, or a little bit of both.\
        Also would be interested in trying this with a meat substitute some time.\
        Haven't tried toasting the walnuts, although that could be fun. Not sure how noticeable though.")

    __make_recipe("Greek salad", [
        Ingredient("Cucumber", 1, "large"),
        Ingredient("Cherry tomatoes", 1, "cup or so?"),
        Ingredient("Onion", 1, "cup or so?"),
        Ingredient("Feta", 4, Unit.DRY_OZ),
        Ingredient("Olive oil", None, "not sure"),
        Basil(None, "ask MK", is_fresh=False),
        Ingredient("Oregano", None, "ask MK")
    ], [
        "Chop up the onion, cherry tomatoes (or regular tomato), and cucumber",
        "Mix together the olive oil and spices",
        "Cut an 8 oz block of feta in half, vertically",
        "Pour olive oil/spice mixture over the feta and serve"
    ])

    """
    Not going to officially put this one in the cookbook yet, but I did make it.
    See notes below, and note that the recipe was halved (8 servings on allrecipes instead of 16).

    https://www.allrecipes.com/recipe/215069/tasteful-tahini-salad-dressing/
    - Put in just a few sprinkles of ground ginger - could have put in more. (Might put in a tad more for the rest of the batch.)
    - Tried not using a blender, probably a mistake since the tahini did not dissolve very quickly hahaha. Not sure if it will at all in the fridge.
    - Used about 2 tsp garlic instead of 
    - Probably dumped in too much apple cider vinegar although I tried not to [PS: don't think this made a big difference

    It's not too bad! At least it is very healthy (primary ingredients are water, organic tahini, and organic EVOO)
    -- Probably my biggest knock against it is that I'm not used to this sort of thing as a salad dressing. 
    - I'm curious if it would be good as a chicken marinade or something like that, or maybe in stir fry? Hmm.
    """


