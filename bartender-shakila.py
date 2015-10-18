"Home work assignments:

  * Read PEP8 guidelines
  * variables_like_this not notLikeThis
  * Docstrings!

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


def getmychoice():
	print('type y/yes or n/No')
	mychoice = {}
	for taste, question in QUESTIONS.items():
        	customerInput = raw_input(question + ' ') 
		if customerInput in ('y','yes'):
			userInput = True
		elif customerInput in ('n','no'):
			userInput = False
        	mychoice[taste] = userInput
	print mychoice
	return mychoice


def getMyDrinkIngredients(preferenceInput):
	drinkIngredients = {}
	ingredientInput = ()

	for taste in INGREDIENTS:
		if preferenceInput[taste]:
			ingredientInput = INGREDIENTS[taste]
                	drinkIngredients[taste] = random.choice(ingredientInput)

        print drinkIngredients

	return drinkIngredients


if __name__ == '__main__':
    getTasteChoice = {}
    getDrinkIngredients = {}
    getTasteChoice = getmychoice()
