# 1. Odwrócenie ciągu znaków
# Napisz funkcję, która przyjmuje ciąg znaków i zwraca go odwrócony.

# def odw_ciagu(x):
#     print(x[::-1])
#
#
# odw_ciagu("abc")


# Sprawdzenie liczby pierwszej
# Napisz funkcję, która sprawdzi, czy dana liczba jest liczbą pierwszą.

# def czy_parzysta(y):
#     if y % 2 == 0:
#         print(f"Liczba {y} jest liczba parzysta.")
#     else:
#         print(f"Liczba {y} nie jest liczba parzysta.")
#
#
# czy_parzysta(4)
# czy_parzysta(5)


# def czy_pierwsza(z):
#     lista = []
#     a = 1
#     while a <= z:
#         if z % a == 0:
#             lista.append(a)
#         a += 1
#     if len(lista) == 2:
#         print(f"{z}:pierwsza")
#     else:
#         print(f"{z}:nie jest pierwsza")
#
#
# czy_pierwsza(3)
# czy_pierwsza(4)
# czy_pierwsza(20)
# czy_pierwsza(23)


# 3. Suma liczb parzystych
# Napisz funkcję, która zwraca sumę liczb parzystych z listy.

# def suma_parz(i):
#     suma = 0
#     for k in i:
#         if k % 2 == 0:
#             suma += k
#     print(f" suma liczb parz wynosi {suma}")
#
#
# suma_parz([2, 3, 4])


# 4. Znajdowanie anagramów
# Napisz funkcję, która sprawdza, czy dwa ciągi znaków są anagramami.

# def czy_anagr(x, y):
#     if sorted(x) == sorted(y):
#         print("anagram")
#     else:
#         print("nie anagram")
#
#
# czy_anagr("ala ma kota", "ale makota")
# czy_anagr("silent", "listen")


# 5. Zliczanie słów w tekście
# Napisz funkcję, która zlicza liczbę wystąpień każdego słowa w danym tekście.

#  Suma liczb w macierzy
# Napisz funkcję, która zwraca sumę wszystkich liczb w macierzy 2D.

# def suma(matr):
#     suma = 0
#     for row in matr:
#         for i in row:
#             suma += i
#     print(f"suma macierzy wynios: {suma}")
#
#
# matr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# suma(matr)

# 7. Fibonacci – dynamiczne programowanie
# Napisz funkcję, która zwraca n-ty element ciągu Fibonacciego, wykorzystując dynamiczne programowanie.

# 8. Sortowanie zliczające (Counting Sort)
# Napisz funkcję, która implementuje algorytm sortowania zliczającego.

# lista = ['ada', 'adam', 'ola', 'ada', 'ada', 'adam']
#
#
# def zlicz(lista):
#     lista2 = []
#     for i in lista:
#         ilosc = lista.count(i)
#         a = f"{i}:{ilosc}"
#         lista2.append(a)
#         # if a not in lista2
#     dupp_usun = set(lista2)
#     return dupp_usun
#
#
# print(zlicz(lista))

# 9. Znajdowanie najdłuższego wspólnego prefiksu WROCIC
# Napisz funkcję, która znajduje najdłuższy wspólny prefiks z listy ciągów znaków.

# lista=['abcaaaa','abcabbb','abccccc']
#
# def znajdz_pref(z):
#     a =0
#     lista2 = []
#     while a<=len(z[0]):
#         for i in z:
#             znak = i[a]
#             znak2 = f"{a}:{znak}"
#             lista2.append(znak2)
#         a+=1
#     return lista2
#
# print(znajdz_pref(lista))

# 8. Funkcje i praca z plikami
# Zadanie: Napisz funkcję, która odczytuje plik tekstowy i zwraca liczbę linii w tym pliku.

# with open('rozne_txt.csv', 'r') as text:
#     odczyt = text.readlines()
#     print(odczyt)
#     # print(odczyt.index(','))
#     print(len(odczyt))


# 9. Obsługa wyjątków
# Zadanie: Napisz funkcję, która dzieli dwie liczby, ale obsługuje wyjątek, gdy użytkownik podzieli przez zero.

# def podziel(a, b):
#     try:
#         wynik = a / b
#         # return wynik
#     except ZeroDivisionError:
#         print("Nie dzieli sie przes zero")
#     else:
#         print("dobrze ze pamietales ze nie dzielimy przez sero")
#         print(f"wynik:{wynik}")
#     finally:
#         print("koniec obliczen")
#
#
# podziel(4, 2)
# podziel(5, 0)


#################  STOS   ################
# Przykład 1: Zbalansowane nawiasy
# Sprawdź, czy dany ciąg nawiasów jest poprawnie zbalansowany. Użyj stosu.

# python
# Skopiuj kod
# def is_balanced(expression):
#     stack = []
#     for char in expression:
#         if char in "({[":
#             stack.append(char)
#         elif char in ")}]":
#             if not stack:
#                 return False
#             top = stack.pop()
#             if not ((top == '(' and char == ')') or
#                     (top == '{' and char == '}') or
#                     (top == '[' and char == ']')):
#                 return False
#     return not stack
#
#
# def is_balanced(expression):
#     stack = []  # stos do przechowywania otwierających nawiasów
#     for char in expression:
#         if char in "({[":  # sprawdzamy otwierające nawiasy
#             stack.append(char)
#         elif char in ")}]":  # sprawdzamy zamykające nawiasy
#             if not stack:  # jeśli stos jest pusty, to mamy błąd
#                 return False
#             top = stack.pop()  # zdejmujemy ostatni otwierający nawias
#             if not ((top == '(' and char == ')') or
#                     (top == '{' and char == '}') or
#                     (top == '[' and char == ']')):  # sprawdzamy dopasowanie par
#                 return False
#     return not stack  # jeśli stos jest pusty na koniec, nawiasy są zbalansowane


