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


# while True:
#     wybor = int(input('''wybierz numer:
#     1. Dodawanie
#     2. Odejmowanie
#     3. Mnożenie
#     4. Dzielenie
#     5. Koniec
#     '''))
#     if wybor == 5:
#         print("Koniec pracy")
#         break
#
#     else:
#         try:
#             if wybor==1 or wybor==2 or wybor==3 or wybor==4:
#                 liczba1 = int(input("pierwsza liczba: "))
#                 liczba2 = int(input("druga liczba: "))
#                 if wybor == 1:
#                     # print(liczba1 + liczba2)
#                     a=liczba1 + liczba2
#                 elif wybor == 2:
#                     # print(liczba1 - liczba2)
#                     a=liczba1 - liczba2
#
#                 elif wybor == 3:
#                     # print(liczba1 * liczba2)
#                     a=liczba1 * liczba2
#                 elif wybor == 4:
#                     # print(liczba1 / liczba2)
#                     a=liczba1 / liczba2
#             else:
#                     print("zly nr")
#                     break
#         except ZeroDivisionError:
#             print("nie dziel prez zero")
#             # if wybor==4 and liczba2==0:
#             #     print()
#         except ValueError:
#             print('Podaj poprawna wartosc')
#         except TypeError:
#             print('Podaj poprawna wartosc')
#
#         else:
#             print("obliczono")
#             print(f"wynik oblicznia: {a}")
#         finally:
#             print('obliczenia zakonczono')

# import datetime
# a = datetime.datetime.now()
# print(a)
# print(a.strftime("%B"))

# Napisz funkcję reverse_string, która przyjmuje łańcuch znaków jako argument i zwraca ten łańcuch odwrócony.
# Użyj pętli while, aby odwrócić łańcuch.

# def rev_str(x):
#     dl = len(x)
#
#     while dl > 0:
#         o = (x[dl - 1])
#         print(o)
#         dl -= 1
#
# rev_str('alami')
#
# with open('nauka', 'w+') as ft:
#     ft.write("ucze sie")
#
# with open('nauka') as ft:
#     a =ft.read()
# print(a)
#
# Napisz program w Pythonie, który wczytuje plik CSV zawierający dane o uczniach (imię, nazwisko, wiek, klasa)
# i zapisuje do nowego pliku CSV tylko tych uczniów, którzy są w wieku 15 lat lub starsi.

# import csv
# with open("uczniowie.csv",'r') as file:
#     # writer = csv.reader(file, delimiter=',')
#     # for line in writer:
#     #     print(readlines)
#     #     # plik =line
#     # print(plik)
#     # fieldname = ['name','surname','age','klasa']
#     # reader = csv.DictReader('uczniowie.csv',delimiter=',')
#     # for line in reader:
#     #     print(line)
#     # reader =csv.DictReader(file, fieldnames=fieldname,delimiter=',')
#     # for line in reader:
#     #     if int(reader['age'])>=15:
#     #         print(line)
#     reader = csv.DictReader(file)
#     # for line in reader:
#     #     if reader['age']>15:
#     #         print(line)
#     stud = [row for row in reader if int(reader['age'])>=15]
#     print(stud)
#
# import csv
# with open("uczniowie.csv",'r') as file:
#     reader = csv.DictReader(file)
#     stud = [row for row in reader if int(row['age']) >= 15]
# print(stud)


# import csv
# file = 'uczniowie.csv'
# with open(file,'r') as ft:
#     reader = csv.DictReader(ft)
#     students = [line for line in reader if int(line['age'])>=15]
# print(students)
#
# fieldname = ['name','surname','age','klasa']
# file2 = 'uczniowie2.csv'
#
# with open(file2,'w') as ft2:
#     writer = csv.DictWriter(ft2,fieldnames=fieldname)
#     writer.writeheader()
#     writer.writerows(students)


# def wylicz_srednia(x):
#     print(sum(x) / len(x))
#
#
# x = (5, 4, 3, 5)
# wylicz_srednia(x)


# def sumuj(*cyfry):
#     suma = 0
#     for i in cyfry:
#          suma += i
#     return suma
#
#
# print(sumuj(2, 3, 4))

# def wylicz_srednia2(uczen, *oceny):
#     # sumuj(oceny)
#     suma = 0
#     for i in oceny:
#         suma += i
#         # return suma
#     srednia = suma/len(oceny)
#     print(f"Srednia ucznia {uczen} wynosi: {srednia}")
#
# # x = (Ola, 4,5,6,)
# wylicz_srednia2('Ola',4,5,6)


# Napisz funkcję describe_student, która przyjmuje argumenty pozycyjne (imię, nazwisko, wiek) oraz dowolną liczbę
# argumentów nazwanych (**kwargs), które mogą zawierać dodatkowe informacje o uczniu (np. klasa, hobby, ulubiony_przedmiot).
# Funkcja powinna zwracać słownik z wszystkimi informacjami o uczniu.

# def describe_student(imie, nazwisko, wiek, **kwargs):
#     print(f"Uczen {imie} {nazwisko} ma lat: {wiek} ")
#     print(f"Dodatkowe informacje o nim to : {kwargs}")
#
#
#
# describe_student("Adam", "Kot", 8, klasa='2b', hobby='pilka')
#
# bezwz = lambda *args: abs(sum(args))
# print(bezwz(-1,2,-4,-5))
#
# liczby = [2,5,9,3]
# fun = list(map(lambda x: x*10, liczby))
# print(fun)


# import datetime
#
# today = datetime.date.today()
# print(today)
# tomorrow = today+datetime.timedelta(days=1)
# print(tomorrow)
#
# Napisz program, który zawiera funkcję zagnieżdżoną do obliczania kwadratu liczby, oraz funkcję główną,
# która zwraca listę kwadratów liczb z listy wejściowej.
#
#
# def fun1(number):
#     def fun2(x):
#         return x*x
#     # return fun1
#     lista = []
#     for i in number:
#         lista.append(fun2(i))
#     return lista
#
#
# print(fun1([3,4,5]))
#
# Napisz program, który zawiera funkcję zagnieżdżoną do sprawdzania, czy liczba jest liczbą pierwszą, oraz funkcję główną,
# która zwraca listę wszystkich liczb pierwszych mniejszych niż zadana liczba n.

