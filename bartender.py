'''
This program takes the y/n input for strong/salty/bitter/sweet/fruity
and picks the random ingredients for each added flavor and makes 
the drink
'''



import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
     }

ingredients = {
    "strong":["glug of rum", "slug of whisky", "splash of gin"],
    "salty":["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter":["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet":["sugar cube", "spoonful of honey","spash of cola"],
    "fruity":["slice of orange","dash of cassis","cherry on top"]
      }

def drink_ingredients():
    drink_ingrd = {}
    print ('Enter "Y" or "Yes" or "N" or "No"')
    strongip = raw_input('strong').lower()
    #print strongip
    if strongip == ('y' or 'yes'):
       drink_ingrd["strong"] = True
    else:
        drink_ingrd["strong"] = False
    

    #print drink_ingrd
    saltyip = raw_input('salty').lower()
    if saltyip == ('y' or 'yes'):
         drink_ingrd['salty'] = True
    else:
         drink_ingrd['salty'] = False


    bitterip = raw_input('bitter').lower()
    if bitterip == ('y' or 'yes'):
         drink_ingrd['bitter'] = True
    else:
         drink_ingrd['bitter'] = False


    sweetip = raw_input('sweet').lower()
    if sweetip == ('y' or 'yes'):
         drink_ingrd['sweet'] = True
    else:
          drink_ingrd['sweet'] = False
    #print drink_ingrd
     
    fruityip = raw_input('fruity').lower()
    if fruityip == ('y' or 'yes'):
         drink_ingrd['fruity'] = True
    else:
         drink_ingrd['fruity'] = False
    print drink_ingrd
    return drink_ingrd


def make_drink(preference):
    drink = {}
    if preference['strong'] == True:
        drink['strong'] = (random.choice(ingredients['strong']))
    if preference['salty'] == True:
        drink['salty'] = (random.choice(ingredients['salty']))
    if preference['bitter'] == True:
        drink['bitter'] = (random.choice(ingredients['bitter']))
    if preference['sweet'] == True:
            drink['sweet'] = (random.choice(ingredients['sweet']))
    if preference['fruity'] == True:
            drink['fruity'] = (random.choice(ingredients['fruity']))
    #print(drink)
    return drink

if __name__ == '__main__':
      choices = {}
      got_drink = {}
      choices = drink_ingredients()
      #print choices
      got_drink = make_drink(choices)
      print(got_drink)



