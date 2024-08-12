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

# def fun1(lista):
#     def fun2(i):
#         return i
#     parzyste=[]
#     for _ in lista:
#         if _%2 ==0:
#             parzyste.append(_)
#
#     parz_duze=[]
#     for y in parzyste:
#         if y >3:
#             parz_duze.append(y)
#
#     return parz_duze
#
#
# print(fun1([2, 3, 4, 5]))


# def fun1(n):
#     def fun2(i):
#         return i
#     parzyste=[]
#     for _ in range(1,n):
#         if _%2 ==0:
#             parzyste.append(_)
#     return parzyste
#
# print(fun1(10))
#
#
# Napisz program, który sortuje listę słowników według określonego klucza, używając funkcji lambda.

# Instrukcje
# Zdefiniuj listę słowników, gdzie każdy słownik reprezentuje osobę z kluczami imie, wiek, miasto.
# Użyj funkcji lambda do posortowania listy według wieku (wiek) w porządku rosnącym.
# Użyj funkcji lambda do posortowania listy według imienia (imie) w porządku alfabetycznym.
# Użyj funkcji lambda do posortowania listy według miasta (miasto) w porządku alfabetycznym.


# sortowanie_wiek = lambda **kwargs: sorted(kwargs,key=kwargs.wiek)
#
# baza = [{'imie':"Ola", 'wiek':10, 'miasto':'Krakow'}, {'imie':"Ala", 'wiek':5, 'miasto':'Warsz'},
#         {'imie':"Adam",'wiek':12, 'miasto':"Adamowka"}]
#
# sortowanie_wiek(baza)


# Napisz program, który używa funkcji lambda do przekształcenia listy liczb przez:
#
# Pomnożenie każdej liczby przez 2.
# Dodanie 5 do każdej liczby.

# dwu = lambda x: x*2
# print(list(map(dwu,[2, 4, 6])))
# print(list(map(lambda x:x*2,[2, 4, 6])))
#
# piec = lambda x:x+5
# print(list(map(piec,[5,15,95])))
#
# duze = lambda x:x>5
# print(list(filter(duze,[5,10,2,56])))
#
#
# Napisz program, który filtruje listę liczb, używając funkcji lambda, w celu:
#
# Znalezienia wszystkich liczb parzystych.
# Znalezienia wszystkich liczb nieparzystych.
# Znalezienia wszystkich liczb większych od podanej wartości.

# lista = [2, 7, 6, 5, 3, 9, 1]
# parzyste = list(filter(lambda x: x % 2 == 0, lista))
# print(parzyste)
#
# wieksze = list(filter(lambda x: x>5,lista))
# print(wieksze)
#
# Znaleźć najdłuższe słowo w liście słów.

# from functools import reduce
#
# slowa = ['ala', 'kokokokok', 'ul']
# najluzsze = reduce(lambda x,y: x if len(x)>len(y) else y, slowa)
# print(najluzsze)
#


# Napisz dekorator sprawdz_typy, który sprawdza typy argumentów przekazywanych do funkcji i wyświetla ostrzeżenie,
# jeśli typy są niezgodne z oczekiwanymi.
#
# Instrukcje
# Zdefiniuj dekorator sprawdz_typy.
# Zdefiniuj przykładową funkcję, np. dodaj(a, b), która dodaje dwie liczby.
# Użyj dekoratora sprawdz_typy, aby sprawdzić, czy argumenty przekazywane do funkcji dodaj(a, b) są typu int.

# def spr_typ(funkcja):
#     def wrapper(a,b):
#         if type(a) == 'int' and type(b) == 'int':
#             print("mozesz dodawac")
#         else:
#             print("nie mozesz dodac bo to nie sa liczby")
#         return funkcja
#     print("----")
#     return wrapper
#
#
# @spr_typ
# def sumuj(a, b):
#     return a + b
#
#
# print(sumuj(1, 2))
# print(type(1))
#
#
# Napisz dekorator licz_wywolania, który liczy, ile razy dana funkcja została wywołana. Licznik powinien być przypisany
# do atrybutu wywolania dekorowanej funkcji.
#
# Instrukcje
# Zdefiniuj dekorator licz_wywolania.
# Zdefiniuj przykładową funkcję, np. powitaj(), która wypisuje "Cześć!".
# Użyj dekoratora licz_wywolania do funkcji powitaj i sprawdź liczbę wywołań po kilku wywołaniach funkcji.


