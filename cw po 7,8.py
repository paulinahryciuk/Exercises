# import json
#
# # with open("plik_j.json","w") as f:
# #     #tekst = json.load(f)
# #     json.dump("moj_j",f,"w",indent=4)
#
# slownik = {"name":"Paulina", "wiek": 33, "city": "Krakow"}
# with open("plik_j.json",'w') as file:
#     json.dump(slownik,file,indent=4)
#
# with open("plik_j.json", 'r') as file2:
#     a =json.load(file2)
#     b = a["name"]
# print(a)
# print(b)
# #
# # slownik2 = {"name":"Pau", "wiek": 30, "city": "Krak"}
# # with open("plik_j.json",'w') as file2:
# #     c = json.dump(file2)
#
# with open("new_file_js.json","w") as ft:
#     json.dump(a,ft)
#
#
# ob_js={
#   "message": "success",
#   "people": [
#     {
#       "name": "Jasmin Moghbeli",
#       "craft": "ISS"
#     },
#     {
#       "name": "Andreas Mogensen",
#       "craft": "ISS"
#     },
#     {
#       "name": "Satoshi Furukawa",
#       "craft": "ISS"
#     },
#     {
#       "name": "Konstantin Borisov",
#       "craft": "ISS"
#     },
#     {
#       "name": "Oleg Kononenko",
#       "craft": "ISS"
#     },
#     {
#       "name": "Nikolai Chub",
#       "craft": "ISS"
#     },
#     {
#       "name": "Loral O'Hara",
#       "craft": "ISS"
#     }
#   ],
#   "number": 7
# }
#
# aa = json.dumps(ob_js)
# print(aa)


# import requests  # słuzy do komunikacji http w pythonie
# from pydantic import BaseModel  # serializacja danych typu json, bazy danych , podobne
# from typing import List
#
# url = 'http://api.open-notify.org/astros.json'
# odp = requests.get(url)
# print(odp)
#
# print(odp.text)
# print("-------------------------")
# print(odp.json())

# import pakiet_cw
# pakiet_cw.powitanie()

# class Slown(dict):
#
#     def __missing__(self, key):
#        self[key] =0


# class KL:
#
#     def Met(self):
#         return ("test")
#
# k1 = KL()
# assert "test" == k1.Met()
# assert "test2" == k1.Met()


# class Punkt:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#     def wyswietl(self):
#         return (self.x,self.y)
#
#     def move(self,a,b):
#         self.x += a

    # def reset(self):
        # self.x = 0
        # self.move(-15,0)


    # def __str__(self):
    #     return f"({self.x, self.y})"

    # def __repr__(self):
    #     return f"({self.x, self.y})"

    # def __str__(self):
    #     lista = []
    #     lista.append(self.x)
    #     lista.append(self.y)
    #     # return f"({lista})"

#     def __repr__(self):
#         return f"({self.x, self.y})"
#
# pkt1 = Punkt(2,3)
# # print(pkt1.wyswietl())
# # print(pkt1)
#
# pkt2 = Punkt(5,6)
# lista = [pkt2,pkt1]
# print(lista)
# print("--------")
#
# pkt2.move(10,10)
# print(pkt2.wyswietl())
# print(pkt2)
# # pkt2.reset()
# print(pkt2)
#
# print('---------')
# print(pkt2.__class__.__name__)
# print(pkt2.__class__.__mro__)

# dictio = {"A":'a',"B":"b"}
# class Slownik(dict):
#     def __init__(self,x= dictio):
#         self.x = x
#     def __missing__(self, key):
#         return "nie ma"
# #     # def __init__(self,x=dictio):
# sl = Slownik()
# print(sl.x)
# # # sl = {"A":'a',"B":"b"}
# # print(type(sl))
# # print(sl)
# print(sl.get('name'))
# print(sl["A"])
# print(sl["name"])

# class Litery:
#     def zwroc(self):
#         print("hello")
#
# xxx = Litery()
# # xxx = "goodbye"
#
# assert "goodbye" == xxx.zwroc()

# x = "hello"
#
#
#
# x = "goodbye"
#
# # assert "hello" == 'x'
# if assert "goodbye" == x:
#     return "hello"


# class A:
#     def meto(self):
#         print("AAA")
#
# class B:
#     def meto(self):
#         print("BBB")
#
# class C(B,A):
#     def meto(self):
#         # A.meto(self)
#         super().meto()
#         print("i jeszcze to")
#
# c1 = C()
# c1.meto()
# print(c1.__class__.__mro__)

#########################################https://www.youtube.com/watch?v=PIKiHq1O9HQ



# from dataclasses import dataclass
#
# @dataclass
# class Person:
#     wiek: int
#     wzrost: int
#     pseudo: str
#
#
# Romek = Person(20,200,"Ro")
# print(Romek.pseudo)
# print(Romek)

# slownik = {"A":"a", "B":"b"}
# import pickle
# with open("slow_pikl.pikle",'wb') as file:
#     pickle.dump(slownik,file)
#
# # with open("slow_pikl.pikle",'rb') as file2:
# #     pickle.load(file2)
# #     print(file2)
# # with open("slow_pikl.pikle",'rb') as file2:
# # pf = pickle.load(file2)
# # print(pf)
# # pf = pickle.loads(file2)
# # print(pf)
# with open("slow_pikl.pikle",'rb') as file2:
#     pf = pickle.load(file2)
# print(pf)

# class Exp_zero(Exception):
#     def __init__(self, tresc):
#         super().__init__(tresc)
#
# try:
#     x = int(input("Podaj x"))
#     y = int(input("Podaj y"))
#     # print(x/y)
#     if y ==0:
#         raise Exp_zero("zero ??")
#     print(x / y)
# except Exp_zero:
#     print("nie mozna dzielic przez 0")
# else:
#     print("na szczescie nei podales 0")
# finally:
#     print("Koniec obliczen")
#
# lista = [1,2,3,4,5,6,7,8,9]
# iterator = iter(lista)
# # print(iterator)
# print(next(iterator))
# print("pauza")
# print(next(iterator))

class Bomba:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __iter__(self):
        return self

B1 = Bomba(1,6)
print(next(B1))