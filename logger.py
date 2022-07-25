import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#Formating
bot_name = Style.BRIGHT+"[Leveler]"

#Functions

#Erorr printing
def printError(errorMsg):
    print(bot_name +" " +Fore.RED +errorMsg)

#Log printing
def printWarning(warningMsg):
    print(bot_name +" " +Fore.YELLOW +warningMsg)
    
#Success printing
def printSuccess(successMsg):
    print(bot_name +" " +Fore.GREEN +successMsg)

#Success printing
def printLog(logMsg):
    print(bot_name +" " +Fore.LIGHTWHITE_EX +logMsg)
