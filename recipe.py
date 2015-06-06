#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import codecs
import os

three_recipes2txtfile=open(sys.argv[1],'w')
#three_recipes2txtfile=codecs.open(os.path.dirname(os.path.abspath(__file__))+'/three-recipes.txt','w')
three_recipes2txtfile.write('オムライス'+'\n')
three_recipes2txtfile.write('親子丼'+'\n')
three_recipes2txtfile.write('杏仁豆腐'+'\n')
three_recipes2txtfile.close()
