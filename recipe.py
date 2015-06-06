#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import codecs
import os



three_recipes={1:'オムライス',2:'親子丼',3:'杏仁豆腐'}
for recipe_key, recipe_name in three_recipes.items():
  print str(recipe_key)+': '+ recipe_name
