class RateOfInterest:
    interest = 0.06 #class variable
    def __init__(self, name, loan):
        self.name = name
        self.loan = loan

    def calc_interest(self):
        print("Welcome! ",self.name,self.lname)
        print("Total Interest 1 : ",self.loan * self.interest)
        print("Total Interest 2 : ",self.loan * RateOfInterest.interest)

class Student(RateOfInterest):
    def __init__(self, name, lname, loan):
        super().__init__(name, loan)
        self.lname = lname

s = Student("Atip","Jaitham", 500000)
# interest = 0.04
s.calc_interest()
# p1 = RateOfInterest("Atip", 500000)
# p1.interest = 0.08
# p1.calc_interest()

# p2 = RateOfInterest("Aitian", 400000)
# p2.interest = 0.04
# p2.calc_interest()