# licznik =0
# def licz_wywolania(funkcja):
#     # licznik =0
#     def wrapper():
#         # licznik+=1
#         wrapper.wywolania +=1
#
#     return wrapper()
#
#
# @licz_wywolania
# def powitanie():
#     print("Czesc")
#
# powitanie()


# Zadanie
# Zdefiniuj dekorator capitalize_output, który będzie zmieniał wszystkie litery w zwracanym przez funkcję tekście na wielkie.
# Zdefiniuj przykładową funkcję powitanie, która przyjmuje imię jako argument i zwraca powitanie w formacie "Cześć, {imię}!".
# Użyj dekoratora capitalize_output na funkcji powitanie.
# Wywołaj funkcję powitanie z różnymi argumentami i sprawdź, czy zwracany tekst jest w wersji z wielkimi literami.

# def capitalize_output(funk):
#     def wrapper(*args,**kwargs):
#         results = funk(*args,**kwargs)
#         return results.upper
#     return wrapper
#
#
# @capitalize_output
# def powitanie(x):
#     print(f"witaj {x}")
#
# powitanie("Pau")
#
#
# Zadanie: Automatyczna walidacja zakresu wartości
# Zadanie: Napisz dekorator, który automatycznie sprawdza, czy argumenty przekazane do funkcji mieszczą się w określonym
# zakresie. Jeśli nie, powinien zgłaszać błąd (ValueError).

# def spr_zakresu(func):
#     def wrapper(*arg, **kwargs):
#          results = func(*arg,**kwargs)
#          if results > 10:
#              print( 'za duza wartosc')
#          return results
#     return wrapper
#
#
# @spr_zakresu
# def liczba_wielkosc(x):
#     print(f"twoja jednocyfrowa liczba to {x}")
#     return x
#
#
# liczba_wielkosc(5)
# liczba_wielkosc(15)
#
# Zadanie 1: Podwojenie wartości w liście

# lista = [0,5,7,8]
# lista2 = [i*2 for i in lista]
# print(lista2)
#
# # Zadanie 2: Filtracja liczb parzystych
# lista3 = [i for i in lista if i%2 ==0]
# print(lista3)
#
# # Zadanie 3: Lista kwadratów
# lista4 = [i*i for i in lista3]
# print(lista4)

# Zadanie 4: Długości słów w zdaniu
#
# zdanie = 'Ola ma kota.'
# lista = [len(i) for i in zdanie]
# print(lista)
# lista2 = [len(i) for i in zdanie.split()]
# print(lista2)

# Zadanie 5: Zamiana liter na wielkie
# slowa = ['obraz', 'waz']
# slowo_upt = [i.upper() for i in slowa]
# print(slowo_upt)
#
#
# Zadanie: Klasa Prostokat
# Opis: Utwórz klasę Prostokat, która będzie reprezentować prostokąt. Klasa powinna mieć metody do obliczania pola oraz
# obwodu prostokąta.
#
# Szczegóły:
#
# Klasa powinna mieć dwie właściwości: dlugosc i szerokosc.
# Dodaj metodę pole(), która zwróci pole prostokąta.
# Dodaj metodę obwod(), która zwróci obwód prostokąta.

#
# class Prostokat():
#     """
#     Klasa opisujeaca prostokat
#     """
#
#     def __init__(self, dlugosc, szerokosc):
#         self.dlugosc = dlugosc
#         self.szerokosc = szerokosc
#
#
#     def oblicz_pole(self):
#         pole = self.dlugosc * self.szerokosc
#         print(f"Pole prostokata wynosi {pole} cm kwdr")
#
#
#     def oblicz_obwod(self):
#         obwod = 2 * self.dlugosc + 2 * self.szerokosc
#         print(f"Obowd prostokata o wymiarach {self.dlugosc} i {self.szerokosc} wynosi: {obwod} cm")
#
#     def czy_kwadrat(self):
#         if self.dlugosc==self.szerokosc:
#             return True
#         else:
#             return False
#
#
# p1 = Prostokat(2, 3)
# p1.oblicz_pole()
# p1.oblicz_obwod()
# print(p1.czy_kwadrat())
# p2 = Prostokat(2,2)
# print(p2.czy_kwadrat())
#
#
#


