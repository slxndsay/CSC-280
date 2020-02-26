# Lab 5
# Problem 1 
# Name: Sophia Lindsay

# Parent Class (Students
class Student():
	def __init__(self, name, year, gpa, current_classes):
		self.name            = name
		self.year            = year
		self.gpa             = gpa
		self.current_classes = current_classes

	# Methods
	def addYear(self):
		if(self.year < 4):
			self.year += 1

	def setGPA(self, newGPA):
		self.gpa = newGPA

	# Using update in method
	def addClass(self, newClass):
		self.current_classes.update(newClass)


def main():
	# Object 1
	student_1 = Student(name = "Sophia Lindsay", 
						year = 1, 
						gpa = 3.9, 
						current_classes = {"Econ-301":3, 
											"Calculus":4, 
											"Physics":4, 
											"AUx":1, 
											"CSC":4, 
											"Intro to Rapid Prototyping":1})
	
	# Informational statement for Year 1
	print(student_1.name, ' was Year', student_1.year, 'with a', student_1.gpa, 'GPA. ')

	# Assigning values for methods
	student_1.addYear()	
	student_1.setGPA(4.0)
	student_1.addClass({"Writing": 3})

	# Informational statement for updated attributes
	print("Next year,", student_1.name, "was Year", student_1.year, "with (hopefully) a", student_1.gpa, "GPA. They would be taking", student_1.current_classes)



if __name__ == "__main__":
	main()