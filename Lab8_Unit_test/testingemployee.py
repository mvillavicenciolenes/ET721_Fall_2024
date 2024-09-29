"""
Example 3: Verify if the email, full name, and salary fields are correct
Michael Villavicencio
"""

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    # Set up a template before running each test
    def setUp(self):
        # Create an instance of the class Employee
        self.emp1 = Employee("Peter", "Pan", 50000)

    def test_emailemployee(self):
        # Test the email generation
        self.assertEqual(self.emp1.emailemployee, "Peter.Pan@company.com")

    def test_fullname(self):
        # Test the full name generation
        self.assertEqual(self.emp1.fullname, "Peter Pan")  # Removed extra comma

    def test_apply_raise(self):
        # Test the salary raise application
        self.emp1.apply_raise()
        self.assertEqual(self.emp1.salary, 75000)  # Corrected expected salary after raise

if __name__ == "__main__":
    unittest.main()