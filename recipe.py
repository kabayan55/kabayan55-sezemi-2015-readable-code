#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import codecs
import os

recipe_data_txtfile=codecs.open(os.path.dirname(os.path.abspath(__file__))+'/receipe_data.txt','w')
recipe_data_txtfile.write('オムライス'+'\n')
recipe_data_txtfile.close()
