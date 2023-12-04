## https://www.practicepython.org/exercise/2014/01/29/01-character-input.html ##

#1
# imie = input("jak masz na imie?")
# wiek = int(input ("ile masz lat?"))
# import datetime
# x = datetime.datetime.now()
# rok_now = int(x.strftime("%Y"))
# #print(rok_now)
# sto_lat = rok_now + (100 - wiek )
# print( f"{imie} bedziesz miela 100 lat w roku {sto_lat}")


#2
# number = int(input("Podaj liczbe: "))
# if number%2 == 0:
#     print (f"Liczba {number} jest parzysta.")
# else:
#     print(f"Liczba {number} jest nieparzysta.")

#3
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# wynik = []
# for n in a:
#     if n < 5:
#         wynik.append(n)
# print( f"Liczby z listy mniejsze niz 5 to : {wynik}")

#4
# liczba = int(input( " podaj liczbe: "))
# lista = []
# for n in range (1,liczba+1):
#     if liczba % n == 0:
#         lista.append(n)
# print(f"Dzielniki liczby {liczba} to : {lista}")

#5
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# a_set = set(a)
# b_set = set(b)
# c_set = a_set&b_set
# nowa_lista = list(c_set)
# print(nowa_lista)

#6
# znaki = input("podaj ciag znakow ")
# znaki_rev = znaki[-1::-1]
# # print(znaki_rev)
# if znaki==znaki_rev:
#     print("twoj ciag jest palindromem")
# else:
#     print("twoj ciag nie jest palindromem")

#7
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new =