#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import codecs
import os

# Data is defined HERE
three_recipes={1:'オムライス',2:'親子丼',3:'杏仁豆腐'}

def searchById(recipe_id):
  searched_recipe_name = three_recipes[recipe_id]
  print str(recipe_id)+': '+ searched_recipe_name

def printAllRecipe():
  for recipe_key, recipe_name in three_recipes.items():
    print str(recipe_key)+': '+ recipe_name

if len(sys.argv) == 2:
  # Case: ID is given
  searchById(int(sys.argv[1])) # assume that ID is correctly given
else:
  # Case: Normal output
  printAllRecipe()
