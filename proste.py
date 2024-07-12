# n = int(input("podaj liczbe n "))
# for i in range(0,n):
#     print(i ** 2)

# rok = int(input("ktory rok? "))
# def czy_przestepny(rok):
#     if rok % 4 == 0:
#         if rok % 100 == 0:
#             if rok % 400 == 0:
#                 print("Rok przestepny")
#             else:
#                 print("Rok nie jest przestepny")
#         else:
#             print("Rok przestepny")
#     else:
#         # return False
#         print("Rok nie jest przestepny")
#
#
# czy_przestepny(rok)

# lista = [["a", 20], ["c", 50], ["b", 50]]
# nlista = []
# for n, k in lista:
#     # print(k)
#     nlista.append(k)
# print(nlista)
# i = max(nlista)
# print(i)
# # for n,k in lista:
# nowa = [n,k for n,k in lista if k ==20]


# 3
# Kryszna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# list = [
# 3
# Kryszna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# ]

# licz_osob = list[0]
# # osoba = list
# a=list[-1:]index(/n)

# text = '''
# 3
# Kryszna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# '''
#
# text2 = text.replace(" ",",")
# print(text2)
# licz_osob = text2[1]
# print(f"liczba osob to {licz_osob}")
# # a =text2[::-1].find("\n"")
# # print(a)


# print(type('a'))
# print(5 * 's')
# a: int = 5
# a = ('aoao')
# b = 1.234
# print("aaa to %d" %b)
# print("aaa to %5f" %b)
# print(f"halo halo tu {b:.8f}")
# c=100000000000000
# print(f"to jest liczba {c:,}")
# d='ola ma kota'
# print(d.split())


# liczby3 = [3, 8, 5, 12, 1]
# liczby3.insert(3,0)
# print(liczby3)
# liczby3[3] = 2
# print(liczby3)
# liczby3.pop(2)
# liczby3.remove(3)
# print(liczby3)
#
# a = 'text'
# lista1 = list(a)
# print(lista1)
# lista2 = [a]
# print(lista2)

# slownik = {'czerwony': 'red', 'niebeiski': 'blue', 'bialy': 'white'}
# slowko = input("Podaj slowko do przetlumaczenia")
# # print(slownik[slowko])
# print(slowko)

#
# x = input("Podaj liczne x :")
# def describe_number(x):
#     match int(x):
#         case x if int(x) > 0:
#             print(f"Liczba {x} jest dodatnia")
#         case x if int(x) < 0:
#             print(f"Liczba {x} jest ujemna")
#         case x if int(x) == 0:
#             print(f"Liczba {x} wynosi zero")
#
# describe_number(x)


# lista = [0, 1, 2, 3, 4, 5]
# for i in enumerate(lista, start=100):
#     print(i)
#
# ludzie = ['Radek', 'Janek', 'Tomek', 'Martyna', "Marek"]
# wiek = [45, 40, 18, 26]
# for i,j in zip(ludzie,wiek):
#     print(i,j)
#

# Napisz funkcję sum_of_squares, która przyjmuje listę liczb całkowitych jako argument i zwraca sumę kwadratów tych liczb.
# Skorzystaj z pętli for, aby przejść przez wszystkie elementy listy i obliczyć sumę kwadratów.

# lista2 = []
#
# def sum_of_squares(x):
#     suma = 0
#     for i in x:
#         a =(i**2)
#         lista2.append(a)
#         suma += a
#     print(f'suma wynosi {suma}')
#
#
#
#
# lista = [2,4,10,8]
# sum_of_squares(lista)
# print(lista2)
# # print(f'suma wynosi {suma}')

# Napisz funkcję countdown, która przyjmuje jedną liczbę całkowitą n jako argument i drukuje odliczanie od n do 1,
# a następnie drukuje "Start!". Użyj pętli while, aby zrealizować odliczanie.

# def countdown(n):
#     while n >= 1:
#         print(n)
#         n = n - 1
#     print("strat")
#
#
# countdown(3)
#
# 1. Dodawanie
#     2. Odejmowanie
#     3. Mnożenie
#     4. Dzielenie
#     5. Koniec


while True:
    wybor = int(input('''wybierz numer:
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    '''))
    if wybor == 5:
        print("Koniec pracy")
        break

    else:
        try:
            if wybor==1 or wybor==2 or wybor==3 or wybor==4:
                liczba1 = int(input("pierwsza liczba: "))
                liczba2 = int(input("druga liczba: "))
                if wybor == 1:
                    # print(liczba1 + liczba2)
                    a=liczba1 + liczba2
                elif wybor == 2:
                    # print(liczba1 - liczba2)
                    a=liczba1 - liczba2

                elif wybor == 3:
                    # print(liczba1 * liczba2)
                    a=liczba1 * liczba2
                elif wybor == 4:
                    # print(liczba1 / liczba2)
                    a=liczba1 / liczba2
            else:
                    print("zly nr")
                    break
        except ZeroDivisionError:
            print("nie dziel prez zero")
            # if wybor==4 and liczba2==0:
            #     print()
        except ValueError:
            print('Podaj poprawna wartosc')
        except TypeError:
            print('Podaj poprawna wartosc')

        else:
            print("obliczono")
            print(f"wynik oblicznia: {a}")
        finally:
            print('obliczenia zakonczono')
