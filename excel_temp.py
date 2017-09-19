from sql_temp import *
import matplotlib.pyplot as plt
from openpyxl import *
from openpyxl.chart import (LineChart,Reference,)

if __name__ == '__main__':
    wb = Workbook()
    wb_name = 'World Temperature.xlsx'
    sh = wb.active
    sh.title="Temperature By City"
    conn = create_db("data.db")
    query = "SELECT  CITY, strftime('%Y',_DATE), AVG(AVGTEMP) FROM CITY WHERE COUNTRY ='China' AND AVGTEMP NOT NULL GROUP BY strftime('%Y',_DATE),CITY ORDER BY strftime('%Y',_DATE) DESC"
    r = select_from_database(conn,query)

    print(r)

    x = []
    y = []
    z = []

    d = {}

    sh['B1']='Year'
    sh['C1']='Average Temperature in China'
    sh['A1']='City'

    for i in range(0,len(r)):
        if int(r[i][1]) > 0:
            sh['A'+str(i+2)]=str(r[i][0])
            sh['B'+str(i+2)]=r[i][1]
            sh['C'+str(i+2)]=r[i][2]

            if r[i][0] not in d.keys():
                d[r[i][0]]=[[],[]]

            if(r[i][2]!=0):
                d[r[i][0]][0].append(r[i][1])
                d[r[i][0]][1].append(r[i][2])
        pass


    for k,v in d.items():
        plt.plot(v[0],v[1],label=k)
    plt.title("Average Temperature in Major Chinese Cities")
    plt.plot(y,z)
    plt.xlabel('Year')
    plt.ylabel('Average Temperature (Celsius)')
    plt.legend()
    plt.show()

    c = LineChart()
    c.title = "Average Temperature in Major Chinese Cities"
    c.style = 13
    c.y_axis.title = "Average Temperature (Celsius)"
    c.x_axis.title = "Year"

    data = Reference(sh,min_col=1,min_row=1,max_col=3,max_row=1200)
    c.add_data(data,titles_from_data=True)

    sh.add_chart(c,"E1")

    wb.save(wb_name)
