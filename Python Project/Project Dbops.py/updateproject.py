from connectproject import *
from readproject import *

def update():
    movieID = input("Enter the ID of the movie you would like to change: ")
    Title = input("Enter the movie title: ")
    MainActor = input("Enter main actor: ")
    Release = input("Enter movie release date: ")
    Summary = input("Enter movie summary: ")

    sqlCode = f"""
    UPDATE blkhistmovies 
    SET Title = "{Title}", "Main Actor" = "{MainActor}", Release = "{Release}", Summary = "{Summary}"
    WHERE movieID5 = {movieID}
    """

    cursor.execute(sqlCode)
    conn.commit()

    print(f"The movie has been successfully updated.")