# def balans(ciag):
#     stos = []
#     for i in ciag:
#         if i in "({[":
#             stos.append(i)
#         elif i in ")}]":
#             stos.append(i)
#         else:
#             print("Nie ma nawiasow")
#     for x in stos:
#         if x == "(":
#             if ")" in stos:
#                 stos.remove("(")
#                 stos.remove(")")
#             # else:
#             #     print("Nnie jest zachowany balan nawiasow")
#
#     for x in stos:
#         if x == "[":
#             if "]" in stos:
#                 stos.remove("[")
#                 stos.remove("]")
#             # else:
#             #     print("Nnie jest zachowany balan nawiasow")
#
#     for x in stos:
#         if "{" in stos:
#             if x == "}":
#                 stos.remove("{")
#                 stos.remove("}")
#             # else:
#             # print("Nnie jest zachowany balan nawiasow")
#     # print(f"stos:{stos}")
#     if len(stos) == 0:
#         print("balans nawiasow zosatl zachowany")
#     else:
#         print("balans nawiasow nie zosatl zachowany")
#
#
# balans(")([]")
# balans(")([")
# balans(")([}")

# Przykład 2: Najdłuższy wspólny podciąg (dynamiczne programowanie)
# Znajdź długość najdłuższego wspólnego podciągu dla dwóch ciągów znaków.

# a = 'abcdef'
# b = 'hhhhhuuuudeffff'

# for x in a:
#     if x in b:
#         l=a[x]
#         print(l)


# Przykład 3: Problem "Two Sum"
# Znajdź dwie liczby w liście, które sumują się do podanej wartości.

# import copy

# lista1 = [0, 1, 2, 3, 4, 5]
# suma = 4
#
#
# def spr_sume(suma, lista1):
#     for i in lista1:
#         lista2 = []
#         # lista2=copy.copy(lista1)
#         lista2 = lista2 + lista1
#         lista2.remove(i)
#         wartosc = int(suma) - int(i)
#         if wartosc in lista2:
#             print(f"{suma} rowna sie sumie liczb {i} i {wartosc}")
#     print("koniec obliczen")
#
#
# spr_sume(suma, lista1)


# trojkat pascala
#
#             1
#            1  1
#         1    2   1
#       1    3   3   1

# def trojkat(n):
#     for i in range(1, 1 + n):
#         print(i * "1")
#
#
# def trojkat_pascala(n):
#     rzad = [1]
#     for i in range(n):
#         print(rzad)
#         nowy_rzad = [1] + [rzad[j] + rzad[j + 1] for j in range(len(rzad) - 1)] + [1]
#         rzad = nowy_rzad
#
#
# trojkat(3)
# trojkat_pascala(3)
# trojkat_pascala(5)

# Znajdowanie maksimum w liście
# Napisz funkcję, która zwróci maksymalny element w liście bez użycia wbudowanej funkcji max().

lista = [3, 1, 4, 1, 5, 9]


# def znajdz_najwiekszy(lista):
#     # for i in lista:
#     #     for k in range(0,(len(lista)-2)):
#     #         if lista[k]>lista[k+1]:
#     #             lista.remove(lista[k+1])
#     #         else:
#     #             lista.remove(lista[k])
#     # print(f"max: {lista}")
#
#     for k in range(1,(len(lista))):
#             if lista[k]>lista[k-1]:
#                 # lista.remove(lista[k-1])
#             else:
#                 lista.remove(lista[k])
#     print(f"max: {lista}")
#
# znajdz_najwiekszy(lista)

# def znajdz_max(lista):
#     max = lista[0]
#     for k in range(1, len(lista)):
#         if lista[k] > max:
#             max = lista[k]
#     print(f"max: {max}")
#
#
# znajdz_max(lista)


# Zadanie: Napisz funkcję suma_cyfr(n), która przyjmuje liczbę całkowitą i zwraca sumę jej cyfr (np. dla 123 zwróci 6,
# bo 1 + 2 + 3 = 6).

# def suma_cyfr(n):
#     lista = []
#     dl = len(str(n))
#     for i in range(0, dl):
#         cyfra = str(n)[i]
#         lista.append(cyfra)
#         wynik = 0
#     for n in lista:
#         wynik += int(n)
#     print(wynik)
#
#
# suma_cyfr(123)
# suma_cyfr(15)

# Zadanie: Napisz program, który przyjmuje od użytkownika zdanie, a następnie wyświetla liczbę słów w zdaniu.

# def ile_slow_w_zd(n):
#     if len(n)>0:
#         liczba = 1
#         czyste =n.strip()
#         a= czyste.count(" ")
#         liczba+=a
#     print(f"slow w zdanie: {liczba}")
#
#
# ile_slow_w_zd("Ola ma kota.")
# ile_slow_w_zd("  Ola ma kota.")

# Zadanie: Napisz program, który prosi użytkownika o podanie liczby, a jeśli użytkownik wpisze coś innego,
# program wyświetla wiadomość o błędzie i prosi o poprawne dane.

# while True:
#     try:
#         liczba = input("Podaj liczbe: ")
#     # except liczba is digit:
#     # except liczba.isdigit():
#         if not liczba.isdigit():
#             raise ValueError("To nie jest liczba calkowita")
#     except ValueError:
#         print("Sprobuj jeszcze raz")
#     else:
#         print(f"liczba: {liczba}")
#         break
#     # finally:
#     #     print("KOniec obliczen")


