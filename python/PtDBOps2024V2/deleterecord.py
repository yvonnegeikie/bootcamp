"Objectives"
"" '' # Import connect module
from connect import * 

"" '' # Create a function to delete record(s) in a table in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement

"" '' # Notes
"" '' # The SQL statement may be parametrized (i. e. placeholders instead of SQL literals). 
"" '' # A parameter specifies the value a particular field must contain when carrying out a query. 	

# Create a function to delete record(s) in a table in a database
def delete_record():
    try:
        dbCon, dbCursor = db_access()

        # check if SongID exists before deleting
        song_id = int(input("Enter the SongID to delete a record: "))
        dbCursor.execute("SELECT * FROM songs WHERE SongID = ?", (song_id,)) #tuple 

        # invoke the fetchone method and assign it to the variable called row
        row = dbCursor.fetchone() # fetch a single row or unique record 

        if row == None:  # None is a singleton object that checks if a value exists or is present 
            print(f"No record with SongID {song_id} in songs table!")
        else: # if there is a match with SongID provided
            dbCursor.execute("DELETE FROM songs WHERE SongID = ?", (song_id,))
            dbCon.commit()
            print(f"Record {song_id} deleted from the song table")
    except sql.ProgrammingError as e:
        print("DElete operation failed: {e}")
if __name__=="__main__":
    delete_record() 