# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 19:22:29 2018

@author: ewitt4
"""

import markovify

with open ("Papyrus of Ani.txt") as textfile:
    ani = textfile.read()
    
#print ani
#    
#ani_model = markovify.Text(ani)
#
#for i in range(3):
#    print ani_model.make_sentence()
#    print " "

with open ("Papyrus of Ani.txt") as textfile:
    ani = textfile.read()

with open ("Precepts of the prefect the lord Ptah-hotep.txt") as textfile:
    precepts = textfile.read()
    
ani_model = markovify.Text(ani)

precepts_model = markovify.Text(precepts)

synthesized_model = markovify.combine([ani_model, precepts_model], [1,1])

poem = synthesized_model.make_sentence()
 

#randomly generate a sentence of no more than 140 characters
my_list = []
for i in range (0,5):
    my_list.append(synthesized_model.make_short_sentence(140))
    print my_list

#mylist + []
#for i in range(1,10):
#    mylist.append("hello world" +s)
#    print mylist
#    print mylist[i]      


#poem = "hello world"
#  
#print poem
#
#with open("poem.md", "w") as p:
#     for i in range(1,10):
#         poem = synthesized_model.make_short_sentence(140)
#         print poem
#         p.write(poem)
#         p.write("\n")
#         
         
#    p.write("""
##  ## Title
##  ```
##  {poem}
##  """.format(poem=poem))
##    p.write("## Title")
##    p.write("\n")        
##    p.write("```")
##    p.write("\n") 
##    p.write(poem)
##    p.write("\n")
##    p.write("```")