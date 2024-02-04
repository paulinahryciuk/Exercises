import sqlite3

# try:
#     conn = sqlite3.connect('baza.db')
#     cursor = conn.cursor
#     print('baza podl')
# except sqlite3.Error as e:
#     print("blad bazy danych",e)
# finally:
#     if conn:
#         conn.close()
#         print("baza zamkneita")


try:
    polaczenie = sqlite3.connect(':memory:')
    kursor = polaczenie.cursor()
    print("baza podloczona")
except polaczenie.Error as e:
    print("blad",e)
finally:
    if polaczenie:
        polaczenie.close()
        print("baza zamknieya")





