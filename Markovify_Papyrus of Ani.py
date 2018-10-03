# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:22:29 2018

@author: ewitt4
"""

import markovify

#with open ("Papyrus of Ani.txt") as textfile:
#    ani = textfile.read()
#    
#print ani
    
#ani_model = markovify.Text(ani)

#for i in range(3):
 #   print ani_model.make_sentence()
  #  print " "

with open ("Papyrus of Ani.txt") as textfile:
    ani = textfile.read()

with open ("Precepts of the prefect the lord Ptah-hotep.txt") as textfile:
    precepts = textfile.read()
    
ani_model = markovify.Text(ani)

precepts_model = markovify.Text(precepts)

synthesized_model = markovify.combine([ani_model, precepts_model], [1,1])

print synthesized_model.make_sentence()
 