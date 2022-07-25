from config import lol_folder_location
from logger import *
import subprocess
import time
import keyboard
import mouse

def launchLeagueClient():
    try:    
        subprocess.call(lol_folder_location)#+"LeagueClient.Exe")
    except Exception:
        printError("Can't launch League. Check if you provided correct league location in config.py")
        printError("Change it and relaunch main.py")
def loginInto():
     time.sleep(3)
     keyboard.write("")
     keyboard.press_and_release('tab')
     time.sleep(1)
     keyboard.write("")
     keyboard.press_and_release('enter')
     time.sleep(20)
     


def loginFirstTime():
    loginInto()
    time.sleep(20)
    #Move to scroll ToS
    mouse.move(1207,219)
    time.sleep(2)
    mouse.wheel(-600)
    #Move to accept it
    mouse.move(893, 827)
    time.sleep(1)
    mouse.click('left')
    time.sleep(1)
    #Move to login button
    mouse.move(394, 915)
    mouse.click('left')
    time.sleep(10)
    #Accepting Code of Coduct
    #First
    mouse.move(1362, 325)
    mouse.click('left')
    time.sleep(1)
    #Second
    mouse.move(1364, 468)
    mouse.click('left')
    time.sleep(1)
    #Third
    mouse.move(1369, 597)
    mouse.click('left')
    time.sleep(1)
    #Fourth
    mouse.move(1367, 742)
    mouse.click('left')
    time.sleep(1)
    #Click "I'm in" button
    mouse.move(968, 911)
    mouse.click('left')
    time.sleep(1)
    #Insert nickname
    mouse.move(962, 517)
    mouse.click('left')
    time.sleep(1)
    keyboard.write("nick2138test")
    #Click "Start now" buton
    mouse.move(974, 902)
    time.sleep(5)
    mouse.click('left')
    time.sleep(1)
    #Select summoners rift button
    mouse.move(967, 497)
    time.sleep(5)
    mouse.click('left')

def createLobby():
    #Play button
    mouse.move(328, 113)
    time.sleep(5)
    mouse.click('left')
    #Select COOP VS ALL
    mouse.move(365, 195)
    time.sleep(5)
    mouse.click('left')
    #Select Intro
    mouse.move(735, 682)
    time.sleep(5)
    mouse.click('left')
    # Confirm button click
    mouse.move(824, 928)
    time.sleep(5)
    mouse.click('left')
    #Join to queue
    time.sleep(5)
    mouse.click('left')