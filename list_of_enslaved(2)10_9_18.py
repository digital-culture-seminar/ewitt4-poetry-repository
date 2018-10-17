# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 20:46:49 2018

@author: ewitt4
"""
import random

list_of_list = [
        ["Big George", "45", "Sugar-Maker"], 
        ["Lovelace", "30", "Ploughman"],
        ["Louis", "30", "Cook"],
        ["Lawson", "35", "Cooper"],
        ["James", "35", "mason"],
        ["Phillip", "50", "Field Hand"],
        ["Ben", "60", "Blackamith"],
        ["Edward", "9", "Orphan"],
        ["Eliza", "50", "Ironer"],
        ["Etienne", "53", "Foreman"],
        ["Mingo", "18", "Fieldhand"],
        ["Lucille", "26", "Fieldhand"],
        ["Marie Gally", "22", "Domestic"],
        ["Marianne", "30", "Cook"],
        ["Celeste", "16", "Fieldhand"],
        ["James", "48", "glazier"],
        ["Louisa", "35", "Hospital Worker"],
        ["Caroline", "38", "Babymaker"],
        ["Johnette", "35", "Cook"],
        ["Elmira", "25", "Sickly"],
        ["Peggy", "30", "Good Hand"]
        ]

enslaved = random.choice(list_of_list)

#enslaved = list_of_list[random.randint(0,20)]

name = enslaved[0]
age = enslaved[1]
occupation = enslaved[2]

print name + " " +age + " " + occupation

#for characteristic in enslaved:
#    print characteristic