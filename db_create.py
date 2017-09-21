import sqlite3
#from xlrd import open_workbook
from openpyxl import *

from sqlite3 import Error

def create_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn

    except Error as e:
        print(e)

def execute_sql(conn,sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)

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

        execute_sql(conn,create_table_gltbmc)
        execute_sql(conn,create_table_gltbs)
        execute_sql(conn,create_table_gltbc)

        print("data_gltbmc...")
        data_gltbmc = load_workbook("xl/GlobalLandTemperaturesByMajorCity.xlsx")
        data_gltbmc_ws = data_gltbmc.active
        print("done.")

        print("data_gltbs...")
        data_gltbs = load_workbook("xl/GlobalLandTemperaturesByState.xlsx")
        data_gltbs_ws = data_gltbs.active
        print("done.")

        print("data_gltbc...")
        data_gltbc = load_workbook("xl/GlobalLandTemperaturesByCountry.xlsx")
        data_gltbc_ws = data_gltbc.active
        print("done.")

        for i in data_gltbmc_ws:
            sql = """INSERT INTO CITY (_DATE,AVGTEMP,UNCERT,CITY,COUNTRY,LATITUDE,LONGITUDE) VALUES ("{vDATE}","{vAVGTEMP}","{vUNCERT}","{vCITY}","{vCOUNTRY}","{vLATITUDE}","{vLONGITUDE}");"""
            sql = sql.format(vDATE=i[0].value,vAVGTEMP=i[1].value,vUNCERT=i[2].value,vCITY=i[3].value,vCOUNTRY=i[4].value,vLATITUDE=i[5].value,vLONGITUDE=i[6].value)
            #print(sql)
            execute_sql(conn,sql)
            pass

        for i in data_gltbs_ws:
            sql = """INSERT INTO STATE(_DATE,AVGTEMP,UNCERT,STATE,COUNTRY) VALUES ("{vDATE}","{vAVGTEMP}","{vUNCERT}","{vSTATE}","{vCOUNTRY}");"""
            sql = sql.format(vDATE=i[0].value,vAVGTEMP=i[1].value,vUNCERT=i[2].value,vSTATE=i[3].value,vCOUNTRY=i[4].value)
            #print(sql)
            execute_sql(conn, sql)
            pass

        for i in data_gltbc_ws:
            sql = """INSERT INTO COUNTRY(_DATE,AVGTEMP,UNCERT,COUNTRY) VALUES ("{vDATE}","{vAVGTEMP}","{vUNCERT}","{vCOUNTRY}");"""
            sql = sql.format(vDATE=i[0].value,vAVGTEMP=i[1].value,vUNCERT=i[2].value,vCOUNTRY=i[3].value)
            #print(sql)
            execute_sql(conn, sql)
            pass

        conn.commit()
        conn.close()