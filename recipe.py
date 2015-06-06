#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import codecs
import os

# Data is defined HERE
three_recipes={
    1:('オムライス', 'http://cookpad.com/recipe/2653946'),
    2:('親子丼',     'http://cookpad.com/recipe/2657882'),
    3:('杏仁豆腐',   'http://cookpad.com/recipe/2654398')
  }

def printRecipe(recipe_id, recipe_name, recipe_url):
  print str(recipe_id)+': '+ recipe_name + ' ' + recipe_url

def searchRecipeById(recipe_id):
  searched_recipe_name, searched_recipe_url = three_recipes[recipe_id]
  printRecipe(recipe_id, searched_recipe_name, searched_recipe_url)

def printAllRecipes():
  for recipe_id, (recipe_name, recipe_url) in three_recipes.items():
    printRecipe(recipe_id, recipe_name, recipe_url)

if len(sys.argv) == 2:
  # Case: ID is given
  searchRecipeById(int(sys.argv[1])) # assume that ID is correctly given
else:
  # Case: Normal output
  printAllRecipes()
