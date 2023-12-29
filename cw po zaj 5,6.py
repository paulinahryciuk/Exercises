# print(list(map(lambda x: x+1, [1,21,5,3])))
# def fun1(x):
#     return x+1
#
# lista = [1,2,5]
#
# print(list(map(fun1,lista)))

# lista = list(range(1,21))
# # print(lista)
#
# def funkc(x):
#     return 1/x
#
# print(list(map(funkc,lista)))
#
# print(list(map(lambda x : 1/x,lista)))
#
# lista2 = list(range(1,101))
# print(list(filter(lambda x: x%3 == 0 and x%4 != 0, lista2)))

#
# lista = [2,3,2,5,5,6,6,7]
# from functools import reduce
# print(reduce(lambda x,y : y-x ,lista))

# x = int(input("Podaj liczbe calkowita: "))

# def sumuj_mniejsze(x):
#     calkowite = list(range(1, 10))
#     suma =0
#     for c in calkowite:
#         if c <x:
#             return c + suma
#     print(suma)

def sumuj_mniejsze(x):
    if x==0:
        return 0
    else:
        return x + sumuj_mniejsze(x-1)

print(sumuj_mniejsze(4))
