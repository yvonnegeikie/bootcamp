"Objectives"
"" '' # Import sqlite module
import sqlite3 as sql # imported the sqlite3 module and assigned it an alias 'sql' 

"" '' # Understand what is sqlite
"" '' # Create and use a function to create a database file
"" '' # Use try and except to handle error(s)
"" '' # Use the connect function from the sqlite module to create a database file
"" '' # Create a cursor variable from the connect function  

"" '' # Notes:
"" '' #  What is Sqlite
"" '' #  SQLite is a lightweight disk-based database that does not require a separate server process making it easy to integrate into applications
"" '' #  and it uses a variant of the SQL language for database queries to access database. This combination of features makes SQLite a popular 
"" '' #  choice for applications that need a simple and self-contained database solution

def db_access():
    try: # try the code  within the try block
        # context(with) manager access resources and automatically closes unused resources
        # invoke the sqlite connect method to create a db file if it foes not exist
        # in the specified folder and assigned it an alias 'dbCon'
        with sql.connect("PtDBOps2024V2/dfe7w4.db") as dbCon:
           
            #create a variable called dbCursor and initialise with cursor method from the connect function
            dbCursor = dbCon.cursor() # cursor function is used to call the execute method
 
            return dbCon, dbCursor
    except sql.OperationalError as e: # raise sqlerror
        #use the error raised to handle the exception/error
        print(f"Connection failed: {e}")

if __name__== "__main__":
    db_access()

   
         



