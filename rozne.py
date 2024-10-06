# 1. Odwrócenie ciągu znaków
# Napisz funkcję, która przyjmuje ciąg znaków i zwraca go odwrócony.

def odw_ciagu(x):
    print(x[::-1])
odw_ciagu("abc")

# Sprawdzenie liczby pierwszej
# Napisz funkcję, która sprawdzi, czy dana liczba jest liczbą pierwszą.

def czy_parzysta(y):
    if y%2==0:
        print(f"Liczba {y} jest liczba parzysta.")
    else:
        print(f"Liczba {y} nie jest liczba parzysta.")

czy_parzysta(4)
czy_parzysta(5)

def czy_pierwsza(z):
    lista = []
    a=1
    while a <=z:
        if z%a==0:
            lista.append(a)
        a += 1
    if len(lista)==2:
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
        if k%2==0:
            suma+=k
    print(f" suma liczb parz wynosi {suma}")

suma_parz([2,3,4])

# 4. Znajdowanie anagramów
# Napisz funkcję, która sprawdza, czy dwa ciągi znaków są anagramami.

def czy_anagr(x,y):
    if sorted(x)==sorted(y):
        print("anagram")
    else:
        print("nie anagram")

czy_anagr("ala ma kota","ale makota")
czy_anagr("silent","listen")

# 5. Zliczanie słów w tekście
# Napisz funkcję, która zlicza liczbę wystąpień każdego słowa w danym tekście.

#  Suma liczb w macierzy
# Napisz funkcję, która zwraca sumę wszystkich liczb w macierzy 2D.

def suma(matr):
    suma = 0
    for row in matr:
        for i in row:
            suma+=i
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

lista = ['ada','adam','ola','ada','ada','adam']


def zlicz(lista):
    lista2 = []
    for i in lista:
        ilosc=lista.count(i)
        a = f"{i}:{ilosc}"
        lista2.append(a)
        #if a not in lista2
    dupp_usun = set(lista2)
    return dupp_usun

print(zlicz(lista))


# 9. Znajdowanie najdłuższego wspólnego prefiksu
# Napisz funkcję, która znajduje najdłuższy wspólny prefiks z listy ciągów znaków.

lista=['abcaaaa','abcabbb','abccccc']

def znajdz_pref(z):
    a =0
    lista2 = []
    while a<=len(z[0]):
        for i in z:
            znak = i[a]
            znak2 = f"{a}:{znak}"
            lista2.append(znak2)
        a+=1
    return lista2

print(znajdz_pref(lista))