# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 19:55:10 2018

@author: ewitt4
"""

# import libraries
#from playsound import playsound
#from gtts import gTTS

# text to speech
#tts = gTTS(text="Hello world", lang="en")

# write audio file
#tts.save("hello-world.mp3")

# play audio file
#playsound("hello-world.mp3")

#----

# import libraries
from playsound import playsound
from gtts import gTTS
import markovify

# get raw text as string
with open("List of Enslaved.txt") as f:
    text = f.read()

# build the markov model
text_model = markovify.NewlineText(text)

# print a randomly-generated sentence of no more than 140 characters
markov_poem = text_model.make_short_sentence(140) 

# text to speech
tts = gTTS(text=markov_poem, lang='en')

# write audio file
tts.save("markovified-poem10.mp3")

# play audio file
playsound("markovified-poem10.mp3")