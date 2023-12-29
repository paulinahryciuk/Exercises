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

import time

def dekorator(funk):
    def wrapper(*args, **kwargs):
        start = time.time()
        x = funk(*args,**kwargs)
        koniec = time.time()
        print(koniec - start)
        return x
    return wrapper

@dekorator
def funkcja():
    print("o la la")

funkcja()
