import unittest
from bankaccount import BankAccount

class BankAccountTests(unittest.TestCase):

    # Set up the initial balance
    def setUp(self):
        self.account = BankAccount("Bruce Wayne", 1000000000000.0) 

    # Check the account's balance
    def test_starting_balance(self):
        self.assertEqual(self.account.get_balance(), 1000000000000.0)

    # Check that deposits work correctly
    def test_add_funds(self):
        self.account.deposit(500.0)  # Adding 500 to balance
        self.assertEqual(self.account.get_balance(), 1000000000500.0)

    # Checking withdraws
    def test_remove_funds(self):
        self.account.withdraw(400.0)  # Removing 400
        self.assertEqual(self.account.get_balance(), 999999999600.0)

    # Check that withdrawing more than available balance raises an error
    def test_overdraft_prevention(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(1200000000000.0)  

    # Confirm the balance after two types of activities
    def test_sequence_of_transactions(self):
        self.account.deposit(200.0)
        self.account.withdraw(150.0)
        self.assertEqual(self.account.get_balance(), 1000000000060.0)

    # Ensure that depositing a negative amount throws an error
    def test_negative_deposit(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100.0)

    # Ensure that trying to withdraw a negative amount throws an error
    def test_negative_withdrawal(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-50.0)

if __name__ == "__main__":
    unittest.main()