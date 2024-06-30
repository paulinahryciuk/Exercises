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

text = '''
3
Kryszna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
'''

text2 = text.replace(" ",",")
print(text2)
licz_osob = text2[1]
print(f"liczba osob to {licz_osob}")
# a =text2[::-1].find("\n"")
# print(a)
