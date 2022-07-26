import imp
logger = imp.load_source('logger', '.\logger.py')
import requests
from requests.structures import CaseInsensitiveDict
from time import time, sleep
import random
import string

def getDomains():
    #Thank you guys for your Api <3
    url = "https://api.mail.tm/domains"
    resp = requests.get(url).json()

    numberOfSites =int(resp['hydra:totalItems'])
    sitesList = []
    for i in range(0,numberOfSites,1):
        domain = resp['hydra:member'][i]['domain']
        sitesList.insert(i,domain)
    return sitesList

def createEmail(nick):
    sitesList = getDomains()
    address = nick +"@" +random.choice(sitesList)
    password= output_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
    
    data = {
    "address": address,
    "password": password}

    url = "https://api.mail.tm/accounts"
    response = requests.post(url, json=data)
    print("Status Code", response.status_code)
    print("JSON Response ", response.json())