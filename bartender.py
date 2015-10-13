"""This program takes the y/n input for strong/salty/bitter/sweet/fruity
and picks the random ingredients for each added flavor and makes 
the drink

Constants:
    QUESTIONS (dict): --
    INGREDIENTS (dict): --

"""

import random


# CONSTANTS
QUESTIONS = {
             "strong": "Do ye like yer drinks strong?",
             "salty": "Do ye like it with a salty tang?",
             "bitter": "Are ye a lubber who likes it bitter?",
             "sweet": "Would ye like a bit of sweetness with yer poison?",
             "fruity": "Are ye one for a fruity finish?"
            }
INGREDIENTS = {
               "strong": ["glug of rum", "slug of whisky", "splash of gin"],
               "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
               "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
               "sweet": ["sugar cube", "spoonful of honey","spash of cola"],
               "fruity": ["slice of orange","dash of cassis","cherry on top"]
              }


def drink_ingredients():
    """A quick summary on this function.

    Returns:
        dict: A dictionary of an ingredient adjective (from the
            INRGREDIENTS constant) mapped to a yes/no boolean
            representing if the user likes it or not! Example:

            >>> {'salty': False, 'strong': True, 'bitter': True, ...}

    See Also:
        INGREDIENTS: the ingredients constant in this module.
        QUESTIONS: --

    """

    # The ingredients dictionary will be a key>value mapping of
    # the type of ingredient (key) from INGREDIENTS to a true/false
    # boolean value.
    liked_ingredients = {}
    print("Enter Y or YES; N or NO")

    for ingredient_adjective, question in QUESTIONS.items():

        # This loop is for making sure the user supplies a yes or
        # no answer!
        while True:
            user_input = raw_input(question + ' ').lower()

            if user_input in ('y', 'yes'):
                user_likes_ingredient = True
                break
            elif user_input in ('n', 'no'):
                user_likes_ingredient = False
                break

        # finally, add the True/False for liking the ingredient to the
        # liked ingredients dictionary
        liked_ingredients[ingredient_adjective] = user_likes_ingredient
        
    return liked_ingredients


def make_drink(preference):
    """A summary of what this function does.

    Args:
        preference (dict): Maps an "ingredient adjective" (a key
            from the INGREDIENTS constant) to a yes/no boolean
            value designating preference.

    Returns:
        dict: Mapping of ingredient adject from INGREDIENTS (key)
            to a randomly select descriptive
            word from INGREDIENTS (value).

    See Also:
        drink_ingredients(): The return value of this function
            is used to supply "preference" to this function.

    """

    drink = {}

    for ingredient_adjective in INGREDIENTS:

        if preference[ingredient_adjective]:
            ingredient_descriptions = INGREDIENTS[ingredient_adjective]
            drink[ingredient_adjective] = random.choice(ingredient_descriptions)

    return drink


if __name__ == '__main__':
      choices = {}
      got_drink = {}
      choices = drink_ingredients()
      got_drink = make_drink(choices)
      print(got_drink)
