from connect import *

dbCon, dbCursor = db_access()

def create_tbls():

    dbCursor.execute("""
    CREATE TABLE "tblfilms" (
        "filmID" integer,
        "title" text,
        "yearReleased" integer,
        "rating" text,
        "duration" integer,
        "genre" text
    )
    """)

    # dbCursor.execute("INSERT INTO tblfilms (title, yearReleased, rating, duration, genre) VALUES ('Sample Movie', 2022, 'PG', 120, 'Action')")

if __name__ == "__main__":
    create_tbls()