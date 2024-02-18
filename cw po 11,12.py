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

#
# from sqlalchemy import (
#     Column, Integer, String, ForeignKey, create_engine
# )
#
# from sqlalchemy.orm import relationship, sessionmaker, declarative_base
#
# Base = declarative_base()
#
# class Person(Base):
#     __tablename__ = 'osobki'
#     id = Column (Integer, primary_key = True)
#     imie  = Column(String)
#     nazwisko = Column(String)
#     wiek = Column(Integer)
#     miejsce = relationship('Adress',
#                            back_populates='person',
#                            cascade='all, delete-orphan')
#
# class Adress(Base):
#     __tablename__ = 'miasta'
#     id = Column(Integer, primary_key = True)
#     miasto = Column(String)
#     person_id = Column(ForeignKey('osobki.id'))
#     person = relationship('Person',back_populates='miejsce')
#
# engine = create_engine('sqlite:///zamieszkanie2.db')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()
#
# ala = Person(imie = "Ala",nazwisko = "kkk",wiek = 20)
# ola = Person(imie = "Ola",nazwisko = "mmm",wiek = 30)
# ala.miejsce = [Adress(miasto ='krakow')]
# ola.miejsce = [Adress(miasto ='wawa'),
#              Adress(miasto = 'lodz')]
#
# session.add(ala)
# session.add(ola)
# # session.add(ola_adres)
# # session.add(ala_adres)
#
# session.commit()
#
# users = session.query(Person.imie).all()
# print(users)


from sqlalchemy import (
    Column, Integer, String, ForeignKey, create_engine
)

from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()


class Owoc(Base):
    __tablename__ = 'owoce'
    id = Column(Integer, primary_key= True)
    nazwa = Column(String)
    # kolorek = relationship('Typ1', backref='owoc_kolor')
    # smaczek = relationship(('Typ2', backref= 'owoc_smak'))kolorek = relationship('Typ1', backref='owoc_kolor')
    kolorek = relationship('Typ1', back_populates='owoc_kolor', cascade='all, delete-orphan')
    smaczek = relationship('Typ2', back_populates= 'owoc_smak', cascade = 'all, delete-orphan')


class Typ1(Base):
    __tablename__ = 'typ1'
    id = Column(Integer, primary_key=True)
    kolor = Column(String)
    kolorek_id = Column(ForeignKey('owoce.id'))
    # owoc_kolor = Column(ForeignKey(Owoc, 'kolorek'))
    owoc_kolor = relationship('Owoc', back_populates='kolorek')


class Typ2(Base):
    __tablename__ = 'typ2'
    id2 = Column(Integer, primary_key=True)
    smak = Column(String)
    # owoc_smak = Column(ForeignKey(Owoc, 'smaczek'))
    smak_id = Column(ForeignKey('owoce.id'))
    owoc_smak = relationship('Owoc', back_populates='smaczek')


engine = create_engine('sqlite:///owoce.db')
Base.metadata.create_all(engine)
pierwszy = Owoc(nazwa='jablko')
drugi = Owoc(nazwa='banan')
trzeci = Owoc(nazwa='aronia')
pierwszy.kolorek = [Typ1(kolor='zielony')]
drugi.kolorek = [Typ1(kolor='zolty')]
trzeci.kolorek = [Typ1(kolor='cirmny')]
pierwszy.smaczek = [Typ2(smak='kwasny')]
drugi.smaczek = [Typ2(smak='slodki')]
trzeci.smaczek = [Typ2(smak='cierpki')]
Session = sessionmaker(bind=engine)
session = Session()
session.add(pierwszy)
session.add(drugi)
session.add(trzeci)
session.commit()
