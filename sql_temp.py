# Filename: sql_temp.py
# Author: Damon Murdoch
# Date: 22/09/2017
# Purpose: Generate a new database table in 'data.db' with data from existing tables and print the highest, lowest and mean temperature for Queensland.

import sqlite3
from sqlite3 import Error
from db_create import *

# select_from_database(conn,query): List[]
# Runs a given query 'query' on a connection 'conn'
# and returns an array containing the data.
def select_from_database(conn,query):

    # Create cursor and query
    cur = conn.cursor()
    cur.execute(query)

    # Fetch all the data and add it to a list
    rows=cur.fetchall()
    result = []
    for row in rows:
        result.append(row)
    return result

if __name__ == '__main__':

    conn = create_db("data.db")

    # Create new table 'Southern cities'
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
    execute_sql(conn, create_table_south_hem)

    # Insert data into new table
    for s in data_south_hem:
        sql = """ INSERT INTO 'Southern cities'(_DATE,AVGTEMP,UNCERT,CITY,COUNTRY,LATITUDE,LONGITUDE) VALUES("{vDATE}","{vAVGTEMP}","{vUNCERT}","{vCITY}","{vCOUNTRY}","{vLATITUDE}","{vLONGITUDE}")"""
        sql = sql.format(vDATE=s[0],vAVGTEMP=s[1],vUNCERT=s[2],vCITY=s[3],vCOUNTRY=s[4],vLATITUDE=s[5],vLONGITUDE=s[6]);

    # Select all Queensland data
    data_min_max_avg = select_from_database(conn,"SELECT AVGTEMP FROM STATE WHERE STATE = 'Queensland' AND AVGTEMP IS NOT NULL")

    max=0
    min=100
    avg=0
    count=0

    # Find the minimum, maximum and average values.
    for i in data_min_max_avg:
        if(i[0])=='' or i[0]=='None':
            continue

        if (i[0]) > max:
            max = float(i[0])

        if (i[0]) < min:
            min = float(i[0])

        avg += (i[0])
        count += 1

    avg = avg / count

    print("Maximum: ",max,"Minimum: ",min,"Average: ",avg)