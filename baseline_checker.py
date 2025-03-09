import xlwings as xw
import openpyxl as xl



class Output:
    def __init__(self,avanterra):
        self.avantera = avanterra


    def new_book:
        wb = xw.Book()
        sheet = wb.sheet[0]

    def col_avanterra(self):
        wb_av = xl.load_workbook(self.avantera)
        sheet_av = wb_av.active
        head_av = {cell.value: cell.column for cell in sheet_av[1]} #pobranie naglowkow
        columns_name = ['Isin','A']
        data_av = []
        for row in sheet_av.iter_rows(min_row=2, values_only=True):
            data_av.append({name: row[head_av[name]-1] for name in columns_name}) #pobranei slownika z danych po nazwie kolumn

class Sources:
    def __init__(self, avanterra, curr_monit):
        self.avanterra = C:\Users\Paulina\PycharmProjects\Exercises\baseline\input
        self.curr_monit = C:\Users\Paulina\PycharmProjects\Exercises\baseline\input
