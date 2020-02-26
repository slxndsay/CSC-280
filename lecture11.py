# Lecture 11
class Employee():
	def __init__(self, name, yearsOfExperience, pastEmployers):
		self.name              = name
		self.yearsOfExperience = yearsOfExperience
		self.pastEmployers     = pastEmployers

# Getters
	def getName(self):
		return(self.name)

	def getYearsOfExperience(self):
		return(self.yearsOfExperience)

	def getPastEmployers(self):
		return(self.pastEmployers)

# Setters
	def setName(self, newName):
		self.name              = newName

	def setYearsOfExperience(self, newYearsOfExperience):
		self.yearsOfExperience = newYearsOfExperience

	def setPastEmployers(self, newPastEmployers):
		self.pastEmployers     = newPastEmployers

# Method

	def needsPromotion(self):
		if self.yearsOfExperience > 5:
			return(True)

		return(False)


def main():
	# Object 1
	employee_1 = Employee(name = "Sophia Lindsay", 
						  yearsOfExperience = 2, 
						  pastEmployers = [])

	employee_2 = Employee(name = "Jane Doe", 
						  yearsOfExperience = 6, 
						  pastEmployers = ["IBM", "Google"])

	# Informative Messages with yearsOfExperience setters and getters
	print("Years were:", employee_1.getYearsOfExperience())
	employee_1.setYearsOfExperience(newYearsOfExperience = 3)
	print("Years are:", employee_1.getYearsOfExperience())

	# Does Employee_1 Need a promotion?
	print(employee_1.needsPromotion())

	

if __name__ == "__main__":
	main()