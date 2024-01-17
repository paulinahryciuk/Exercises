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


class KL:

    def Met(self):
        return ("test")

k1 = KL()
assert "test" == k1.Met()
assert "test2" == k1.Met()