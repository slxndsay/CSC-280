# Import the Parent Class
from lecture11 import Employee

# Make a subclass for CEO
class CEO(Employee):
	def __init__(self, name, yearsOfExperience, pastEmployers, 
				onForbes, worksforFortune500):
	
		super().__init__(name, yearsOfExperience, pastEmployers)
		self.onForbes           = onForbes
		self.worksforFortune500 = worksforFortune500

	# needsPromotion will always return(False) because he's CEO
	def needsPromotion(self):
		return(False)

	def namedBezos(self):
		return(True)

def main():
	CEO_1 = CEO(name = "Jeff Bezos", 
				yearsOfExperience  = 20,
				pastEmployers      = ["Amazon"], 
				onForbes           = True,
				worksforFortune500 = True)

	print(CEO_1.needsPromotion())

	print(CEO_1.namedBezos())


if __name__ == "__main__":
	main()