# Zadanie: Klasa Samochod
# Opis: Utwórz klasę Samochod, która będzie reprezentować samochód. Klasa powinna posiadać metody do dodawania przebiegu,
# obliczania średniego spalania oraz zwracania informacji o samochodzie.
#
# Szczegóły:
#
# Klasa powinna mieć właściwości:
# marka
# model
# rocznik
# przebieg (początkowo ustawiony na 0)
# spalanie (średnie spalanie w litrach na 100 km, domyślnie ustawione na 7.0)
# Dodaj metodę dodaj_przebieg(km), która zwiększy przebieg o podaną wartość.
# Dodaj metodę oblicz_spalanie(km, litry), która obliczy średnie spalanie na podstawie przejechanych kilometrów i zużytego paliwa.
# Dodaj metodę info(), która zwróci informacje o samochodzie (marka, model, rocznik, przebieg).
#
# class Samochod():
#     """
#     Klasa opisujaca samochod
#     """
#
#     def __init__(self, marka, model, rocznik, przebieg, spalanie=7.0):
#         self.marka = marka
#         self.model = model
#         self.rocznik = rocznik
#         self.przebieg = przebieg
#         self.spalanie = spalanie
#
#     def dodaj_przebieg(self):
#         self.przebieg += 10
#
#     def oblicz_spalanie(self):
#         # self.srednie_spalanie = srednie_spalanie
#         self.srednie_spalanie = self.przebieg * self.spalanie
#         print(f"srednie spalanie to: {self.srednie_spalanie} ")
#
#     def info(self):
#         print(
#             f"Samochod marki {self.marka} model: {self.model} ma przebieg: {self.przebieg} a spalnie srednie wynosi: {self.srednie_spalanie}")
#
#
# sam1 = Samochod('Ford', 'Mondeo', 2020, 0)
# sam1.dodaj_przebieg()
# sam1.dodaj_przebieg()
# sam1.oblicz_spalanie()
# sam1.info()


# Zadanie: Klasa KontoBankowe
# Opis: Utwórz klasę KontoBankowe, która będzie reprezentować konto bankowe z hermetyzowanymi danymi.
# Klasa powinna umożliwiać dostęp do salda oraz operacje wpłaty i wypłaty środków, z zachowaniem odpowiednich zasad.
#
# Szczegóły:
#
# Klasa powinna mieć atrybuty:
# _numer_konta (prywatny)
# _saldo (prywatny, początkowo 0)
# Dodaj metodę wplac(kwota), która zwiększy saldo o podaną kwotę.
# Dodaj metodę wyplac(kwota), która zmniejszy saldo o podaną kwotę, jeśli saldo na to pozwala.
# Dodaj metodę sprawdz_saldo(), która zwróci aktualne saldo.
# Dodaj getter i setter dla numeru konta, aby można było go odczytać, ale nie zmieniać po utworzeniu konta.


# class KontoBankowe():
#     def __init__(self, __numer_konta, __saldo=0):
#         self.__numer_konta = __numer_konta
#         self.__saldo = __saldo
#
#     def wplac(self, kwota):
#         # self.kwota = kwota
#         self.__saldo += kwota
#         print("Pieniadze wplacone")
#
#     def wyplac(self, wyplata):
#         # self.wyplata = wyplata
#         if wyplata <= self.__saldo:
#             self.__saldo -= wyplata
#             print("Pieniadze wyplacone")
#         else:
#             print("Masz za malo pieniedzy")
#
#     def sprawdz_saldo(self):
#         print(f"Stan konta wynosi: {self.__saldo}")
#
#
# k1 = KontoBankowe(2222)
# k1.wplac(1000)
# k1.sprawdz_saldo()
# k1.wyplac(200)
# k1.sprawdz_saldo()


