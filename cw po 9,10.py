# import sqlite3
# lista = [(4,'Ola'),
#          (5,'Basia'),]

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

#
# try:
#     # polaczenie = sqlite3.connect(':memory:')
#     polaczenie = sqlite3.connect('baza.db')
#     polaczenie2 = sqlite3.Row
#     kursor = polaczenie.cursor()
#     print("baza podloczona")
#
#     # query='''
#     # CREATE TABLE SqliteDB_developers (
#     # id INTEGER PRIMARY KEY,
    # name TEXT NOT NULL UNIQUE
    # );'''
    #
    # kursor.execute(query)
    # polaczenie.commit()

    # with open('tables.sql','r') as f:
    #     tabelka = f.read()
    #
    # kursor.executescript(tabelka)
    # polaczenie.commit()
    #
    # insert = '''
    # INSERT INTO SqliteDB_developers (id, name) VALUES (1, 'Ania');
    # '''
    #
    # insert2 = '''
    # INSERT INTO SqliteDB_developers (id, name) VAlues (2, 'Kasia');
    # '''
    # kursor.execute(insert)
    # kursor.execute(insert2)
    # polaczenie.commit()

    # select = '''
    # SELECT * FROM SqliteDB_developers;
    # '''
    # # kursor.execute(select)
    # for rows in kursor.execute(select):
    #     print(rows)

    # insert = '''
    # INSERT INTO SqliteDB_developers (id, name) VALUES (?,?);
    # '''
    # # kursor.execute(insert, (3,'Asia'))
    # # polaczenie.commit()
    # kursor.executemany(insert,lista)
    # polaczenie.commit()

    # delete = '''
    # DELETE from SqliteDB_developers WHERE name = 'Ola';
    # '''
    #
    # kursor.execute(delete)
    # polaczenie.commit()

#     update = '''
#     UPDATE SqliteDB_developers SET name = 'Ola' WHERE id = 3
#     '''
#
#     kursor.execute(update)
#     polaczenie.commit()
#
# except polaczenie.Error as e:
#     print("blad",e)
# finally:
#     if polaczenie:
#         polaczenie.close()
#         print("baza zamknieya")
#

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class User(Base):
    __table__ = 'tabeleczka'
    id = Column(Integer,primary_key = True)
    name = Column(String)
    age = Column(Integer)

engine = create_engine('sqlite:///moja_baza.db', echo=True)
Base.metadata.create_all(engine)






