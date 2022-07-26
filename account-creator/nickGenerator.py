#Nick must be 3-16 characters long
import imp
from random import *
logger = imp.load_source('logger', '.\logger.py')
from logger import printError, printLog, printSuccess
config = imp.load_source('config', '.\config.py')
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

def generateRandomName():
   nickname = ""
   for x in range(0,nickname_partials,1):
        x = choice(strings)
        nickname += x
   if(len(nickname)<4):
     printLog("Nick too short. Adding more partials...")
     x = choice(strings)
     nickname += x
   if(len(nickname)>15):
     printError("Nick too long. Triming...")
     nickname= nickname[:15]
   printSuccess("Nick: " +nickname)
   return nickname
