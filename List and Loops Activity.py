# -*- coding: utf-8 -*-
"""
Author: Erika Witt
Description: python text generator
License: GNU General Public License v2
"""

import random

random.seed()

#list of nouns
nouns = ["alien", "star", "planet", "comet", "constellation"]

#list of verbs
verbs = ["shoots", "shines", "stands still", "dreams"]

#list of adjectives
adjectives = ["beautiful", "sparkling", "dazzling", "ancient"]

noun = random.choice(nouns)

verb =random.choice(verbs)

adjective = random.choice(adjectives)
second_adjective = random.choice(adjectives)


#word poem
print "The " + adjective + " " + noun + " "
#for Loop to iterate through verbs
i = 1
for verb in verbs:
    whitespace = " " * i
    print whitespace + verb
    i = i + 1
    
#i = 0
#for verb in verbs:
#    print verb 
    
    
    
# concateration
#print "The " + adjective + ", " + second_adjective + " " + noun + " " + verb + "."
#
##string formatting
#print "The {adj} {n} {v}".format(adj=adjective, n=noun, v=verb)


#i = 0
#for noun in nouns:
#    print nouns[i]
#    i = i + 1
    
    