# Napisz program, który pobiera od użytkownika listę imion, a następnie wyświetla każde imię z przypisanym do niego
# numerem porządkowym.

# lista_imion = []
# while True:
#     imie = input('''Podaj imie
# (Aby zakonczyc wybierz 1):''')
#     if imie==str(1):
#         break
#     lista_imion.append(imie)
#
#
# for i in enumerate(lista_imion,start=1):
#     print(i)


# Funkcje anonimowe i lambdy:
#
# Zadanie: Użyj lambda, map i filter, aby w liście liczb [1, 2, 3, 4, 5, 6, 7, 8, 9] znaleźć liczby parzyste, a następnie podnieść je do kwadratu.
# List Comprehensions:
#
# Zadanie: Napisz list comprehension, który wygeneruje listę kwadratów liczb od 1 do 10.
# Praca z plikami:
#
# Zadanie: Napisz program, który tworzy plik tekstowy liczby.txt i zapisuje w nim liczby od 1 do 20. Następnie otwiera plik i wyświetla jego zawartość.
# Poziom Zaawansowany
# Klasy i obiekty (OOP):
#
# Zadanie: Napisz klasę Samochod, która ma atrybuty marka, model, rok. Klasa powinna mieć metodę opis, która zwraca opis samochodu w formie: "Marka: ... Model: ... Rok: ...".
# Iteratory i generatory:
#
# Zadanie: Napisz generator fib, który generuje liczby Fibonacciego do określonej liczby (np. do 100). Użyj go, aby wypisać liczby Fibonacciego w zakresie do 100.
# Dekoratory:
#
# Zadanie: Napisz dekorator logowanie, który wyświetla informacje o nazwie wywołanej funkcji oraz o jej argumentach. Użyj dekoratora, aby "ozdobić" przykładową funkcję przywitaj(imie).
# Rekurencja:
#
# Zadanie: Napisz funkcję rekurencyjną, która oblicza n-ty element ciągu Fibonacciego.
# Zaawansowane sortowanie:
#
# Zadanie: Napisz program, który sortuje listę słowników według określonego klucza. Lista zawiera słowniki z informacjami o osobach, np.: osoby = [{'imie': 'Adam', 'wiek': 30}, {'imie': 'Ewa', 'wiek': 25}]. Posortuj według wieku.
# Ekspert: Data Science i Machine Learning (opcjonalne)
# NumPy – operacje na tablicach:
#
# Zadanie: Używając biblioteki NumPy, utwórz macierz 3x3 wypełnioną losowymi liczbami. Następnie znajdź sumę wszystkich elementów w macierzy.
# Pandas – analiza danych:
#
# Zadanie: Utwórz DataFrame z listą danych o pracownikach, np. kolumny "Imię", "Wiek", "Stanowisko". Zastosuj filtrowanie, aby znaleźć wszystkich pracowników w wieku powyżej 30 lat.
# Wizualizacja – Matplotlib:
#
# Zadanie: Stwórz wykres słupkowy pokazujący liczbę osób w różnych grupach wiekowych (np. 20-30, 31-40, 41-50). Skorzystaj z biblioteki Matplotlib.
# Uczenie maszynowe – klasyfikacja:
#
# Zadanie: Użyj scikit-learn do stworzenia prostego modelu klasyfikacyjnego, np. drzewa decyzyjnego, które na podstawie zestawu danych klasyfikuje gatunki kwiatów Iris (korzystając z wbudowanego zestawu danych load_iris).
# Natural Language Processing (NLP):
#
# Zadanie: Użyj nltk do przetworzenia tekstu, np. zdania: "Python jest świetnym językiem!". Przetwórz tekst do formatu tokenów, usuń tzw. "stop words" i wykonaj stemming.


# Zadanie:
# Napisz program, który przyjmuje zdanie od użytkownika, a następnie wypisuje każdą literę tego zdania wraz z jej pozycją
# w tekście. Numerowanie liter powinno zaczynać się od 1, a spacje należy pominąć.

# tekst = input("Podaj zdanie: ")
# # tekst2 = tekst.strip(" ")
# tekst2 = tekst.replace(" ","")
# print(tekst2)
# print(list((enumerate(tekst2, 1))))
#
# for i,j in enumerate(tekst2,1):
#     print(f"{i} : {j}")


# Zadanie: Użyj lambda, map i filter, aby w liście liczb [1, 2, 3, 4, 5, 6, 7, 8, 9] znaleźć liczby parzyste,
# a następnie podnieść je do kwadratu.

# lista= [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # lambda x: x^x
# # filter(x%2==0)
# # map(lambda x: x^x),filter(x%2==0))
#
# parzyste = filter(lambda x: x%2==0,lista)
# kwadrat = list(map(lambda x: x**2, parzyste))
#
# print(kwadrat)

# List Comprehensions:
# Zadanie: Napisz list comprehension, który wygeneruje listę kwadratów liczb od 1 do 10.

# kwad = [x**2 for x in range(1,11)]
# print(kwad)

# Praca z plikami:
# Zadanie: Napisz program, który tworzy plik tekstowy liczby.txt i zapisuje w nim liczby od 1 do 20. Następnie otwiera
# plik i wyświetla jego zawartość.

