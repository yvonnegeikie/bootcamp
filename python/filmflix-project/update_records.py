from connect import *

# Create a function to update record(s) in a table in a database
def update_record():
    try:
        dbCon, dbCursor = db_access()

        filmID = int(input("Enter the filmID to update a record: "))
        dbCursor.execute("SELECT * FROM tblFilms WHERE filmID = ?", (filmID,))

        row = dbCursor.fetchone()

        if row == None:
            print(f"No record with the filmID {filmID} exists ")
        else:
            field_name = input("Enter the field (filmID or title or yearReleased or rating or duration or genre) ").lower()
            if field_name not in ["filmid", "title", "yearreleased", "rating", "duration", "genre"]:
                print(f"Field {field_name} is not a field name in the table")

            else:
                field_value = input(f"Enter the value for the field {field_name}: ")
                
                dbCursor.execute(f"UPDATE tblFilms SET {field_name} = ? WHERE filmID = ? ", (field_value,filmID,))
                dbCon.commit()
                print(f"Record {filmID} updated")            
    except sql.ProgrammingError as e:
        print(f"Update error: {e}")

if __name__ == "__main__":
    update_record()



