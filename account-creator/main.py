"""
koncept:

wybierz serwer

wygeneruj nick
sprawdz czy juz go nie wygenerowałeś
sprawdz czy go na tym serwerze juz nie ma

jesli wszystko jest ok

uworz email

utworz konto w riocie

zapisz do bazy

"""
from checkAvability import checkNickAvability, checkFile 
from nickGenerator import generateRandomName
from emailGenerator import createEmail
nick = generateRandomName()
server = "eune" #todo in selectServer
checkFile(nick)
status = checkNickAvability(server,nick)

if status == 0:
    createEmail(nick)