# liczby = "liczby"
# # for x in range (1,21):
# #     lista.append(x)
#
# with open("liczby.txt","w") as ft:
#     ft.write(liczby)
#
# with open("liczby.txt","w") as ft:
#     for x in range(1,21):
#         ft.write(str(x))
#         ft.write("\n")
#
#
# with open("liczby.txt","r") as ft:
#     zawartosc = ft.read()
#     print(zawartosc)

# Klasy i obiekty (OOP):
# Zadanie: Napisz klasę Samochod, która ma atrybuty marka, model, rok. Klasa powinna mieć metodę opis, która zwraca opis
# samochodu w formie: "Marka: ... Model: ... Rok: ...".

# class Samochod:
#     def __init__(self, marka, model, rok):
#         if __name__ == '__main__':
#             self.marka = marka
#             self.model = model
#             self.rok = rok
#
#     def opis(self):
#         print(f"Marka: {self.marka} Model: {self.model} Rok: {self.rok}")
#
#
# o1 = Samochod("Audi", "A1", 2000)
# o1.opis()

# Dekoratory:
# Zadanie: Napisz dekorator logowanie, który wyświetla informacje o nazwie wywołanej funkcji oraz o jej argumentach.
# Użyj dekoratora, aby "ozdobić" przykładową funkcję przywitaj(imie).


# def logowanie(funkcja):
#     print(f" Argumenty: {self.imie}")
#
#
# class Osoba:
#     def __init__(self, imie):
#         self.imie = imie
#
#
#     @logowanie
#     def Przywitaj(self):
#         print(f"Witaj {self.imie}")
#
#
#
# o2 = Osoba("ola")
# o2.przywitaj()


# Zadanie:
# Z danej listy liczb [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] wybierz tylko liczby podzielne przez 3, a następnie oblicz
# ich sześciany.

# liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# podzielne = list(filter(lambda x: x%3==0, liczby))
# print(podzielne)
# wynik = list(map(lambda x: x**3,podzielne))
# print(wynik)
#
# nowa = [x**3 for x in liczby if x%3==0]
# print(nowa)

# Zadanie:
# Stwórz słownik, który zawiera imiona jako klucze oraz ich wiek jako wartości. Następnie napisz program, który:
# Wyświetli wszystkie imiona osób starszych niż 18 lat.
# Doda nową osobę do słownika i wyświetli zaktualizowaną listę osób.

# osoby = {"ALa": 20, "Adam": 30, "Ola": 15}
# # if osoby.values>18:
# #     print(osoby.items())
#
# for j, k in osoby.items():
#     if k > 18:
#         print(j)
#
# osoby["Jan"] = 25
# print(osoby.keys())

# nowa = [i for i,j in osoby.items if j>18]
# print(nowa)

# Zadanie:
# Masz słownik z ocenami uczniów, gdzie klucz to imię ucznia, a wartość to lista ocen. Napisz program, który:
#
# Obliczy średnią ocen dla każdego ucznia i zapisze te wartości w nowym słowniku.
# Wyświetli imiona uczniów, którzy mają średnią ocen wyższą niż 4.0.

# dziennk = {
#     "Ala": [5, 5, 5, 5],
#     "Iga": [4, 4, 3, 3],
#     "Olaf": [6, 5, 4]
# }
#
#
# def policz_srednia(x):
#     suma = 0
#     # for i in dziennk.get(x):
#     for i in dziennk[x]:
#         suma += int(i)
#     srednia = suma / len(dziennk.get(x))
#     print(f"Srenia {x} wynosi: {srednia}")
#
#
# policz_srednia('Ala')
# policz_srednia('Olaf')

# Masz dwie listy: imiona uczniów oraz ich oceny końcowe. Napisz program, który połączy te dwie listy w słownik,
# gdzie imię ucznia jest kluczem, a jego ocena wartością. Użyj funkcji zip.

# imiona = ["Ania", "Jan", "Ola", "Marek"]
# oceny = [5, 4, 3, 5]
#
# baza = dict(zip(imiona, oceny))
# print(baza)

# Zadanie:
# Napisz program, który prosi użytkownika o podanie liczby i dzieli 100 przez tę liczbę. Obsłuż przypadki, gdy:
#
# Użytkownik nie poda liczby (wyjątek ValueError).
# Użytkownik poda 0, co spowoduje błąd dzielenia przez zero (ZeroDivisionError).


# liczba = input('Podaj liczbe: ')
# try:
#     wynik = 100 / int(liczba)
# except ValueError:
#     print("nie podales liczbu")
# except ZeroDivisionError:
#     print("nie dzielimy przez 0")
# else:
#     print(f"wynokL {wynik}")
# finally:
#     print("KOniec obliczen")


# Zadanie:
# Napisz funkcję, która przyjmuje dowolną liczbę argumentów pozycyjnych i nazwanych. Funkcja powinna:
#
# Wypisać sumę wszystkich argumentów pozycyjnych.
# Wyświetlić wszystkie argumenty nazwane w formacie klucz: wartość.

# def policz_sume(*args, **kwargs):
#     wynik = sum(args)
#     print(f"suma wynosi: {wynik}")
# def wyswietl(*args, **kwargs):
#     for k,v in kwargs.items():
#         print(f"{k} : {v}")
#
#
# policz_sume(2,4,6,a=3, b=7)
# wyswietl(2,4,6,a=3, b=7)

# Zadanie:
# Napisz funkcję, która przyjmuje dowolną liczbę argumentów pozycyjnych (*args) i nazwanych (**kwargs). Funkcja powinna:
#
# Pomnożyć wszystkie argumenty pozycyjne.
# Sprawdzić, czy w argumentach nazwanych (**kwargs) znajduje się klucz o nazwie "dzielnik". Jeśli tak, to podziel wynik
# mnożenia przez tę wartość i zwróć wynik dzielenia. Jeśli klucz nie istnieje, zwróć wynik mnożenia bez dzielenia.

