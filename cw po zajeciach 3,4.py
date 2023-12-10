# b = 1234564.569
# print(f"hahha {b:.2f} and {b:,f}")
# a = 10
# klucze = {"A", "B"}
# dict1 = dict()
# dict1 = dict.fromkeys(klucze)
# print(dict1)
# klucze = {"a","b"}
# wartosci = ['app','bone']
# dict_my = dict.fromkeys(klucze,wartosci)
# print(dict_my)
# print(dict_my.get("b"))
# print(dict_my.get("c","nie ma"))
# dict_my.update([("M","T"),("mama","tata")])
# print(dict_my)
# import random
# lista = [ 1,2,3,4,5,6]
# print(random.choices(lista,k = 2))
# print(random.sample(lista,k =2))

# a = input("alfobet :")
# match a:
#     case "a":
#         print('ala')
#     case 'b':
#         print("bob")
#     case _:
#         print("ajsuadhk")

# for n in enumerate(a, start=10):
#     print(n)
# for n,l in enumerate(a, start=10):
#     print(n,l)


# lista1 = ["O","A"]
# lista2 = ["ola", "ala"]
# for i in zip(lista1, lista2):
#     print(i)
# for i,j in zip(lista1, lista2):
#     print(i,j)

# for i in dict_my.keys():
#     print(i)
# for i in dict_my:
#     print(i)
# for i in dict_my.values():
#     print(i)

# for i in range (5):
#     try:
#         print(5/i)
#     except ZeroDivisionError:
#         print("nie dziel przez 0")
#     except Exception as i:
#         print('hduhduh')
#     else:
#         print("uf tu nei bylo zera")
#     print("koniec")

# import datetime
# today = datetime.date.today()
# print(today)
# full = datetime.datetime.now()
# print(full)
# tomorrow = datetime.date.today() +datetime.timedelta(days = 1)
# print(tomorrow)

# with open("moj_plik","a") as a:
#     a.write("mąż")
#     a.write("2")
# with open("moj_plik","r") as a:
#     b = a.read()
#     print(b)
# with open("moj_plik","x") as a:
#     a.write("hello")

# import chardet
# with open("moj_plik","rb") as a:
#     tekst = a.read()
# result = chardet.detect(tekst)
# print(result)
# kodowanie = result["encoding"]
# print(kodowanie)
# nowy_tekst = tekst.decode(encoding=kodowanie)
# print(nowy_tekst)

# import csv
# lista = [1,2,3,4,5,6,7,8,9,'a','b','c']
# with open("fcsv.csv",'w') as plik_csv:
#     tekst = csv.writer(plik_csv)
#     nowy = tekst.writerow(lista)
#
# all_slownik = [
#     {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': '0'},
#     {'name': 'tomek', 'branch': 'cos', 'year': '3', 'cgpa': '8'},
#     {'name': 'zenek', 'branch': 'cot', 'year': '3.9', 'cgpa': '9'},
#     {'name': 'marek', 'branch': 'coe', 'year': '11', 'cgpa': '1.5'},
#     {'name': 'arek', 'branch': 'cow', 'year': '8', 'cgpa': '0.2'},
# ]
#
# import csv
# # naglowki = ['name', 'branch', 'year', 'cgpa']
# # with open("slownik.csv","w") as slow:
# #     reader = csv.reader(slow)
# #     dopiska = csv.DictWriter(slow,fieldnames=naglowki)
# #     dopiska.writeheader()
# #     dopiska.writerows(all_slownik)
# #     znak = csv.Sniffer.sniff(slow.read(1024))
# #     print(znak.delimiter)
#
# with open("slownik.csv", "r") as slow:
#     znak = csv.Sniffer().sniff(slow.read(1024))
#     print(znak.delimiter)
#
# def fun1():
#     print("To jest fun1")
#
#     def fun2():
#         print("To jest funkcja fun2")
#
#     return
#
#
# # a = fun1()
# # a()
# fun1()
# fukcja = fun1()
# fukcja()

#
# def restauracja(typ_zamowienia):
#     print("Witamy w naszej restauracji")
#
#     def zamow_pizze(skladniki="pieczarki"):
#         print("Zamówiona pizza, składniki: ", skladniki)
#
#     def zamow_napoj(nazwa="herbata"):
#         print("Zamow napoj", nazwa)
#
#     if typ_zamowienia.lower() == 'pizza':
#         return zamow_pizze
#     else:
#         return zamow_napoj  # zwracam adres funkcji
#
#
# zamowienie_pizza = restauracja('pizza')
# zamowienie_napoj = restauracja('napoj')

# def sumuj (*args):
#     # print((a + *))
#     suma = 0
#     for i in args:
#         suma += i
#     print(suma)
# lista = [1,2,3,4]
# sumuj(1,2,3,4)
# # sumuj(lista)

