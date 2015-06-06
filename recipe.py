#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import codecs
import os

# Data is defined HERE
three_recipes={1:'オムライス',2:'親子丼',3:'杏仁豆腐'}

def printRecipe(recipe_id, recipe_name):
  print str(recipe_id)+': '+ recipe_name

def searchRecipeById(recipe_id):
  searched_recipe_name = three_recipes[recipe_id]
  printRecipe(recipe_id, searched_recipe_name)

def printAllRecipes():
  for recipe_id, recipe_name in three_recipes.items():
    printRecipe(recipe_id, recipe_name)

if len(sys.argv) == 2:
  # Case: ID is given
  searchRecipeById(int(sys.argv[1])) # assume that ID is correctly given
else:
  # Case: Normal output
  printAllRecipes()