# def dzialania(*args, **kwargs):
#     mnozenie = 1
#     dzielenie = 1
#     for i in args:
#         mnozenie *= i
#     # print(f"wynik mnozenia to: {wynik}")
#     #     for k in kwargs.keys():
#     #         if k == 'dzielnik':
#     #             wynik_final = wynik / kwargs[k]
#     #             print(f"wynik dzialania to: {wynik_final}")
#     #         else:
#     #             print(f"wynik mnozenia to: {wynik}")
#     if 'dzielnik' in kwargs.keys():
#         dzielenie = mnozenie / kwargs["dzielnik"]
#         print(f"wynik dzialania to: {dzielenie}")
#     else:
#         print(f"wynik mnozenia to: {mnozenie}")
#
#
# dzialania(2, 5, 6, a=5)
# dzialania(2, 5, 6, a=5, dzielnik=10)

# Zadanie:
# Napisz program, który korzysta z funkcji reduce, aby:
# Obliczyć iloczyn wszystkich liczb w podanej liście.
# Znaleźć największą liczbę w tej liście.

# lista = [2, 3, 6, 9, 2]
# from functools import reduce
#
# iloczyn = reduce(lambda a, b: a * b, lista)
# print(iloczyn)
# max = reduce(lambda a, b: a if a > b else b, lista)
# print(f"max: {max}")


# Zadanie:
# Napisz dekorator, który zwiększa wartość wyniku o 10.

# def zwiekszacz(funk):
#     def wrapper(*args, **kwargs):
#         result = funk(*args, **kwargs)
#         return result + 10
#
#     return wrapper
#
#
# @zwiekszacz
# def suma(a, b):
#     wynik = a + b
#     return wynik
#
#
# print(suma(1, 2))
#
#
# # Zadanie: Odwracanie tekstu
# # Napisz funkcję, która odwraca podany tekst.
#
# def odwroc(tskst):
#     print(tskst[::-1])
#
#
# a = "ola ma kota"
# odwroc(a)
#
#
# # Zadanie: Liczenie samogłosek w tekście
# # Napisz funkcję, która zlicza liczbę samogłosek w podanym tekście.
#
# def licz_samogloski(x):
#     liczba = 0
#     liczba += x.count('a')
#     liczba += x.count('i')
#     liczba += x.count('o')
#     liczba += x.count('y')
#     liczba += x.count('e')
#     print(liczba)
#
#
# x = 'ala ma oko'
# licz_samogloski(x)


# Rozbuduj funkcję tak, aby zwracała liczbę samogłosek i spółgłosek osobno.
# def licz_spolg_i_samogl(x):
#     samogl = 0
#     for i in x:
#         if i in ("aeiouyąęóAEIOUYĄĘÓ"):
#             samogl += 1
#     litery = 0
#     for i in x:
#         if i.isalpha():
#             litery += 1
#     spolgl = litery - samogl
#     print(f" w teksie wystepuje {samogl} samoglosek i {spolgl} spolglosek")
#
#
# licz_spolg_i_samogl('ala ma oko')


# Zadanie: System zarządzania kontami bankowymi
# Napisz klasę KontoBankowe, która będzie symulować proste konto bankowe.

# class KontoBankowe:
#     def __init__(self, nr_konta, wlasciciel, saldo):
#         self.nr_konta = nr_konta
#         self.wlasciciel = wlasciciel
#         self.saldo = saldo
#
#     def wplac(self, wplata):
#         self.saldo += wplata
#
#     def wyplac(self, wyplata):
#         if wyplata <= self.saldo:
#             self.saldo -= wyplata
#         else:
#             print("Nie masz wystarczajo srodkow na koncie")
#
#     def wyswietl_info(self):
#         print(f"Wlasicielem konta {self.nr_konta} jest {self.wlasciciel}, saldo wynosi: {self.saldo}")
#
# k1 = KontoBankowe(123456, 'Paula', 2000)
# k1.wplac(1000)
# k1.wyplac(200)
# k1.wyswietl_info()

