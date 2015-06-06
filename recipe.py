#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import codecs
import os



three_recipes2txtfile=open(sys.argv[1],'w')
#three_recipes2txtfile=codecs.open(os.path.dirname(os.path.abspath(__file__))+'/three-recipes.txt','w')
three_recipes={1:'オムライス',2:'親子丼',3:'杏仁豆腐'}
for recipe_key, recipe_name in three_recipes.items():
  three_recipes2txtfile.write(str(recipe_key)+': '+ recipe_name +'\n')  
three_recipes2txtfile.close()
