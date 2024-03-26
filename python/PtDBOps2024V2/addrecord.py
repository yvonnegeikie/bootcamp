"Objectives"
"" '' # Import connect module
"" '' # Create a function to add record(s) to a table in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement


"" '' # Notes
"" '' # The SQL statement may be parametrized (i. e. placeholders instead of SQL literals). 
"" '' # A parameter specifies the value a particular field must contain when carrying out a query. 	

from connect import *
 
# create a functin to add/inser recod in the songs table
def insert_record():
    try:
        dbCon, dbCursor = db_access()
        #SongID, Title, Artist, Genre
        #SongID is an auto incrment field , no data is required.
 
        # create a variable for each field
        song_title = input("Enter song title: ")
        song_artist = input("Enter song artist: ")
        song_genre = input("Enter song genre: ")
 
        # create a sql statement to insert data from the respective variables song_title, song_artist, song_genre
        dbCursor.execute("INSERT INTO songs VALUES(NULL,?,?,?)",(song_title,song_artist,song_genre))
        # Or
        # dbCursor.execute("INSERT INTO songs (Title,Artist,Genre) VALUES(?,?,?)",(song_title,song_artist,song_genre))
        dbCon.commit() # permanently write the record/data to the table in the database
        print(f"{song_title} inserted in the songs table")
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
   
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
   
    except sql.Error as er:
        print(f"This error: {er}")
if __name__ == "__main__":
    insert_record()
 