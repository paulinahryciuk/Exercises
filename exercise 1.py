## https://www.practicepython.org/exercise/2014/01/29/01-character-input.html ##

#1
imie = input("jak masz na imie?")
wiek = int(input ("ile masz lat?"))
import datetime
x = datetime.datetime.now()
rok_now = int(x.strftime("%Y"))
#print(rok_now)
sto_lat = rok_now + (100 - wiek )
print( f"{imie} bedziesz miela 100 lat w roku {sto_lat}")


