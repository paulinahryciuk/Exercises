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

#
# from sqlalchemy import (
#     Column, Integer, String, ForeignKey, create_engine
# )
#
# from sqlalchemy.orm import relationship, sessionmaker, declarative_base
#
# Base = declarative_base()
#
#
# class Owoc(Base):
#     __tablename__ = 'owoce'
#     id = Column(Integer, primary_key= True)
#     nazwa = Column(String)
#     # kolorek = relationship('Typ1', backref='owoc_kolor')
#     # smaczek = relationship(('Typ2', backref= 'owoc_smak'))kolorek = relationship('Typ1', backref='owoc_kolor')
#     kolorek = relationship('Typ1', back_populates='owoc_kolor', cascade='all, delete-orphan')
#     smaczek = relationship('Typ2', back_populates= 'owoc_smak', cascade = 'all, delete-orphan')
#
#
# class Typ1(Base):
#     __tablename__ = 'typ1'
#     id = Column(Integer, primary_key=True)
#     kolor = Column(String)
#     kolorek_id = Column(ForeignKey('owoce.id'))
#     # owoc_kolor = Column(ForeignKey(Owoc, 'kolorek'))
#     owoc_kolor = relationship('Owoc', back_populates='kolorek')
#
#
# class Typ2(Base):
#     __tablename__ = 'typ2'
#     id2 = Column(Integer, primary_key=True)
#     smak = Column(String)
#     # owoc_smak = Column(ForeignKey(Owoc, 'smaczek'))
#     smak_id = Column(ForeignKey('owoce.id'))
#     owoc_smak = relationship('Owoc', back_populates='smaczek')


# engine = create_engine('sqlite:///owoce.db')
# Base.metadata.create_all(engine)
# pierwszy = Owoc(nazwa='jablko')
# drugi = Owoc(nazwa='banan')
# trzeci = Owoc(nazwa='aronia')
# pierwszy.kolorek = [Typ1(kolor='zielony')]
# drugi.kolorek = [Typ1(kolor='zolty')]
# trzeci.kolorek = [Typ1(kolor='cirmny')]
# pierwszy.smaczek = [Typ2(smak='kwasny')]
# drugi.smaczek = [Typ2(smak='slodki')]
# trzeci.smaczek = [Typ2(smak='cierpki')]
# Session = sessionmaker(bind=engine)
# session = Session()
# session.add(pierwszy)
# session.add(drugi)
# session.add(trzeci)
# session.commit()


# from sqlalchemy import (
#     Column, Integer, String, ForeignKey, create_engine
# )
#
# from sqlalchemy.orm import relationship, sessionmaker, declarative_base
#
# Base = declarative_base()
#
#
# class Rodzic(Base):
#     __tablename__ = 'rodzice'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     dzieci = relationship('Dzieci', backref='rodz1')
#
#
# class Dzieci(Base):
#     __tablename__ = 'dzieci'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     rodzic_id = Column(Integer, ForeignKey('rodzice.id'))
#
#
# engine = create_engine('sqlite:///rodzina.db')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()
#
# rodz = Rodzic(name='rodzice1')
# # rodz.dzieci = [Dzieci('dziecko1')]
# # rodz.dzieci = [Dzieci('dziecko1')]
# dziec1 = Dzieci(name='dziecko1', rodz1 = rodz)
# dziec2 = Dzieci(name='dziecko2', rodz1 = rodz)
#
# # session.add_all([rodz, dziec1, dziec2])
# session.add(rodz)
# session.add(dziec1)
# session.add(dziec2)
# session.commit()


# from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
# from sqlalchemy.orm import relationship, sessionmaker, declarative_base
#
# Base = declarative_base()
#
# porownanie = Table('tytul', Base.metadata,
#                    Column('student_nr', Integer, ForeignKey('studenci.id'), primary_key=True),
#                    Column('kurs_nr', Integer, ForeignKey('kursy.id'), primary_key=True))
#
#
# class Student(Base):
#     __tablename__ = 'studenci'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     kursy = relationship('Kurs', secondary=porownanie, back_populates='studenci')
#
#
# class Kurs(Base):
#     __tablename__ = 'kursy'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     studenci = relationship('Student', secondary=porownanie, back_populates='kursy')
#
#
# engine = create_engine('sqlite:///kursy.db')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()
#
# student1 = Student(name='student1')
# student2 = Student(name='student2')
# kurs1 = Kurs(name='kursA')
# kurs2 = Kurs(name='kursB')
# student1.kursy.append(kurs2)
# student2.kursy.append(kurs2)
# student2.kursy.append(kurs1)
#
# session.add(student1)
# session.add(student2)
# session.commit()

# from decimal import Decimal
#
# l1 = Decimal('0.02')
# l2 = Decimal('1.07')
# precyzja = Decimal('0.1')
# print((l1+l2).quantize(precyzja))

####test
