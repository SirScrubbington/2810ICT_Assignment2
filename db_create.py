import sqlite3
from xlrd import open_workbook

from sqlite3 import Error

def create_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn

    except Error as e:
        print(e)

def create_table(conn,sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

def insert_row(conn,table,data):
     try:
         c = conn.cursor()

         sql = "INSERT INTO "+table+" VALUES ("

         for i in range(0,len(data)):
             if(i > 0):
                sql += ","
             if(isinstance(data[i],str)):
                 temp = data[i].replace("'","’")
                 sql +="'"+temp+"'"
             else:
                 sql +=str(data[i])
         sql+=");"
         print(sql)
         c.execute(sql)
         conn.commit()
     except Error as e:
         print(sql)
         print(e)

def read_data(worksheet,table):
    for s in worksheet.sheets():
        for row in range(s.nrows):
            col_value = []
            for col in range(s.ncols):
                value = (s.cell(row, col).value)
                col_value.append(value)
            insert_row(conn,table, col_value)


if __name__ == '__main__':

    # Global Land Temperatures by City
    create_table_gltbmc = "CREATE TABLE CITY(" \
                          "_DATE DATE NOT NULL," \
                          "AVGTEMP DOUBLE NOT NULL," \
                          "UNCERT DOUBLE NOT NULL," \
                          "CITY VARCHAR(16) NOT NULL," \
                          "COUNTRY VARCHAR(16)," \
                          "LATITUDE VARCHAR(8) NOT NULL," \
                          "LONGITUDE VARCHAR(8) NOT NULL," \
                          "PRIMARY KEY(_DATE,CITY));"

    # Global Land Temperatures By State
    create_table_gltbs = "CREATE TABLE STATE(" \
                         "_DATE DATE NOT NULL," \
                         "AVGTEMP DOUBLE NOT NULL," \
                         "UNCERT DOUBLE NOT NULL," \
                         "STATE VARCHAR(16) NOT NULL," \
                         "COUNTRY VARCHAR(16)," \
                         "PRIMARY KEY(_DATE,STATE));"

    # Global Land Temperatures by Country
    create_table_gltbc = "CREATE TABLE COUNTRY(" \
                          "_DATE DATE NOT NULL," \
                          "AVGTEMP DOUBLE NOT NULL," \
                          "UNCERT DOUBLE NOT NULL," \
                          "COUNTRY VARCHAR(16) NOT NULL," \
                          "PRIMARY KEY(_DATE,COUNTRY));"

    conn = create_db("data.db")

    if conn is not None:

        create_table(conn,create_table_gltbmc)
        create_table(conn,create_table_gltbs)
        create_table(conn,create_table_gltbc)

        print("data_gltbmc...")
        data_gltbmc = open_workbook("xl/GlobalLandTemperaturesByMajorCity.xlsx")
        print("done.")
        print("data_gltbs...")
        data_gltbs = open_workbook("xl/GlobalLandTemperaturesByState.xlsx")
        print("done.")
        print("data_gltbc...")
        data_gltbc = open_workbook("xl/GlobalLandTemperaturesByCountry.xlsx")
        print("done.")

        read_data(data_gltbmc,"CITY")
        read_data(data_gltbs, "STATE")
        read_data(data_gltbc, "COUNTRY")
        #conn.commit()