#Nick must be 3-16 characters long
from random import *
from config import nickname_partials
import string
import sys
import os

"""
#------# Nick Generator #------#

Nick generator uses random partials to combine nick.

"""

file = open(os.path.join(sys.path[0], "nickPartials.txt"),"r+")
strings = file.read().split('\n')

def generateRandomName(strings):
   nickname = ""
   for x in range(0,nickname_partials,1):
        x = choice(strings)
        nickname += x
   print(nickname)

   if(len(nickname)<4):
    x = choice(strings)
    nickname += x

   if(len(nickname)>15):
    print("Wiecej niz 15")
    nickname= nickname[:15]
    print(nickname)


generateRandomName(strings)