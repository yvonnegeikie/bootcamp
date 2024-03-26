"Objectives"
"" '' # Import connect module
"" '' # Create and use a function that create tables in a database
"" '' # Use try and except to handle error(s)
"" '' # Use the execute method from the cursor object to run sql statement

from connect import *


# assign the function with two variables to represent each items in the tuple 
dbCon, dbCursor = db_access()

def create_tbls():

    dbCursor.execute(
    """ 
    CREATE TABLE "members" (
        "MemberID"  INTEGER NOT NULL UNIQUE,
        "Firstname" TEXT,
        "Lastname"  TEXT,
        "Email" TEXT,
        PRIMARY KEY("MemberID" AUTOINCREMENT)
    )"""
    )
    # ...............................
    dbCursor.execute(
        """
    CREATE TABLE "songs" (
        "SongID"    INTEGER NOT NULL UNIQUE,
        "Title" TEXT,
        "Artist"    TEXT,
        "Genre" TEXT,
        PRIMARY KEY("SongID" AUTOINCREMENT)
    )"""
    )
    # ...........................
    dbCursor.execute(
        """
      CREATE TABLE "downloads" (
        "DownlID"   INTEGER NOT NULL UNIQUE,
        "SongID"    INTEGER,
        "MemberID"  INTEGER,
        "Date"  TEXT,
        PRIMARY KEY("DownlID" AUTOINCREMENT),
        FOREIGN KEY("SongID") REFERENCES "songs"("SongID"),
        FOREIGN KEY("MemberID") REFERENCES "members"("MemberID")
    )
    """
    )
    
if __name__ == "__main__":
    create_tbls()