# print(list(map(lambda x: x+1, [1,21,5,3])))
# def fun1(x):
#     return x+1
#
# lista = [1,2,5]
#
# print(list(map(fun1,lista)))

# lista = list(range(1,21))
# # print(lista)
#
# def funkc(x):
#     return 1/x
#
# print(list(map(funkc,lista)))
#
# print(list(map(lambda x : 1/x,lista)))
#
# lista2 = list(range(1,101))
# print(list(filter(lambda x: x%3 == 0 and x%4 != 0, lista2)))

#
# lista = [2,3,2,5,5,6,6,7]
# from functools import reduce
# print(reduce(lambda x,y : y-x ,lista))

# x = int(input("Podaj liczbe calkowita: "))

# def sumuj_mniejsze(x):
#     calkowite = list(range(1, 10))
#     suma =0
#     for c in calkowite:
#         if c <x:
#             return c + suma
#     print(suma)

# def sumuj_mniejsze(x):
#     if x==0:
#         return 0
#     else:
#         return x + sumuj_mniejsze(x-1)
#
# print(sumuj_mniejsze(4))

# Napisz funkcję rekurencyjną countup(n), która drukuje "Blastoff!" a następnie w kolejnych liniach numery od 1 do n
# def cutdown(x):
#     if x == 0:
#         return "Blastoff"
#     else:
#         print(x)
#         cutdown(x-1)
#
# cutdown(3)

# Suma cyfr liczby n jest sumą jej cyfr. Napisz rekurencyjną funkcję digitalSum(n), która pobiera dodatnią liczbę całkowitą n i zwraca sumę jej cyfr.
# liczba = int(input("Podaj dodatnia liczbe calkowita"))
# def digitalSum(n):
#     if n < 10:
#         print(n)
#     else:
#         print()
#
# import turtle
# t = turtle.Turtle()
# t.goto(100,100)
# t.penup()
# t.goto(200,200)
# t.pendown()
# t.goto(300,300)
# t.left(50)
# t.goto(50,50)
# window = turtle.Screen()
# window.mainloop()


# def dekor(f):
#     def wrapper():
#         print("dekorujemy")
#         return f()
#     return wrapper
# @ dekor
# def napisz (x="Ewa"):
#     print(f"helo {x}")
#
# napisz()

# def decorator (funk):
#     def wrapper():
#         wynik = funk()
#         return wynik.upper()
#     return wrapper
#
# @decorator
# def funkcja():
#     tekst = input("podaj tekkst ")
#     return tekst
#
# print(funkcja())

# Ćwiczenie 2: Napisać dekorator,
# mający za zadanie, drukować informację o czasie wykonywania funkcji.
# Dekorator, powinien być gotowy dekorować funkcje przyjmujące różną ilość parametrów.

# import time
#
# def dekorator(funk):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         x = funk(*args,**kwargs)
#         koniec = time.time()
#         print(koniec - start)
#         return x
#     return wrapper
#
# @dekorator
# def funkcja():
#     print("o la la")
#
# funkcja()


# import shutil
# from pathlib import Path
#
# sciezka1= Path('przyklad')
# sciezka2 = Path('przyklad/D')
#
# if sciezka1.exists() and sciezka1.is_dir():
#     """Recursively delete a directory tree."""
#     shutil.rmtree(sciezka1)
#
# sciezka1.mkdir()
#
# sciezkaB = sciezka1/'A'/'B'
# sciezkaC = sciezka1/'A'/'C'
#
# sciezkaB.mkdir(parents = True)
# sciezkaC.mkdir()
#
# # sciezka1.rename('A'/"AAA")

# lista = [1.2,3.5,4.1,8.6]
# lista2 = [int(i) for i in lista ]
# print(lista2)

# tekst = ['AAAAAGGAATTCCCCTAGAATTAAAAACCAGGTTACTG']
# frag = ['A', 'T', 'G', '0']
# print(["!!" for i in tekst ])

#
# class Zwierze:
#     """
#     Klasa dwfiniujaca zwierze
#     """
#
#     def __init__(self, imie, ulubione_zabawki, najgorsze_zabawki):
#         self.imie = imie
#         self.ulubione_zabawki = ulubione_zabawki
#         self.najgorsze_zabawki = najgorsze_zabawki
#
#     def przywitaj_sie(self):
#         return f"Czesc mam na imie {self.imie}"
#
#     def wymien_ulubione(self):
#         return f"Moje ulubone zabawki to : {self.ulubione_zabawki}"
#
#     def wymien_nielubiane(self):
#         return f"Moje najgorsze zabawki to : {self.najgorsze_zabawki} jest ich {len(self.najgorsze_zabawki)}"
#
# kot = Zwierze("Kotek","pilka",["lala","auto"])
#
# print(kot.przywitaj_sie())
# print(kot.wymien_ulubione())
# print(kot.ulubione_zabawki)
# print(kot.wymien_nielubiane())


class Player:
    '''
    Klasa repr gracza
    '''

    def __init__(self,nazwa,points):
        self.nazwa = nazwa
        self.points = points

    def wyswietl_punkty(self):
        return f"Gracz {self.nazwa}  ma {self.points} punktow"

    def zdobyty_punkt(self):
        self.points += 1

gracz1 = Player("AA",0)

gracz1.zdobyty_punkt()
print(gracz1.wyswietl_punkty())



