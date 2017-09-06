import sqlite3
from sqlite3 import Error
from xlrd import open_workbook

from db_create import *

def select_from_database(conn,query):
    cur = conn.cursor()
    cur.execute(query)
    rows=cur.fetchall()

    result = []

    for row in rows:
        result.append(row)

    return result


if __name__ == '__main__':

    conn = create_db("data.db")

    data_south_hem = select_from_database(conn,"SELECT * FROM CITY WHERE LATITUDE LIKE '%n' ")

    create_table_south_hem = "CREATE TABLE 'Southern cities'(" \
                          "_DATE DATE NOT NULL," \
                          "AVGTEMP DOUBLE NOT NULL," \
                          "UNCERT DOUBLE NOT NULL," \
                          "CITY VARCHAR(16) NOT NULL," \
                          "COUNTRY VARCHAR(16)," \
                          "LATITUDE VARCHAR(8) NOT NULL," \
                          "LONGITUDE VARCHAR(8) NOT NULL," \
                          "PRIMARY KEY(_DATE,CITY));"

    create_table(conn, create_table_south_hem)

    for s in data_south_hem:
        print(s)
        insert_row(conn,"'Southern cities'",s)

    data_min_max_avg = select_from_database(conn,"SELECT MAX(AVGTEMP), MIN(AVGTEMP),AVG(AVGTEMP) FROM STATE WHERE STATE = 'Queensland' AND AVGTEMP NOT NULL ")

    print(data_min_max_avg)