# Zadanie: Klasy Zwierze i Pies
# Opis: Utwórz dwie klasy: Zwierze i Pies. Klasa Pies powinna dziedziczyć po klasie Zwierze.
# Klasa Pies powinna mieć dodatkową metodę specyficzną dla psów.
#
# Szczegóły:
#
# Klasa Zwierze powinna mieć atrybuty:
# gatunek
# wiek
# Klasa Zwierze powinna mieć metodę dzwiek(), która będzie zwracać dźwięk wydawany przez zwierzę.
# Klasa Pies powinna dziedziczyć po klasie Zwierze i mieć dodatkowy atrybut rasa.
# Klasa Pies powinna nadpisać metodę dzwiek() tak, aby zwracała "Hau hau!".
# Dodaj do klasy Pies metodę aportuj(), która zwraca tekst "Pies aportuje!".

# class Zwierze():
#     def __init__(self, gatunek, wiek):
#         self.gatunek = gatunek
#         self.wiek = wiek
#
#     def dzwiek(self):
#         return "zwierze wydaje dzwiek"
#
#
# class Pies(Zwierze):
#     def __init__(self, gatunek, wiek, rasa):
#         super().__init__( gatunek, wiek)
#         self.rasa = rasa
#
#     def dzwiek(self):
#         return "Hau hau"
#
#     def aportuj(self):
#         print("Pies aportuje")
#
#
# z1 = Pies('pies', 5, 'owczarek')
# z1.aportuj()
# print(z1.dzwiek())


# Zadanie: Klasy Pojazd i Samochod
# Opis: Utwórz dwie klasy: Pojazd i Samochod. Klasa Samochod powinna dziedziczyć po klasie Pojazd.
# Dodaj atrybuty i metody, które będą odpowiednio wykorzystywać dziedziczenie.
#
# Szczegóły:
#
# Klasa Pojazd powinna mieć atrybuty:
# marka
# model
# rok_produkcji
# Klasa Pojazd powinna mieć metodę opis_pojazdu(), która zwróci opis pojazdu w formacie: "Marka Model (Rok produkcji)".
# Klasa Samochod powinna dziedziczyć po klasie Pojazd i mieć dodatkowy atrybut liczba_drzwi.
# Klasa Samochod powinna mieć metodę opis_samochodu(), która rozszerza opis pojazdu o informację o liczbie drzwi.
# Klasa Samochod powinna również mieć metodę czy_klasyczny(), która sprawdzi, czy samochód jest klasyczny (starszy niż 25 lat).
#
# import datetime
#
#
# class Pojazd():
#     def __init__(self, marka, model, rok_produkcji):
#         self.marka = marka
#         self.model = model
#         self.rok_produkcji = rok_produkcji
#
#     def opis_pojazdu(self):
#         return f"{self.marka} {self.model} ({self.rok_produkcji})"
#
#
# class Samochod(Pojazd):
#     def __init__(self, marka, model, rok_produkcji, l_drzwi):
#         super().__init__(marka, model, rok_produkcji)
#         self.l_drzwi = l_drzwi
#
#     def opis_samochodu(self):
#         # print(f"{self.marka} {self.model} ({self.rok_produkcji}) liczba drzwi:{self.l_drzwi}")
#         print(f"{self.opis_pojazdu()} liczba drzwi:{self.l_drzwi}")
#
#     def czy_klasyczny(self):
#         # x = datetime.datetime.now()
#         # y = x.strftime('%x')
#         # if int(y) - self.rok_produkcji > 25:
#         if 2024 - self.rok_produkcji > 25:
#             return True
#         else:
#             return False
#
#
# s1 = Samochod('Ford', 'Mondeo', 2008, 4)
# s1.opis_samochodu()
# print(s1.czy_klasyczny())
# # print(datetime.datetime.now())


# Zadanie: System Płatności
# Opis: Utwórz system, który obsługuje różne metody płatności (np. kartą kredytową, PayPal, przelewem bankowym).
# W tym celu stwórz klasę abstrakcyjną Platnosc, która będzie zawierała metody abstrakcyjne do przeprowadzania płatności i
# sprawdzania statusu płatności. Następnie utwórz klasy pochodne dla różnych metod płatności, które będą implementować te metody.
#
# Szczegóły:
# Klasa abstrakcyjna Platnosc:
#
# Powinna zawierać dwie metody abstrakcyjne:
# zaplac(kwota): metoda odpowiedzialna za realizację płatności.
# sprawdz_status(): metoda odpowiedzialna za sprawdzenie statusu płatności.
# Klasy pochodne:
#
# Utwórz klasy PlatnoscKarta, PlatnoscPayPal i PlatnoscPrzelew, które dziedziczą po Platnosc.
# Każda z tych klas powinna implementować metody zaplac() i sprawdz_status() w sposób charakterystyczny dla danej metody płatności.
# Symulacja płatności:
#
# Utwórz obiekty każdej z klas płatności i zasymuluj realizację płatności oraz sprawdzenie statusu.


