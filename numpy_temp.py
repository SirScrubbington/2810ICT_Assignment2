import sqlite3
from sqlite3 import Error
from xlrd import open_workbook
from db_create import *
from sql_temp import *
import xlwt
from openpyxl import load_workbook

if __name__ == '__main__':
    wb = load_workbook("World Temperature.xlsx")
    sh = wb.create_sheet("Comparison");
    conn=create_db("data.db")
    sql="SELECT  strftime('%Y',_DATE), AVG(AVGTEMP) FROM STATE WHERE COUNTRY ='Australia' GROUP BY strftime('%Y',_DATE)"

    r = select_from_database(conn,sql)

    sh['A1'] = 'Year'
    sh['B1'] = 'Average Temperature in Australian States'

    x = []
    y = []

    for i in range(0, len(r)):
        sh['A' + str(i + 2)] = r[i][0]
        sh['B' + str(i + 2)] = r[i][1]

        x.append(r[i][0])
        y.append(r[i][1])

    wb.save("World Temperature.xlsx")