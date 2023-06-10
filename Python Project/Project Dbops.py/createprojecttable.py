from connectproject import *

sqlCode = """
CREATE TABLE blkhistmovies (
    "movieID" INTEGER NOT NULL UNIQUE,
    "Title" text,
    "Main Actor" text,
    "Release" INT,
    "Summary" text,
    "Classification" varchar,
    PRIMARY KEY ("movieID" AUTOINCREMENT)
);
"""
cursor.execute(sqlCode) 



 