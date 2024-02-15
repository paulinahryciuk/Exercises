import sqlite3

try:
    polaczenie = sqlite3.connect("baza_ksiazkowa.db")
    kursor = polaczenie.cursor()
    print("baza podlaczona")

    # tabela = """
    # cre"""
    #
    # kursor.execute(tabela)
    # polaczenie.commit()

except polaczenie.Error as e:
    print(f"blad {e}")

finally:
    if polaczenie:
        polaczenie.close()
        print("polacznie zakmniete")