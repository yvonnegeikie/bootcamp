
from connect import *
 
def insert_record():
    try:
        dbCon, dbCursor = db_access()
        
        # create a variable for each field
        filmID = input("Enter filmID: ")
        title = input("Enter film title: ")
        yearReleased = input("Enter year released: ")
        rating = input("Enter film rating: ")
        duration = input("Enter film duration: ")
        genre = input("Enter film genre: ")
 
        # create a sql statement to insert data from the respective variables song_title, song_artist, song_genre
        dbCursor.execute("INSERT INTO filmID VALUES(NULL,?,?,?,?,?)",(title,yearReleased,rating,duration,genre))
    
        dbCon.commit() # permanently write the record/data to the table in the database
        print(f"{filmID} inserted in the tblfilms table")
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
   
    except sql.ProgrammingError as pe:
        print(f"Not working because: {pe}")
   
    except sql.Error as er:
        print(f"This error: {er}")
if __name__ == "__main__":
    insert_record()
 