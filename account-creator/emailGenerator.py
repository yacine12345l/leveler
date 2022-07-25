import imp
logger = imp.load_source('logger', '.\logger.py')
import requests
from requests.structures import CaseInsensitiveDict
from time import time, sleep

#Thank you guys for your Api <3

def getDomains():
    url = "https://api.mail.tm/domains"
    resp = requests.get(url).json()

    numberOfSites =int(resp['hydra:totalItems'])
    sitesList = []
    for i in range(0,numberOfSites,1):

        domain = resp['hydra:member'][i]['domain']
        print(domain)
        sitesList.insert(domain)
    return sitesList

address =""
password=""
data = {
    "address": address,
   "password": password
}

def createEmail():
    url = "https://api.mail.tm/accounts"
    response = requests.post(url, json=data)
    print("Status Code", response.status_code)
    print("JSON Response ", response.json())