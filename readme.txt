Filename: readme.txt
Author: Damon Murdoch
Date: 22/09/2017
Purpose: Instructions on how to use db_create.py, sql_temp.py, excel_temp.py, and numpy_temp.py.

Instructions:
1. Insert the 3 archives to be accessed in the 'xl' folder.
2. Run db_create.py. This will take around five to ten minutes to run on most computers, and will generate the database from the worksheets.
3. Run sql_temp.py. This will make a new database table with select data from existing tables, and will print the highest, lowest and mean temperature for Queensland.
4. Run excel_temp.py. This will create a new workbook called 'World Temperature.xlsx' containing Chinese city temperature data, with a graph in the active worksheet.
5. Run numpy_temp.py. This will create a new worksheet called 'Comparison' in the workbook generated in step 4. It will insert Average yearly temperature data from Australian states
   and the national average into the worksheet, and display a graph using MatPlotLib.