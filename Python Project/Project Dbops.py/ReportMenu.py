from readproject import read
from insertproject import *
from updateproject import *
from deleteproject import *

def menu():
	menuUI = """Welcome to BlackHistoryMovies Database v1.03

	Please Select an option below:
	
	1. Print details of all movies 
    2. Print all movie classifications
	3. Print all movies of a particular year 
    4. Print movie ID of your choice
    5. Exit Application

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
			readclassification()
		elif userChoice == "3":
			readrelease()
		elif userChoice == "4":
			movieID = input("Enter your choice of movieID ")
			readmovieID(movieID)	
		elif userChoice == "5":
			menuLoop = False

print("End Program")
		