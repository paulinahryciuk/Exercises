# 1. Odwrócenie ciągu znaków
# Napisz funkcję, która przyjmuje ciąg znaków i zwraca go odwrócony.

def odw_ciagu(x):
    print(x[::-1])


odw_ciagu("abc")


# Sprawdzenie liczby pierwszej
# Napisz funkcję, która sprawdzi, czy dana liczba jest liczbą pierwszą.

def czy_parzysta(y):
    if y % 2 == 0:
        print(f"Liczba {y} jest liczba parzysta.")
    else:
        print(f"Liczba {y} nie jest liczba parzysta.")


czy_parzysta(4)
czy_parzysta(5)


def czy_pierwsza(z):
    lista = []
    a = 1
    while a <= z:
        if z % a == 0:
            lista.append(a)
        a += 1
    if len(lista) == 2:
        print(f"{z}:pierwsza")
    else:
        print(f"{z}:nie jest pierwsza")


czy_pierwsza(3)
czy_pierwsza(4)
czy_pierwsza(20)
czy_pierwsza(23)


# 3. Suma liczb parzystych
# Napisz funkcję, która zwraca sumę liczb parzystych z listy.

def suma_parz(i):
    suma = 0
    for k in i:
        if k % 2 == 0:
            suma += k
    print(f" suma liczb parz wynosi {suma}")


suma_parz([2, 3, 4])


# 4. Znajdowanie anagramów
# Napisz funkcję, która sprawdza, czy dwa ciągi znaków są anagramami.

def czy_anagr(x, y):
    if sorted(x) == sorted(y):
        print("anagram")
    else:
        print("nie anagram")


czy_anagr("ala ma kota", "ale makota")
czy_anagr("silent", "listen")


# 5. Zliczanie słów w tekście
# Napisz funkcję, która zlicza liczbę wystąpień każdego słowa w danym tekście.

#  Suma liczb w macierzy
# Napisz funkcję, która zwraca sumę wszystkich liczb w macierzy 2D.

def suma(matr):
    suma = 0
    for row in matr:
        for i in row:
            suma += i
    print(f"suma macierzy wynios: {suma}")


matr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

suma(matr)

# 7. Fibonacci – dynamiczne programowanie
# Napisz funkcję, która zwraca n-ty element ciągu Fibonacciego, wykorzystując dynamiczne programowanie.

# 8. Sortowanie zliczające (Counting Sort)
# Napisz funkcję, która implementuje algorytm sortowania zliczającego.

lista = ['ada', 'adam', 'ola', 'ada', 'ada', 'adam']


def zlicz(lista):
    lista2 = []
    for i in lista:
        ilosc = lista.count(i)
        a = f"{i}:{ilosc}"
        lista2.append(a)
        # if a not in lista2
    dupp_usun = set(lista2)
    return dupp_usun


print(zlicz(lista))

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

with open('rozne_txt.csv', 'r') as text:
    odczyt = text.readlines()
    print(odczyt)
    # print(odczyt.index(','))
    print(len(odczyt))


# 9. Obsługa wyjątków
# Zadanie: Napisz funkcję, która dzieli dwie liczby, ale obsługuje wyjątek, gdy użytkownik podzieli przez zero.

def podziel(a, b):
    try:
        wynik = a / b
        # return wynik
    except ZeroDivisionError:
        print("Nie dzieli sie przes zero")
    else:
        print("dobrze ze pamietales ze nie dzielimy przez sero")
        print(f"wynik:{wynik}")
    finally:
        print("koniec obliczen")


podziel(4, 2)
podziel(5, 0)


#################  STOS   ################
# Przykład 1: Zbalansowane nawiasy
# Sprawdź, czy dany ciąg nawiasów jest poprawnie zbalansowany. Użyj stosu.

# python
# Skopiuj kod
def is_balanced(expression):
    stack = []
    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            top = stack.pop()
            if not ((top == '(' and char == ')') or
                    (top == '{' and char == '}') or
                    (top == '[' and char == ']')):
                return False
    return not stack


