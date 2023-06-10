# Database Operations
# CRUD Acronynm
# Create: Create and Insert values into the database
# Read: Read the database
# Update: Update the database
# Delete: Delete Values from the database

import sqlite3 as sql
from time import sleep

# connect() function

conn = sql.connect(r"C:\Users\edank\OneDrive\Documents\Software Testing\HTML GLA\Python Project\Project Dbops.py\blkhistmovies.db")

cursor = conn.cursor()



