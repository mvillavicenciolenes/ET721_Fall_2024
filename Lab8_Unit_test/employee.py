"""
Example 3: Verify if the email, full name, and salary fields are correct
Michael Villavicencio
"""

class Employee:
    raise_amt = 1.5

    def __init__(self, firstname, lastname, salary):
        self.first = firstname
        self.last = lastname
        self.salary = salary

    # The @property decorator indicates that the method will behave like an attribute
    @property
    def emailemployee(self):
        return f"{self.first}.{self.last}@company.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)