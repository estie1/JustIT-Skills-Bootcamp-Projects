from readproject import read
from insertproject import *
from updateproject import *
from deleteproject import *

def menu():
	menuUI = """Welcome to BlackHistoryMovies Database v1.03

	Please Select an option below:
	
	1. Add a New Movie to the database
	2. Delete a movie in the database
	3. Update an Existing Movie
	4. Print all movies
	5. Reports
	6. Exit Application
	"""
	print(menuUI)
	sleep(1)
	
	options = ["1", "2", "3", "4", "5"]
	choice = input("Select an Option From the menu: ")

	while choice not in options:
		print(f"{choice} is not valid.")
		choice = input("Please Enter a valid option: ")
	
	return choice


if __name__ == "__main__":
	menuLoop = True

	while menuLoop == True:
		userChoice = menu()
		if userChoice == "1":
			read()
		elif userChoice == "2":
			delete()
		elif userChoice == "3":
			update()
		elif userChoice == "4":
			print()
		elif userChoice == "5":
			menuLoop = False

print("End Program")
		