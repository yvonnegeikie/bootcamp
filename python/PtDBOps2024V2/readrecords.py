"Objectives"
"" '' # Import connect module
from connect import *

"" '' # Create a function to read record(s) from a table in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement

"" '' # Notes
"" '' # The SQL statement may be parametrized (i. e. placeholders instead of SQL literals). 
"" '' # A parameter specifies the value a particular field must contain when carrying out a query. 	

 # Create a function to read record(s) from a table in a database
def read_records():
    try:
        dbCon, dbCursor = db_access()
        # invoke the cursor.execute method to select all the records from the table
        dbCursor.execute("SELECT * FROM songs")
 
        # fetch all selected records using the fetchall method and assigned it to a variable
        all_records = dbCursor.fetchall() # fetchall method fetches the selected records
 
        if all_records:
            #display a line of 100 * from left to right
            print("*" * 100)
            # format the heading using field names: SongID, Title, Artist, Genre
            print(f"SongID{'':<3}|Title{'':<25}|Artist{'':<24}|Genre{'':<10}")
            print("*" * 100)
 
            for aRecord in all_records:
                # 0         1       2          3        
                #(1,       'Test', 'Tester', 'coding')
                print(f"{aRecord[0]:<9}|{aRecord[1]:<30}|{aRecord[2]:<30}|{aRecord[3]:<15}")
                print("-" * 100)
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
if __name__ == "__main__":
    read_records()
 
 

