from connect import * 

# Create a function to run sql statements to generate different types of reports
def search_report():
    try:
        dbCursor = db_access()[1] 
    
        search_field = input("Search by filmID or title or yearReleased or rating or duration or genre: ")
 
        # check if search_field value entered is filmID
        if search_field == "filmID":
            # search by filmID
            filmID = int(input(f"Enter the value for {search_field}: "))
            dbCursor.execute("SELECT * FROM tblFilms WHERE filmID = ?", (filmID,))
            row = dbCursor.fetchone()
 
            if row is None:
                print(f"No record with filmID {filmID} exists in the films table!!")
            else:
                print("*" * 100)
                # format the heading using field names below 
                print(f"filmID{'':<3}|title{'':<25}|yearReleased{'':<24}|rating{'':<10}|duration{'':<10}|genre{'':<10}")
                print("*" * 100)
                print(f"{row[0]:<9}|{row[1]:<30}|{row[2]:<30}|{row[3]:<15}")
                print("-" * 100)
 
        elif search_field.title() in ["filmID", "title", "yearReleased", "rating", "duration", "genre"]:
            # search by Title or Artist or Genre
            str_input = input(f"Enter the value for {search_field}: ")
          
            dbCursor.execute(f'SELECT * FROM tblFilms WHERE {search_field} LIKE ?', (f'%{str_input}%',))
           
            rows = dbCursor.fetchall()
            if not rows:
                print(f"No record with the field {search_field} matching {str_input} in the film table!!")
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