def is_balanced(expression):
    stack = []  # stos do przechowywania otwierających nawiasów
    for char in expression:
        if char in "({[":  # sprawdzamy otwierające nawiasy
            stack.append(char)
        elif char in ")}]":  # sprawdzamy zamykające nawiasy
            if not stack:  # jeśli stos jest pusty, to mamy błąd
                return False
            top = stack.pop()  # zdejmujemy ostatni otwierający nawias
            if not ((top == '(' and char == ')') or
                    (top == '{' and char == '}') or
                    (top == '[' and char == ']')):  # sprawdzamy dopasowanie par
                return False
    return not stack  # jeśli stos jest pusty na koniec, nawiasy są zbalansowane


def balans(ciag):
    stos = []
    for i in ciag:
        if i in "({[":
            stos.append(i)
        elif i in ")}]":
            stos.append(i)
        else:
            print("Nie ma nawiasow")
    for x in stos:
        if x == "(":
            if ")" in stos:
                stos.remove("(")
                stos.remove(")")
            # else:
            #     print("Nnie jest zachowany balan nawiasow")

    for x in stos:
        if x == "[":
            if "]" in stos:
                stos.remove("[")
                stos.remove("]")
            # else:
            #     print("Nnie jest zachowany balan nawiasow")

    for x in stos:
        if "{" in stos:
            if x == "}":
                stos.remove("{")
                stos.remove("}")
            # else:
            # print("Nnie jest zachowany balan nawiasow")
    # print(f"stos:{stos}")
    if len(stos) == 0:
        print("balans nawiasow zosatl zachowany")
    else:
        print("balans nawiasow nie zosatl zachowany")


balans(")([]")
balans(")([")
balans(")([}")

# Przykład 2: Najdłuższy wspólny podciąg (dynamiczne programowanie)
# Znajdź długość najdłuższego wspólnego podciągu dla dwóch ciągów znaków.

a = 'abcdef'
b = 'hhhhhuuuudeffff'

# for x in a:
#     if x in b:
#         l=a[x]
#         print(l)


# Przykład 3: Problem "Two Sum"
# Znajdź dwie liczby w liście, które sumują się do podanej wartości.

# import copy

lista1 = [0, 1, 2, 3, 4, 5]
suma = 4


def spr_sume(suma, lista1):
    for i in lista1:
        lista2 = []
        # lista2=copy.copy(lista1)
        lista2 = lista2 + lista1
        lista2.remove(i)
        wartosc = int(suma) - int(i)
        if wartosc in lista2:
            print(f"{suma} rowna sie sumie liczb {i} i {wartosc}")
    print("koniec obliczen")


spr_sume(suma, lista1)


# trojkat pascala
#
#             1
#            1  1
#         1    2   1
#       1    3   3   1

def trojkat(n):
    for i in range(1, 1 + n):
        print(i * "1")


def trojkat_pascala(n):
    rzad = [1]
    for i in range(n):
        print(rzad)
        nowy_rzad = [1] + [rzad[j] + rzad[j + 1] for j in range(len(rzad) - 1)] + [1]
        rzad = nowy_rzad


trojkat(3)
trojkat_pascala(3)
trojkat_pascala(5)

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

def znajdz_max(lista):
    max = lista[0]
    for k in range(1, len(lista)):
        if lista[k] > max:
            max = lista[k]
    print(f"max: {max}")


znajdz_max(lista)


# Zadanie: Napisz funkcję suma_cyfr(n), która przyjmuje liczbę całkowitą i zwraca sumę jej cyfr (np. dla 123 zwróci 6,
# bo 1 + 2 + 3 = 6).

def suma_cyfr(n):
    lista = []
    dl = len(str(n))
    for i in range(0, dl):
        cyfra = str(n)[i]
        lista.append(cyfra)
        wynik = 0
    for n in lista:
        wynik += int(n)
    print(wynik)


suma_cyfr(123)
suma_cyfr(15)

#Zadanie: Napisz program, który przyjmuje od użytkownika zdanie, a następnie wyświetla liczbę słów w zdaniu.

def ile_slow_w_zd(n):
    if len(n)>0:
        liczba = 1
        czyste =n.strip()
        a= czyste.count(" ")
        liczba+=a
    print(f"slow w zdanie: {liczba}")


ile_slow_w_zd("Ola ma kota.")
ile_slow_w_zd("  Ola ma kota.")