# Zadanie: Zarządzanie pracownikami w firmie
# Napisz program w Pythonie, który zarządza danymi pracowników w firmie z użyciem klas i dziedziczenia.
#
# class Pracownik:
#     def __init__(self, imie, nazwisko, wynagrodzenie=3000):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.wynagrodzenie = wynagrodzenie
#
#     def wyswietl_inf(self):
#         print(f"Pracownik: {self.imie} {self.nazwisko} wynagrodznie: {self.wynagrodzenie}")
#
#     def podwyzka(self, kwota_podwyzki):
#         self.wynagrodzenie += kwota_podwyzki
#
#     def roczne_wynagrodzenie(self):
#         r_wynag = self.wynagrodzenie * 12
#         print(f"Roczne wynagrodzenie pracpwnika {self.imie} wynosi : {r_wynag   }")
#
#
# class Manager(Pracownik):
#     def __init__(self, imie, nazwisko, wynagrodzenie, dzial):
#         super().__init__(imie, nazwisko, wynagrodzenie)
#         self.dzial = dzial
#
#     def wyswietl_inf(self):
#         print(
#             f"Pracownik: {self.imie} {self.nazwisko} wynagrodznie: {self.wynagrodzenie}, dzial: {self.dzial}")
#
#     def zmien_dzial(self, nowy_dzial):
#         self.dzial = nowy_dzial
#
#
# class PracownikGodzinowy(Pracownik):
#     def __init__(self, imie, nazwisko, stawka):
#         super().__init__(imie, nazwisko)
#         self.stawka = stawka
#
#     def oblicz_wyplate(self, godziny):
#         self.wynagrodzenie = godziny * self.stawka
#
#     def wyswietl_inf(self):
#         print(f"Pracownik: {self.imie} {self.nazwisko} wynagrodznie: {self.wynagrodzenie}")
#
#
# p1 = Pracownik('Ala', 'B.')
# p1.wyswietl_inf()
# m1 = Manager("Jan", "z", 5000, 'importu')
# m1.wyswietl_inf()
# g1 = PracownikGodzinowy("Ela", 'I.', 25)
# g1.oblicz_wyplate(100)
# g1.wyswietl_inf()
# m1.zmien_dzial('reklamy')
# m1.wyswietl_inf()
# p1.podwyzka(1000)
# p1.wyswietl_inf()
# # Rozszerzenie 1: Dodanie metod do podwyżek i zmiany danych
# # Dodamy metodę podwyzka w klasie Pracownik oraz metodę zmien_dzial w klasie Manager, aby umożliwić modyfikację atrybutów obiektów.
#
# # Rozszerzenie 2: Klasa do zarządzania zespołem pracowników
# # Dodajmy klasę Firma, która będzie przechowywać listę pracowników i umożliwi zarządzanie nimi, np. dodawanie, usuwanie i wyświetlanie.
#
# class Firma:
#     def __init__(self, nazwa):
#         self.nazwa = nazwa
#         self.lista_pracow = []
#
#     def dodaj(self, pracownik):
#         self.lista_pracow.append(pracownik)
#
#     def usun(self,pracownik):
#         self.lista_pracow.remove(pracownik)
#
#     def wyswietl(self):
#         print(f"aktualna lisat pracownikow firmy {self.nazwa} to:{self.lista_pracow} ")
#
# f1 = Firma('ABC')
# f1.dodaj('Adam')
# f1.dodaj('Ola')
# f1.dodaj('Ala')
# f1.usun("Ola")
# f1.wyswietl()
#
# # Rozszerzenie 3: Dodanie rocznego wynagrodzenia
# # Możemy dodać metodę roczne_wynagrodzenie do klasy Pracownik, aby obliczać roczny dochód pracownika.
#
# p1.roczne_wynagrodzenie()



# Zadanie: System Biblioteczny
# Zadanie polega na stworzeniu prostego systemu bibliotecznego, który będzie umożliwiał zarządzanie książkami oraz użytkownikami biblioteki.

# class Ksiazka:
#     def __init__(self, tytul, autor, rok_wydania):
#         self.tytul = tytul
#         self.autor = autor
#         self.rok_wydanie = rok_wydania
#         self.dostepna = True
#
#     def wyswietl_info(self):
#         print(f"Ksiazka {self.tytul} autora {self.autor} rok wydanie {self.rok_wydanie} dostpenosc: {self.dostepna}")
#
# class Uzytkownik:
#     def __init__(self, imie, nazwisko):
#         self.imie = imie
#         self.nazwisko = nazwisko
#         self.wypozyczone_ksiazki = []
#
#     def wyswietl_wypozyczone(self):
#         # print(f"Uzytkownik {self.imie} {self.nazwisko} ma wypozyczone ksiazki: {self.wypozyczone_ksiazki}")
#         for i in self.wypozyczone_ksiazki:
#             print(i)
#     def wypozycz(self,tytul):
#         self.wypozyczone_ksiazki.append(tytul)
#         Ksiazka.dostepna = False
#
#     def oddaj(self, tytul):
#         self.wypozyczone_ksiazki.remove(tytul)
#         Ksiazka.dostepna = True
#
#
# class Biblioteka:
#     def __init__(self,nazwa):
#         self.nazwa = nazwa
#         self.lista_ksiazek = []
#         self.uzytkownicy = []
#
#     def dodaj_ksiazke(self,tytul):
#         self.lista_ksiazek.append(tytul)
#
#     def dodaj_uzytkownika(self,uzytkownik):
#         self.uzytkownicy.append(uzytkownik)
#
#     def wyswietl_dostepne_ksiazki(self):
#         print(f"Dostepne ksiazki to: {self.lista_ksiazek}")
#
# biblioteka = Biblioteka("Biblioteka Miejska")
#
# # Dodawanie książek
# ksiazka1 = Ksiazka("Harry Potter i Kamień Filozoficzny", "J.K. Rowling", 1997)
# ksiazka2 = Ksiazka("Władca Pierścieni", "J.R.R. Tolkien", 1954)
# biblioteka.dodaj_ksiazke(ksiazka1)
# biblioteka.dodaj_ksiazke(ksiazka2)
#
# # Dodawanie użytkownika
# uzytkownik1 = Uzytkownik("Jan", "Kowalski")
# biblioteka.dodaj_uzytkownika(uzytkownik1)
#
# # Wypożyczanie książki
# biblioteka.wyswietl_dostepne_ksiazki()
# uzytkownik1.wypozycz(ksiazka1)
#
# # Wyświetlanie po wypożyczeniu
# biblioteka.wyswietl_dostepne_ksiazki()
# uzytkownik1.wyswietl_wypozyczone()
#
# # Oddawanie książki
# uzytkownik1.oddaj(ksiazka1)
# biblioteka.wyswietl_dostepne_ksiazki()
#
# ksiazka1.wyswietl_info()
# uzytkownik1.wypozycz("Harry Potter i Kamień Filozoficzny")
# uzytkownik1.wyswietl_wypozyczone()
# uzytkownik1.wypozycz("Władca Pierścieni")
# uzytkownik1.wyswietl_wypozyczone()
# uzytkownik1.oddaj("Władca Pierścieni")
# uzytkownik1.wyswietl_wypozyczone()
# biblioteka.dodaj_ksiazke("xxx")
# biblioteka.dodaj_uzytkownika('uz2')
# biblioteka.wyswietl_dostepne_ksiazki()


