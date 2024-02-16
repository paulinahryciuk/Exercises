# import sqlite3
#
# # try:
# #     polaczenie = sqlite3.connect("baza_ksiazkowa.db")
# #     kursor = polaczenie.cursor()
# #     print("baza podlaczona")
# #
# #     # tabela = """
# #     # cre"""
# #     #
# #     # kursor.execute(tabela)
# #     # polaczenie.commit()
# #
# # except polaczenie.Error as e:
# #     print(f"blad {e}")
# #
# # finally:
# #     if polaczenie:
# #         polaczenie.close()
# #         print("polacznie zakmniete")
# #
# #
# # from sqlalchemy import create_engine, Column, Integer, String
# # from sqlalchemy.orm import sessionmaker, declarative_base
# #
# # Base = declarative_base()
# # class User(Base):
# #     __table_name__ = 'tabela'
# #
# # engine = create_engine(baza)
# # Base.mets
#
# class ConMan:
#     def __init__(self,db_name):
#         self.db_name = db_name
#         self.polaczenie = polaczenie
#
#     def __enter__(self):
#         polaczenie = sqlite3.connect(self.db_name)
#         return self.polaczenie
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.polaczenie:
#             self.polaczenie.commit()
#             self.polaczenie.close()
#
#     with ConMan(db_name) as polaczenie:
#             kursor = polaczenie.cursor()
#             kursor.execute()


from sqlalchemy import (
    Column, Integer, String, ForeignKey, create_engine
)

from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Persor(Base):
    __tablename__ = 'osobki'
    imie  = Column(String, primary_key=True)
    nazwisko = Column(String)
    wiek = Column(Integer)