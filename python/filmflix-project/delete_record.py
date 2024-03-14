def delete_record():
    try:
        dbCon, dbCursor = db_access()

        # check if filmID exists before deleting
        filmID = int(input("Enter the filmID to delete a record: "))
        dbCursor.execute("SELECT * FROM tblfilms WHERE filmID = ?", (filmID,)) 

        # invoke the fetchone method and assign it to the variable called row
        row = dbCursor.fetchone() # fetch single row 

        if row == None: 
            print(f"No record with filmID {filmID} in songs table")
        else: 
            dbCursor.execute("DELETE FROM tblfilms WHERE filmID = ?", (filmID,))
            dbCon.commit()
            print(f"Record {filmID} deleted from the film table")
    except sql.ProgrammingError as e:
        print("DELETE operation failed: {e}")
if __name__=="__main__":
    delete_record() 