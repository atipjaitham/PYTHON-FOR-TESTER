class Employee:

    def __init__(self, fname, lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email
    
    def greet_person(self):
        print("Hello, Welcome to Python "+self.fname)

emp1 = Employee('Atip', 'Jaitham', "atipjaitham@gmail.com")
emp2 = Employee('Aitian', 'Jin', 'jinaitian@gmail.com')
print(emp1.fname)
print(emp2.fname)

emp1.greet_person()
emp2.greet_person()