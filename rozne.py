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

def dzialania(*args, **kwargs):
    mnozenie = 1
    dzielenie =1
    for i in args:
        mnozenie *= i
    # print(f"wynik mnozenia to: {wynik}")
    #     for k in kwargs.keys():
    #         if k == 'dzielnik':
    #             wynik_final = wynik / kwargs[k]
    #             print(f"wynik dzialania to: {wynik_final}")
    #         else:
    #             print(f"wynik mnozenia to: {wynik}")
    if 'dzielnik' in kwargs.keys():
        dzielenie=mnozenie/kwargs["dzielnik"]
        print(f"wynik dzialania to: {dzielenie}")
    else:
        print(f"wynik mnozenia to: {mnozenie}")

dzialania(2, 5, 6, a=5)
dzialania(2, 5, 6, a=5, dzielnik=10)

# Zadanie:
# Napisz program, który korzysta z funkcji reduce, aby:
# Obliczyć iloczyn wszystkich liczb w podanej liście.
# Znaleźć największą liczbę w tej liście.

lista = [2,3,6,9,2]
from functools import reduce

iloczyn = reduce(lambda a,b:a*b,lista)
print(iloczyn)
max = reduce(lambda a,b:a if a>b else b,lista)
print(f"max: {max}")

# Zadanie:
# Napisz dekorator, który zwiększa wartość wyniku o 10.

def zwiekszacz(funk):
    def wrapper(*args, **kwargs):
        result= funk(*args, **kwargs)
        return result +10
    return wrapper

@zwiekszacz
def suma(a,b):
    wynik = a+b
    return wynik


print(suma(1, 2))




# Zadanie: Odwracanie tekstu
# Napisz funkcję, która odwraca podany tekst.

def odwroc(tskst):
    print(tskst[::-1])

a = "ola ma kota"
odwroc(a)

# Zadanie: Liczenie samogłosek w tekście
# Napisz funkcję, która zlicza liczbę samogłosek w podanym tekście.

def licz_samogloski(x):
    liczba = 0
    liczba += x.count('a')
    liczba += x.count('i')
    liczba += x.count('o')
    liczba += x.count('y')
    liczba += x.count('e')
    print(liczba)

x = 'ala ma oko'
licz_samogloski(x)

# Rozbuduj funkcję tak, aby zwracała liczbę samogłosek i spółgłosek osobno.
def licz_spolg_i_samogl(x):
    samogl = 0
    for i in x:
        if i in ("aeiouyąęóAEIOUYĄĘÓ"):
            samogl+=1
    litery =0
    for i in x:
        if i.isalpha():
            litery+=1
    spolgl = litery- samogl
    print(f" w teksie wystepuje {samogl} samoglosek i {spolgl} spolglosek")

licz_spolg_i_samogl('ala ma oko')