# from abc import ABC, abstractmethod
# # import abc
#
# class Platnosc(ABC):
#
#     @abstractmethod
#     def zaplac(self):
#         pass
#
#     @abstractmethod
#     def sprawdz_status(self):
#         pass
#
#
# class PlatnoscKarta(Platnosc):
#
#     def zaplac(self, kwota):
#         self.kwota = kwota
#         print(f"Platnosc karta na kwote {self.kwota} pobiegla pomyslnie")
#
#     def sprawdz_status(self):
#         print("platnosc pobiegla pomyslnie")
#
#
# p1 = PlatnoscKarta()
# p1.zaplac(200)

# import math
#
# class Czlowiek:
#     def __init__(self, imie):
#         self.imie = imie
#
#     def __str__(self):
#         # return f'({self.imie})'
#         return f'({self.imie!r})'
#
# c = Czlowiek('Ania')
# print(c.imie)
# print(c)
#
# x = 'asia'
# print(f'{x!r}')


# Zadanie: System pojazdów
# Wyobraź sobie, że tworzysz prosty system zarządzania pojazdami. Każdy pojazd ma swoje unikalne właściwości,
# ale niektóre pojazdy mogą dziedziczyć cechy od innych.
#
# Stwórz klasę Vehicle, która będzie bazową klasą dla wszystkich pojazdów. Klasa ta powinna mieć metodę move(),
# która wypisuje "Vehicle is moving".
#
# Stwórz klasę Car, która dziedziczy po klasie Vehicle. Klasa Car powinna nadpisać metodę move() tak,
# aby wypisywała "Car is driving".
#
# Stwórz klasę Boat, która również dziedziczy po klasie Vehicle. Klasa Boat powinna nadpisać metodę move() tak,
# aby wypisywała "Boat is sailing".
#
# Stwórz klasę AmphibiousVehicle, która dziedziczy zarówno po Car, jak i Boat. Niech ta klasa nie nadpisuje metody move().
#
# Utwórz obiekt klasy AmphibiousVehicle i wywołaj metodę move(). Zastanów się, która metoda zostanie wywołana i dlaczego.
#
# (Opcjonalnie) Dodaj do klasy AmphibiousVehicle swoją wersję metody move(), która wypisuje "Amphibious Vehicle is moving",
# a następnie wywołaj ją ponownie.
#
# class Vehicle:
#     def move(self):
#         print("Vehicle is moving")
#
# class Car(Vehicle):
#     def move(self):
#         print("Car is driving")
#
# class Boat(Vehicle):
#     def move(self):
#         print("Boat is sailing")
#
# class AmphibiousVehicle(Car,Boat):
#     pass
#
#     @staticmethod
#     def statyczna():
#         print("to jest metoda statyczna")
#
#
# o1 = AmphibiousVehicle()
# o1.move()
# AmphibiousVehicle.statyczna()


# Zadanie: Zarządzanie kontami bankowymi
# Stwórz klasę BankAccount, która będzie reprezentować konto bankowe. Każde konto ma numer konta i saldo.
# Klasa ta powinna mieć możliwość tworzenia kont na różne sposoby, a także przechowywania liczby wszystkich utworzonych kont.
#
# Wymagania:
# Atrybuty klasy:
#
# total_accounts: Atrybut klasy, który przechowuje liczbę wszystkich utworzonych kont.
# Konstruktor (__init__):
#
# Przyjmuje dwa argumenty: numer konta i saldo początkowe.
# Zwiększa total_accounts o 1 za każdym razem, gdy tworzone jest nowe konto.
# Metoda klasowa from_balance_only(balance):
#
# Tworzy nowe konto z losowym numerem konta (możesz wykorzystać prosty licznik do generowania unikalnych numerów) i
# podanym saldem początkowym.
# Metoda klasowa total_accounts_created():
#
# Zwraca liczbę wszystkich utworzonych kont (wartość total_accounts).
# Metoda instancyjna display():
#
# Wyświetla informacje o numerze konta i saldzie.

