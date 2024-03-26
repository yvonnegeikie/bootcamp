"Objectives"
"" '' # Import connect module
from connect import * 
"" '' # Create a function to run sql statements to generate different type of reports


"" '' # Notes
"" '' # The SQL statement may be parametrized (i. e. placeholders instead of SQL literals). 
"" '' # A parameter specifies the value a particular field must contain when carrying out a query. 	



# Create a function to run sql statements to generate different type of reports
def search_report():
    try:
        dbCursor = db_access()[1] # tuple[Connection, Cursor]
       
 
        # ask for the search field
        search_field = input("Search by SongID or Title or Artist or Genre: ")
 
        # check if search_field value entered is SongID
        if search_field == "SongID":
            # search by SongID
            song_id = int(input(f"Enter the value for {search_field}: "))
            dbCursor.execute("SELECT * FROM songs WHERE SongID = ?", (song_id,))
            row = dbCursor.fetchone()
 
            if row is None:
                print(f"No record with SongID {song_id} exists in the songs table!!")
            else:
                # print(row)
                print("*" * 100)
                # format the heading using field names: SongID, Title, Artist, Genre
                print(f"SongID{'':<3}|Title{'':<25}|Artist{'':<24}|Genre{'':<10}")
                print("*" * 100)
                print(f"{row[0]:<9}|{row[1]:<30}|{row[2]:<30}|{row[3]:<15}")
                print("-" * 100)
 
        elif search_field.title() in ["Title" , "Artist" , "Genre"]:
            # search by Title or Artist or Genre
            str_input = input(f"Enter the value for {search_field}: ")
            #   str_input = pop : '%pop%' (pop)
            # SELECT * FROM songs WHERE Title or Artist or Genre LIKE dance/MJ/pop "
            # SELECT * FROM songs ORDER BY Title DESC
            # SELECT * FROM songs WHERE Genre = 'Pop' or Genre = 'Rock' 
            # SELECT * FROM WHERE Genre NOT LIKE 'Pop' or Genre NOT LIKE 'Rock'
            dbCursor.execute(f'SELECT * FROM songs WHERE {search_field} LIKE ?', (f'%{str_input}%',))
           
            rows = dbCursor.fetchall()
            if not rows:
                print(f"No record with the field {search_field} matching {str_input} in the songs table!!")
            else:
                # display all matched records from the songs table
                for records in rows:
                    print(records)
        else:
            print(f"Search field {search_field} value is invalid !!")
            # print(type(f'%{str_input}%,'))
 
    except sql.ProgrammingError as e:
        print(f"Search error: {e}")
if __name__ == "__main__":
    search_report()