# Zadanie: System rezerwacji stolików w restauracji
# Twoim zadaniem jest stworzenie systemu, który pozwala zarządzać rezerwacjami stolików w restauracji.

# class Stolik:
#     def __init__(self,numer, ile_os):
#         self.ile_os = ile_os
#         self.numer = numer
#         self.wolny = True
#         self.osoba_rezerwujaca = None
#
#
#     def rezerwuj_stolik(self,miejsc,imie):
#         # for x in self.number:
#         if self.wolny is True:
#             if miejsc <= self.ile_os:
#                 self.miejsc = miejsc
#                 self.imie = imie
#                 print("Stolik zarezerwowany")
#                 self.wolny = False
#                 self.osoba_rezerw = imie
#         else:
#             print("Stolik juz wczesniej zarezerwowony")
#
#
#     def odwolanie_rezerwacji(self,imie):
#         if self.wolny is False:
#             if imie == self.osoba_rezerw:
#                 self.wolny = True
#                 self.osoba_rezerwujaca = None
#                 print("Rezerwacja zostala odwolona")
#         else:
#             print("Nie irtnijeje taka rezerwacja")
#
#     def __str__(self):
#         if self.wolny is False:
#             return (f"Stolik numer {self.numer} jest zarezerpwany przez: {self.osoba_rezerwujaca}")
#         else:
#             return (f"Stolik numer {self.numer} jest wolny")
#
#
# class Restuaracja:
#     def __init__(self):
#         self.stoliki = []
#
#     def dodanie_stolika(self,numer, ile_os):
#         # self.ile_os = ile_os
#         # self.numer = numer
#         # wolny = True
#         nowy = Stolik(numer, ile_os)
#         self.stoliki.append(nowy)
#
#     def pokaz_wolne(self):
#         for i in self.stoliki:
#             if i.wolny:
#                 print(i)
#
# s1 = Stolik(1,2)
# s2 = Stolik(2,4)
# s1.rezerwuj_stolik(2,"Ala")
# s1.rezerwuj_stolik(2,"Ala")
# s1.odwolanie_rezerwacji("Ala")
# s1.rezerwuj_stolik(2,"Ala")
# s1.odwolanie_rezerwacji("Al")
# r1 = Restuaracja()
# r1.dodanie_stolika(3,3)
# r1.pokaz_wolne()



# Zadanie: System Zarządzania Kursami Online
# Stwórz system zarządzania kursami online, który pozwoli na:
#
# Dodawanie kursów do platformy.
# Rejestrowanie użytkowników na kursy.
# Wyświetlanie listy wszystkich dostępnych kursów.
# Wyświetlanie listy użytkowników zarejestrowanych na dany kurs.
# Usuwanie użytkownika z kursu.
class Kurs:
    def __init__(self,nazwa):
        self.nazwa = nazwa
        self.uczestnicy =[]

    # def dodaj_kurs(self,nazwa):
    #     Platforma.kursy.append(self.nazwa)
    #     print(f"Kurs {self.nazwa} zosatla dodany do listy kursow")
    #
    # def usun_kurs(self,nazwa):
    #     if self.nazwa in Platforma.kursy:
    #         Platforma.kursy.remove(self.nazwa)
    #         print(f"Kurs {self.nazwa} zosatl usuniety z listy kursow")
    #     else:
    #         print("Nie ma takiego kirsu na liscie")

#     def zapis(self, uczestnik):
#         if uczestnik in self.uczestnicy:
#             print("Uczetnik jest juz na liscie")
#         else:
#             print(f"{uczestnik} zpstal zapisane na kurs {self.nazwa}")
#             self.uczestnicy.append(uczestnik)
#
#     def wypis(self, uczestnik):
#         if uczestnik in self.uczestnicy:
#             self.uczestnicy.remove(uczestnik)
#             print(f"{uczestnik} zpstal wypisany z kursu {self.nazwa}")
#         else:
#             print("Uczestnik nei byl zapisany na ten kurs")
#
#     def wyswietl_liste(self):
#         print(f"Uczesrnicy kursu {self.nazwa} to {self.uczestnicy}")
#
#
# class Platforma:
#     """
#     System Zarządzania Kursami Online
#     """
#     def __init__(self):
#         self.kursy = []
#
#     def dodaj_kurs(self,nazwa):
#         if nazwa in self.kursy:
#             print("Taki kurs jzu jest na liscie")
#         else:
#             self.kursy.append(nazwa)
#             print(f"Kurs {nazwa} zosatla dodany do listy kursow")
#
#
#     def usun_kurs(self,nazwa):
#         if nazwa in self.kursy:
#             self.kursy.remove(nazwa)
#             print(f"Kurs {nazwa} zosatl usuniety z listy kursow")
#         else:
#             print("Nie ma takiego kursu na liscie")
#
#     def wyswietl(self):
#         for k in self.kursy:
#             print(f"Dostepny kurs: {k}")
#
#
# p1 = Platforma()
# p1.dodaj_kurs("jezykowy ang")
# p1.dodaj_kurs("jezykowy ang")
# p1.dodaj_kurs("jezykowy niem")
# p1.dodaj_kurs("jezykowy hisz")
# p1.usun_kurs("jezykowy hisz")
# p1.usun_kurs("jezykowy hisz")
# p1.wyswietl()
# k1 = Kurs("jezykowy niem")
# k1.zapis("Iza")
# k1.zapis("Iza")
# k1.zapis("Aga")
# k1.wyswietl_liste()
# k1.wypis("Iza")
# k1.wyswietl_liste()