# class BankAccount:
#     '''
#     Reprezentuje konto bankowe
#     '''
#     def __init__(self,nr_konta, saldo):
#         self.nr_konta = nr_konta
#         self.saldo = saldo
#     total_accounts = 0
#
#     @classmethod
#     def total_accounts_created(cls,  total_accounts):
#         cls.total_accounts +=1
#
#     @classmethod
#     def from_balance_only(cls, balance):
#
#     @classmethod
#     def total_accounts_created(cls):
#         return cls.total.accounts
#
#     def display(self):
#         return self.nr_konta,self.saldo


# import pickle
#
# slownik = {"imie":"ania", "nazwisko":"nowak", "wiek":40}
# with open ('plik_pikle', 'wb') as file:
#     pickle.dump(slownik, file)
#
# with open('plik_pikle', 'rb') as f:
#     p = pickle.load(f)
#
# print(p)


# Zadanie: System zamówień w restauracji
# Stwórz prosty system zamówień dla restauracji. System ten powinien pozwalać na dodawanie zamówień, przeliczanie kosztów,
# a także obsługiwać sytuacje, gdy podane dane są nieprawidłowe, na przykład jeśli zamówienie jest puste lub cena jest ujemna.
#
# Wymagania:
# Klasa MenuItem:
#
# Atrybuty:
# name (nazwa dania, typ: string)
# price (cena dania, typ: float)
# Konstruktor inicjalizuje powyższe atrybuty i sprawdza, czy cena jest dodatnia. Jeśli nie, zgłasza wyjątek ValueError.
# Metoda __str__() zwraca ładnie sformatowany string zawierający nazwę dania i jego cenę.
# Klasa Order:
#
# Atrybuty:
# items (lista dań, typ: list)
# Metody:
# add_item(item) - dodaje pozycję do zamówienia.
# total_cost() - oblicza i zwraca całkowity koszt zamówienia.
# __str__() - zwraca ładnie sformatowany string zawierający wszystkie pozycje zamówienia i całkowity koszt.
# Klasa EmptyOrderError:
#
# Dziedziczy po Exception i reprezentuje wyjątek, który ma być zgłaszany, gdy zamówienie jest puste.
# Metoda finalize_order(order):
#
# Sprawdza, czy zamówienie zawiera co najmniej jedną pozycję. Jeśli nie, zgłasza EmptyOrderError.
# Jeśli zamówienie jest poprawne, wypisuje szczegóły zamówienia i całkowity koszt.

# class MenuItem:
#     def __init__(self,name: str, price: float):
#         if price < 0:
#             raise ValueError('cena nei mzoe byc ujemna')
#         self.name = name
#         self.price = price
#
#     def __str__(self):
#         return f"Danie: {self.name}, cena: {self.price}"
#
#
#
# class Order:
#     def __init__(self):
#         self_item = []
#
#     def add_item(self, item):
#         self.item.append(item)
#
#
#
#     def total_cost(self):
#         for i in self.item:
#             print(item.price)
#
#
#     def __str__(self):
#         print(f"zamowiono: {self.item}, koszta zamowienia wynosi: {self.total_cost} ")
#
# class EmptyOrderError(Exception):
#     pass
#
#     def finalize_order(self, order)
#         if self.item < 1:
#             raise EmptyOrderError (zamowieei nei moze byc puste)
#             end
#         end
#     end


# Zadanie: Alfabet
# Stwórz klasę Alphabet, która będzie iteratorem generującym kolejne litery alfabetu od A do Z.
#
# Wymagania:
# Klasa Alphabet:
# Atrybuty:
# current (bieżąca litera, typ: str, domyślnie 'A')
# Konstruktor inicjalizuje powyższy atrybut.
# Metoda __iter__() powinna zwracać self.
# Metoda __next__() powinna zwracać bieżącą literę alfabetu i przechodzić do kolejnej. Jeśli litera osiągnie 'Z',
# metoda powinna zgłosić wyjątek StopIteration.


# class StopIteration(Exception):
#     pass


