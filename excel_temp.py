import sqlite3
from sqlite3 import Error
from xlrd import open_workbook
from db_create import *
from sql_temp import *
import xlwt
import numpy as np
import matplotlib.pyplot as plt
from openpyxl import *

if __name__ == '__main__':
    wb = Workbook()
    wb_name = 'World Temperature.xlsx'
    sh = wb.create_sheet("Temperature By City")
    conn = create_db("data.db")
    query = "SELECT  CITY, strftime('%Y',_DATE), AVG(AVGTEMP) FROM CITY WHERE COUNTRY ='China' GROUP BY strftime('%Y',_DATE),CITY"
    r = select_from_database(conn,query)

    print(r)

    x = []
    y = []
    z = []

    #sh.write(0,0,"Year")
    #sh.write(0,1,"Average Temperature in China")

    sh['B1']='Year'
    sh['C1']='Average Temperature in China'
    sh['A1']='City'

    for i in range(0,len(r)):
        #sh.write(i+1,0,str(r[i][0]))
        #sh.write(i+1,1,str(r[i][1]))

        sh['A'+str(i+2)]=str(r[i][0])
        sh['B'+str(i+2)]=r[i][1]
        sh['C'+str(i+2)]=r[i][2]

        x.append(r[i][0])
        y.append(r[i][1])
        z.append(r[i][2])

        pass

    #plt.plot(x,y)
    #plt.xlabel('Year')
    #plt.ylabel('Average Temperature in China')
    #plt.show()

    wb.save(wb_name)
