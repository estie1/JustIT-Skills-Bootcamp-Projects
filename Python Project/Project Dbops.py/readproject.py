from connectproject import *

def read():
    sqlCode = "SELECT * FROM blkhistmovies"

    cursor.execute(sqlCode)
    # Fetchall will retrieve all data from recent query
    data = cursor.fetchall()

    print("\nblkhistmovies List:")
    for i in data:
        print(i)


def readclassification():
    sqlCode = "SELECT Classification FROM blkhistmovies"
    cursor.execute(sqlCode)
    # Fetchall will retrieve all data from recent query
    data = cursor.fetchall()

    print("\nblkhistmovies List:")
    for i in data:
        print(i)

def readrelease():
    sqlCode = "SELECT Release FROM blkhistmovies"
    cursor.execute(sqlCode)
    # Fetchall will retrieve all data from recent query
    data = cursor.fetchall()

    print("\nblkhistmovies List:")
    for i in data:
        print(i)

def readmovieID(ID):
    sqlCode = f"""
    SELECT * FROM blkhistmovies 
    WHERE MovieID = {ID} 
    """
    cursor.execute(sqlCode)
    # Fetchall will retrieve all data from recent query
    data = cursor.fetchall()

    print("\nblkhistmovies List:")
    for i in data:
        print(i)


