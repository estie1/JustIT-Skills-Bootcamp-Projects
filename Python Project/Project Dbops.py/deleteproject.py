# Asks the User for the movie ID to delete
from connectproject import *
from readproject import read

def delete():
	readdata = read()
	if readdata == 0:
		print("There is no data to delete.")
	else:
		movieID = input("Enter a movieID to delete: ")

		# Deleting a movieID
		sqlCode = f"""
		DELETE FROM blkhistmovies
		WHERE movieID = "{movieID}";

		"""

		cursor.execute(sqlCode)
		conn.commit()

		print(f"Movie {movieID} has been successfully deleted.")
		sleep(2)

		read()

if __name__ == "__main__":
	delete()