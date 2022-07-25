import imp
logger = imp.load_source('logger', '.\logger.py')
import requests
from requests.structures import CaseInsensitiveDict
from time import time, sleep

def checkNickAvability(server,nickname):
    sleep(2)
    #Thanks to creators of this site <3
    url = "https://api.nameslol.com/"+server+"/summoner/"+nickname

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    resp = requests.get(url, headers=headers).json()

    if('message') in resp: 
        
        if(resp["message"] == "Summoner by name '"+nickname+"' was not found"):
            
            logger.printSuccess(nickname +" was never registered.")
            return 0 # clean nick, 0 problems
    
    else:
        
        logger.printLog(nickname +" was already registered. Checking it's status...")
        sleep(1)
        
        avabilityTime = resp["availabilityDate"]
        timeNow = int(time() * 1000)
        
        if(avabilityTime>timeNow):
            
            logger.printError(nickname +" is in use.")
            return 1 #nick is used, generate new
        
        else:
            logger.printWarning(nickname +" is probably available. Might be permabanned as well.")
            return 2 #nick was used in past, might be permabanned, cuz riot doesnt clear nicks after permas