# Zadanie: System Wypożyczalni Samochodów
#
# Twoim zadaniem jest stworzenie systemu zarządzania wypożyczalnią samochodów. System pozwala na:
#
# Dodawanie nowych samochodów do bazy wypożyczalni.
# Wypożyczanie samochodów klientom.
# Zwracanie samochodów po wypożyczeniu.
# Wyświetlanie listy dostępnych samochodów.
# Wyświetlanie historii wypożyczeń dla konkretnego samochodu.

# class Wypozyczalnia:
#     def __init__(self):
#         self.auta = []
#
#     def pokaz_baze(self):
#         print(f"Wszystkie samochody: {self.auta}")
#
#     def dodaj_auto(self,marka):
#         # self.marka = marka
#         nowe_auto = Auto(marka)
#         self.auta.append(nowe_auto)
#         print("Auto zostalo dodane do bazy")
#
#     def usun_auto(self,marka):
#         if marka in self.auta:
#             self.auta.remove(marka)
#             print("Auto usuniete z bazy")
#         else:
#             print("Nie ma takiego auta w bazie")
#
#     def pokaz_wolne(self):
#         print("Dostepne samochody:")
#         # if Auto.wolny:
#         #     # print(f"dostepne samochody to:{Auto.marka}")
#         for a in self.auta:
#             if a.wolny:
#                 print(a.marka)
#
#
#
# class Auto:
#     def __init__(self,marka):
#         self.marka = marka
#         self.wolny = True
#         self.histr=[]
#
#     def wypozycz(self,imie):
#         if self.wolny:
#             print("Samochod wypozyczony")
#             self.wolny=False
#             self.histr.append(f"wypozyczony przez {imie}")
#         else:
#             print("Samochod nir jest dostepny")
#
#     def zwroc(self,imie):
#         if self.wolny:
#             print("Ten samochod nie jes wypozyczony")
#         else:
#             print("Samochpd oddany")
#             self.wolny=True
#             self.histr.append(f"oddany przez {imie}")
#
#     def wyswietl_histr(self):
#         print(f"Histroia wypozyczen to: {self.histr}")
#
#
#
#
# w1 = Wypozyczalnia()
# w1.dodaj_auto('bmw')
# w1.dodaj_auto('audi')
# w1.dodaj_auto('ford')
# w1.dodaj_auto('ww')
# w1.usun_auto("audi")
# w1.pokaz_baze()
# w1.pokaz_wolne()
#
#
# a1 = Auto("bmw")
# a1.wypozycz("Ala")
# a1.wypozycz("Ola")
# a1.zwroc("Ala")
# a1.wypozycz("Ola")
# a1.wyswietl_histr()


# Zadanie: System Zarządzania Biblioteką
# Stwórz system zarządzania biblioteką, który pozwala na:
#
# Dodawanie książek do katalogu.
# Usuwanie książek z katalogu.
# Wypożyczanie książek przez użytkowników.
# Zwracanie książek.
# Wyświetlanie dostępnych książek.
# Wyświetlanie historii wypożyczeń dla danej książki.

class Ksiazka:
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor
        self.wolna = True
        self.historia = []

    def wypozycz(self, osoba):
        if self.wolna:
            print(f"Ksiazka {self.tytul} zostala wypozyczone przez {osoba}")
            self.wolna = False
            self.historia.append(f"wypozyczona przez {osoba}")
        else:
            print(f"Ksiazka {self.tytul} nie jest dostepna")

    def oddaj(self, osoba):
        if not self.wolna:
            print(f"Ksiazka oddana")
            self.wolna= True
            self.historia.append(f"oddana przez {osoba}")
        else:
            print("ksiazka nei byla wypozyczona")

    def wyswietl_historie(self):
        print("Historia wyporzyczen:")
        for i in self.historia:
            print(i)


class Biblioteka:
    def __init__(self):
        self.ksiazki = []

    def dodaj(self, tytul, autor):
        book = Ksiazka(tytul,autor)
        self.ksiazki.append(book)
        print(f"Ksiazka {tytul} zostala dodana do bazy")

    def usun(self, tytul):
        for x in self.ksiazki:
            if tytul==x.tytul:
                self.ksiazki.remove(x)
                print(f"ksiazka {tytul} zostala ususnieta z bazy")
        print("Nie ma takiej ksiazki w bazie, nei mozna ususnac")

    def wyswietl_dostepne(self):
        print("Dostepne:")
        for i in self.ksiazki:
            if i.wolna:
                print(i.tytul)

k1 = Ksiazka("Potop", "Sienkiewicz")
k1.wypozycz("Ola")
k1.wypozycz("Ala")
k1.oddaj("Ola")
k1.wyswietl_historie()

b1 = Biblioteka()
b1.dodaj("Ala ma kota","AB")
b1.dodaj("Ala ma kota","AB")
b1.dodaj("Atlas","DC")
b1.usun("A")
b1.usun("Atlas")
b1.wyswietl_dostepne()
