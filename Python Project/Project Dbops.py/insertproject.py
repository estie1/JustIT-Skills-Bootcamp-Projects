from connectproject import *
from readproject import *

# User input to add movies
def insert():
    movieID = input("Enter movie ID")
    Title = input("Enter movie title: ")
    MainActor = input("Enter main actor: ")
    Release = input("Enter movie release date: ")
    Summary = input("Enter movie summary: ")
    Classification = input("Enter movie classification: ")

    sqlCode = f"""
    INSERT INTO blkhistmovies VALUES ("{movieID}", "{Title}", "{MainActor}", "{Release}", "{Summary}", "{Classification}")

    """

    cursor.execute(sqlCode)
    conn.commit()

    print(f"{Title} was successfully added to the database.") 
    read()

# sqlCode = """
# INSERT INTO blkhistmovies VALUES 
# (NULL, "Cry Freedom", "Denzel Washington", 1987, "South African journalist Donald Woods, flees the country after writing a book on his friend, Biko who dies in police custody.", "PG"),
# (2, "And The Children Shall Lead", "Danny Glover", 1985, "Young friends who attempt to ease, racial tensions, whilst living in the deep south, Mississippi in the 60s", "U"),
# (3, "Hidden Figures", "Taraji P. Henson, Octavia Spencer, Janelle Monae", 2017, "Three female african-american mathematicians, face racial  and gender discrimination as they play a vital role at NASA airspace", "PG"),
# (4, "Loving", "Ruth Negga, Joel Edgerton", 2016, "Richard and Mildred Loving, find themselves arrested and thrown out of their home in Virginia. This begins a legal battle that would end in the supreme court", "PG13"),
# (5, "Pride", "Terrence Howard, Bernie Mac", 2007, "An african-american swim team, is faced with overtly racist opposition. Jim and Elston mentor the kids to success", "15"),
# (6, "When They See Us", "Asante Blackk, Caleel Harris, Jovan Adepo, Chris Chalk", 2019, "TV mini-series, based on the events of the Central Park jogger case in 1989, exploring the lives of the families and male suspects who were african-american and latino", "18+")
# """

