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
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# print([a for a in a if a%2 == 0])

#11
# liczba = int(input("podaj liczbe: "))
# dzielniki = []

# def jest_pierwsza(a):
#     for i in range(1,a):
#         if a % i ==0:
#             dzielniki.append(i)
#     if len(dzielniki)> 1:
#         print("nie jest pierwsza")
#     else:
#         print('pierwsza')
#
# jest_pierwsza(liczba)

# w = 0
# def pierwsza(a):
#     w = 0
#
#     while w!=1:
#         for i in range (2,a):
#             if a%i ==0:
#                 w+=1
#     if w==1:
#         print("pierwsza")
#     else:
#         print("nie pierwsza")
#
#
# pierwsza(liczba)

## https://www.practicepython.org/exercise/2014/01/29/01-character-input.html ##

# 12
# a = [5, 10, 15, 20, 25]
#
# def lista (a):
#     pierwszy = a [0]
#     last= a [-1]
#     b = [pierwszy,last]
#     return b
#
# print(lista(a))

#14
# lista = [1,2,2,3,4,4,]
#
# def usun_duplikaty(lista):
#     a = set(lista)
#     b = list(a)
#     return b
#
#
# print(usun_duplikaty(lista))

#18 Krowy i byki

# print("Witam w grze KROWY I BYKI")
# print("Zaczynamy!")
# byki = 0
# krowy = 0
#
# import random
# numer_komputer = random.randint(1,10000)
# print(numer_komputer)
# pier_cyf_komp = str(numer_komputer)[0]
# druga_cyf_komp = str(numer_komputer)[1]
# trzecia_cyf_komp = str(numer_komputer)[2]
# ost_cyf_komp = str(numer_komputer)[-1]
# gracz_numer = 'abcd'
# print(gracz_numer)
# while str(numer_komputer)!=gracz_numer:
#     while True:
#         kolejnosc = input("Ktora cyfre zgadujesz? a/b/c/d ? ")
#         if kolejnosc != 'a' and "b" and 'c' and 'd':
#             print("Podales zla wartosc")
#         else:
#             break
#     cyfra = input("Podaj cyfre: ")
#     if kolejnosc== 'a':
#         if pier_cyf_komp == cyfra:
#             print("Brawo! Zdobywasz byka")
#             krowy +=1
#             gracz_numer.replace('a',cyfra)
#         if cyfra == druga_cyf_komp or trzecia_cyf_komp or ost_cyf_komp:
#             print("Zdobywasz krowe")
#             krowy +=1
#     print(f"Krowy : {krowy} \nbyki: {byki}")
#     print(gracz_numer)

