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
import checkAvability

status = checkAvability.checkNickAvability("Eune","Bubblelift")
print(status)