# class Alphabet:
#     def __init__(self):
#         self.current = 'A'
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current <'Z':
#             self.current= litera
#             self.current + 1
#             return litera
#         else:
#             raise StopIteration
#
#
#     # def koniec_iteracji(self):
#     #     raise StopIteration('Itareacja zakonczyla sie')
#
#
# a = Alphabet()
# print(a.__iter__)
# print(a.__next__())


# Zadanie: Porównywanie prostokątów
# Stwórz klasę Rectangle, która będzie reprezentowała prostokąt. Klasa powinna mieć możliwość porównywania dwóch
# prostokątów na podstawie ich pola powierzchni. Zaimplementuj metodę __lt__, która pozwoli porównywać dwa prostokąty za
# pomocą operatora <.
#
# Wymagania:
# Klasa Rectangle:
#
# Atrybuty:
# width (szerokość prostokąta, typ: float)
# height (wysokość prostokąta, typ: float)
# Konstruktor inicjalizuje powyższe atrybuty.
# Metoda area() powinna zwracać pole powierzchni prostokąta (szerokość * wysokość).
# Metoda __lt__() powinna zwracać True, jeśli pole powierzchni pierwszego prostokąta jest mniejsze niż pole powierzchni
# drugiego prostokąta, i False w przeciwnym przypadku.
# Napisz kod, który porówna kilka prostokątów i wyświetli odpowiednie wyniki.

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def __lt__(self, other):
#         return self.area() < other.area()
#
#
# pr1 = Rectangle(2, 2)
# pr2 = Rectangle(2, 3)
# print(pr1.__lt__(pr2))


# Zadanie: Kalkulator
# Stwórz klasę Calculator, która będzie prostym kalkulatorem wykonującym operacje dodawania, odejmowania, mnożenia i
# dzielenia. Klasa powinna obsługiwać wyjątki, które mogą wystąpić podczas wykonywania tych operacji, takie jak próba dzielenia przez zero lub wprowadzenie niepoprawnych danych wejściowych.
#
# Wymagania:
# Klasa Calculator:
#
# Metody:
# add(a, b): zwraca sumę a i b.
# subtract(a, b): zwraca różnicę a i b.
# multiply(a, b): zwraca iloczyn a i b.
# divide(a, b): zwraca wynik dzielenia a przez b. Jeśli b jest zerem, metoda powinna zgłosić wyjątek ZeroDivisionError z
# komunikatem "Cannot divide by zero."
# Każda z metod powinna również obsługiwać wyjątek ValueError, jeśli dane wejściowe nie są liczbami. W takim przypadku
# powinna zgłaszać wyjątek ValueError z komunikatem "Invalid input. Please enter numbers."
# Napisz kod, który wykorzysta klasę Calculator i spróbuje wykonać różne operacje, obsługując zgłaszane wyjątki.


# class BladWartosci(Exception):
#     def __init__(self, value):
#         super().__init__()
#         self.value = value
#
#
# class Kalkulator:
#     '''
#     Podstawowy kalkulator
#     '''
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         self.BWartosci()   ##
#
#     def dodawanie(self):
#         print(self.a + self.b)
#
#     def odejmowanie(self):
#         print(self.a - self.b)
#
#     def mnozenie(self):
#         print(self.a * self.b)
#
#     def dzielenie(self):
#         print( self.a / self.b)
#
#     def BWartosci(self):
#         if not isinstance(self.a, int):
#             raise BladWartosci(self.a)  ##
#         if not isinstance(self.b, int):
#             raise BladWartosci(self.b)
#
#
# try:
#     k1 = Kalkulator( 's',6)
#     k1.dzielenie()
# except ZeroDivisionError:
#     print("nie mozna dzielic przez 0")
# except BladWartosci:
#     print("nie mozna")
# else:
#     print("Wprowadziles dobre wartosci")
# finally:
#     print("koniec obliczen")

