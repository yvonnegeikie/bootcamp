"Objectives"
"" '' # Import connect module
from connect import *
"" '' # Create a function to update record(s) in a table in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement

# Create a function to update record(s) in a table in a database
def update_record():
    try:
        dbCon, dbCursor = db_access()

        # check if SongID exist before update
        song_id = int(input("Enter the SongID to update a record: "))
        dbCursor.execute("SELECT * FROM songs WHERE SongID = ?", (song_id,))

        row = dbCursor.fetchone()
        if row == None:
                print(f"No record with the SongID {song_id} exists ")
                
        else:
            num_fields = input("Enter N to update one field or Y to update all fields: ").upper()

            if num_fields == "Y":

                song_title = input("Enter value to update song title: ")
                song_artist = input("Enter value to update song artist: ")
                song_genre = input("Enter value to update song genre: ")

                # perform the update 
                #UPDATE songs SET Title or Artist or Genre = TitleValue or ArtistValue or GenreValue WHERE SongID = 1/2/3/4/5....
                dbCursor.execute(f"UPDATE songs SET Title = ?, Artist = ?, Genre = ? WHERE SongID = ? ", (song_title,song_artist,song_genre,song_id,))
                dbCon.commit()
                print(f"Record {song_id} updated")

            elif num_fields == "N":
                 #asf for the field to be updated
                field_name = input("Enter the field (Title or Artist or Genre) ").title()
                if field_name not in ["Title", "Artist",  "Genre"]:
                    print(f"Field {field_name} not a field name in the table")

                else:
                    # ask for the value of the fiel to be updated 
                    field_value = input(f"Enter the value for the field {field_name}: ")
                    # perform the update 
                    #UPDATE songs SET Title or Artist or Genre = TitleValue or ArtistValue or GenreValue WHERE SongID = 1/2/3/4/5....
                    dbCursor.execute(f"UPDATE songs SET {field_name} = ? WHERE SongID = ? ", (field_value,song_id,))
                    dbCon.commit()
                    print(f"Record {song_id} updated")   

            else:
                print(f"Invalid entry, ")


    except sql.ProgrammingError as e:
        print(f"Update error: {e}")

if __name__ == "__main__":
    update_record() 



