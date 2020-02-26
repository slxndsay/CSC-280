# Lab 5
# Problem 2 and 3
# Name: Sophia Lindsay

from lab5p1 import Student

# Problem 2: Subclass (Phd Students)
class Phd(Student):
	def __init__(self, name, year, gpa, current_classes, 
				advisor, numberOfResearchPapers):
		
		super().__init__(name, year, gpa, current_classes)
		self.advisor                = advisor
		self.numberOfResearchPapers = numberOfResearchPapers

	# Modifying the method for Phd students
	def addYear(self):
		if(self.year < 6):
			self.year += 1

	def setGPA(self, newGPA):
		self.gpa = newGPA

	# Using update in method
	def addClass(self, newClass):
		self.current_classes.update(newClass)


# Problem 3: Subclass (Student Athletes)
class StudentAthlete(Student):
	def __init__(self, name, year, gpa, current_classes, 
				sport, yearsOfExperience, onScholarship, starter):
		super().__init__(name, year, gpa, current_classes)
		self.sport             = sport
		self.yearsOfExperience = yearsOfExperience
		self.onScholarship     = onScholarship
		self.starter           = starter

def main():
	student_1 = Phd(name = "John Doe", 
						year = 1, 
						gpa = 3.3, 
						current_classes = {"Econ-301":3, "Calculus":4, "Physics":4}, 
						advisor = "Prof. Doe", 
						numberOfResearchPapers = 3)
	
	student_2 = StudentAthlete(name  = "Jane Doe", 
								year = 2, 
								gpa = 3.5, 
								current_classes = {"Biology":4, "Organic Chemistry": 4}, 
								sport = "Basketball", 
								yearsOfExperience = 3, 
								onScholarship = True, 
								starter = True)

	# Informational Statement, Initial
	print("The Phd student,", student_1.name, "is in Year", student_1.year, "and has a", student_1.gpa, "and is taking", student_1.current_classes)
	print("The Student Athlete,", student_2.name, "is in Year", student_2.year, "and has a", student_2.gpa, "and is taking", student_2.current_classes)

	# Updating methods with data
	student_1.addYear()
	student_1.setGPA(4.0)
	student_1.addClass({"Microbiology": 4})

	student_2.addYear()
	student_2.setGPA(3.4)
	student_2.addClass({"Music": 3})

	# Printing informational statement, final
	print(student_1.name,"is now in year", student_1.year, ", has a GPA of", student_1.gpa,"and is taking", student_1.current_classes)
	print(student_1.name,"is now in year", student_1.year, ", has a GPA of", student_1.gpa,"and is taking", student_1.current_classes)


if __name__ == "__main__":
	main()