#################
# class BladWartosci(Exception):
#     def __init__(self, msg):
#         super().__init__(msg)
#
#
# class Kalkulator:
#     '''
#     Podstawowy kalkulator
#     '''
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         self.BWartosci()   ##
#
#     def dodawanie(self):
#         print(self.a + self.b)
#
#     def odejmowanie(self):
#         print(self.a - self.b)
#
#     def mnozenie(self):
#         print(self.a * self.b)
#
#     def dzielenie(self):
#         print( self.a / self.b)
#
#     def BWartosci(self):
#         if not isinstance(self.a, int):
#             raise BladWartosci("To nei jest liczba")  ##
#         if not isinstance(self.b, int):
#             raise BladWartosci("To nei jest liczba")
#
#
# try:
#     k1 = Kalkulator( 's',6)
#     k1.dzielenie()
# except ZeroDivisionError:
#     print("nie mozna dzielic przez 0")
# except BladWartosci:
#     print("nie mozna")
# else:
#     print("Wprowadziles dobre wartosci")
# finally:
#     print("koniec obliczen")


# Zadanie: System Zarządzania Pracownikami
# Stwórz prosty system zarządzania pracownikami w firmie, wykorzystując klasy danych (@dataclass). System powinien
# umożliwiać dodawanie nowych pracowników, ich listowanie, oraz obliczanie średniego wynagrodzenia w firmie.
#
# Wymagania:
# Stwórz klasę Employee, która będzie przechowywać informacje o pracowniku:
#
# Imię (name): string
# Wiek (age): int
# Stanowisko (position): string
# Wynagrodzenie (salary): float
# Stwórz klasę Company, która będzie zarządzać pracownikami:
#
# Lista pracowników (employees): lista obiektów klasy Employee.
# Metoda add_employee(employee: Employee): dodaje nowego pracownika do listy.
# Metoda list_employees(): wypisuje wszystkich pracowników firmy.
# Metoda average_salary(): zwraca średnie wynagrodzenie wszystkich pracowników.
# Napisz kod, który utworzy kilka obiektów klasy Employee, doda je do firmy, wyświetli listę pracowników oraz obliczy
# średnie wynagrodzenie.

# from dataclasses import dataclass
#
#
# @dataclass
# class Employee:
#     name: str
#     age: int
#     position: str
#     salary: float
#
# @dataclass
# class Company:
#     employees = []
#
#     def add_employees(self, employee):
#         self.employees.append(employee)
#
#     def list_employees(self):
#         for i in self.employees:
#             print(i.name)
#
#     def avarage_salary(self):
#         total = sum(i.salary for i in self.employees)
#         return total / len(self.employees)


# Zadanie: Symulacja Gry RPG z Obiektowością
# Stwórz prostą grę RPG, w której bohaterowie walczą z przeciwnikami. Każdy bohater i przeciwnik będzie mieć swoje
# statystyki i umiejętności. Wykorzystaj klasy i mechanizmy obiektowości, aby zaimplementować logikę gry.
#
# Wymagania:
# Stwórz klasę Character, która będzie bazową klasą dla bohaterów i przeciwników:
#
# Atrybuty: name, health, attack_power, defense.
# Metody:
# attack(target): Zmniejsza zdrowie celu (target) na podstawie mocy ataku atakującego i obrony celu.
# is_alive(): Zwraca True, jeśli zdrowie postaci jest większe niż 0, w przeciwnym razie False.
# Stwórz klasę Hero, która dziedziczy z Character i dodaje dodatkową funkcjonalność:
#
# Atrybuty:
# mana: Energia używana do rzucania czarów.
# Metody:
# cast_spell(target): Zmniejsza zdrowie celu o wartość równą podwójnej mocy ataku, jeśli bohater ma wystarczająco dużo many.
# Stwórz klasę Enemy, która dziedziczy z Character, i dodaj jej jakąś unikalną zdolność.
#
# Zasymuluj walkę między bohaterem a przeciwnikiem. Bohater i przeciwnik atakują się na zmianę, aż jeden z nich zostanie
# pokonany.

class Character:
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, target):
        att = self.attack_power - target.defense
        target.health -= att
        # target.health = self.attack_power - target.defense

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


class Hero(Character):
    def __init__(self, name, health, attack_power, defense, mana):
        super().__init__(health, attack_power, defense)
        self.mana = mana

    def cast_spell(self, target):
        target.health -= 2 * self.attack_power


class Enemy(Character):
    def text(self):
        print('Nigdy mnei nie pokonasz')


ch1 = Character("Ali", 100, 20, 40)
ch2 = Character("bibi", 100, 40, 60)

h1 = Hero("Ccc", 100, 15, 25, 3)
# print(h1.cast_spell(ch1))
print(ch1.attack(h1))

