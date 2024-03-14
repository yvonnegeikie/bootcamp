
from connect import *

 # Create a function to read record(s) from table tblfilms in database filmflix.db
def read_records():
    try:
        dbCon, dbCursor = db_access()
        dbCursor.execute("SELECT * FROM tblfilms")
 
        all_records = dbCursor.fetchall() # fetchall rows and records 
 
        if all_records:
            print("*" * 100) #display a line of 100 * from left to right
            print(f"filmID{'':<3}|title{'':<20}|yearReleased{'':<3}|rating{'':<5}|duration{'':<3}|genre{'':<3}")
            print("*" * 100)
 
            for aRecord in all_records:
                # 0         1       2          3        
                #(1,       'Test', 'Tester', 'coding')
                print(f"{aRecord[0]:<9}|{aRecord[1]:<25}|{aRecord[2]:<15}|{aRecord[3]:<11}|{aRecord[4]:<11}|{aRecord[5]:<10}")
                print("-" * 100)
    except sql.OperationalError as e:
        print(f"Failed because: {e}")
if __name__ == "__main__":
    read_records()
 
 

