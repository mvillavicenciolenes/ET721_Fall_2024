import datetime
import random
import uuid

class Customer:
    def __init__(self, name, age, address, email):
        self.customer_id = str(uuid.uuid4())
        self.name = name
        self.age = age
        self.address = address
        self.email = email
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_id] = account

    def remove_account(self, account_id):
        if account_id in self.accounts:
            del self.accounts[account_id]
        else:
            print(f"Account {account_id} not found for customer {self.name}.")

    def __str__(self):
        return f"Customer {self.name}, Age: {self.age}, Email: {self.email}"

class Account:
    def __init__(self, account_type):
        self.account_id = str(uuid.uuid4())
        self.account_type = account_type
        self.investments = []
        self.balance = 0.0
        self.transaction_history = []

    def add_investment(self, investment):
        self.investments.append(investment)
        self.balance -= investment.amount
        self.transaction_history.append({
            'date': datetime.datetime.now(),
            'type': 'investment',
            'details': str(investment),
            'amount': -investment.amount
        })

    def add_funds(self, amount):
        self.balance += amount
        self.transaction_history.append({
            'date': datetime.datetime.now(),
            'type': 'deposit',
            'details': 'Funds added to account',
            'amount': amount
        })

    def remove_funds(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.transaction_history.append({
                'date': datetime.datetime.now(),
                'type': 'withdrawal',
                'details': 'Funds withdrawn from account',
                'amount': -amount
            })

    def get_investment_summary(self):
        summary = "Investment Summary:\n"
        for investment in self.investments:
            summary += f"{investment}\n"
        return summary

    def __str__(self):
        return f"Account {self.account_id}, Type: {self.account_type}, Balance: ${self.balance:.2f}"

class Investment:
    def __init__(self, investment_type, amount, duration_years, risk_level):
        self.investment_id = str(uuid.uuid4())
        self.investment_type = investment_type
        self.amount = amount
        self.start_date = datetime.datetime.now()
        self.duration_years = duration_years
        self.risk_level = risk_level
        self.roi = self.calculate_roi()

    def calculate_roi(self):
        # Simulating ROI calculation based on risk level and random factors
        risk_multiplier = {'low': 0.03, 'medium': 0.06, 'high': 0.12}
        market_fluctuation = random.uniform(-0.05, 0.1)
        base_roi = risk_multiplier[self.risk_level]
        return base_roi + market_fluctuation

    def current_value(self):
        # Calculate current value based on ROI and time elapsed
        elapsed_years = (datetime.datetime.now() - self.start_date).days / 365.25
        return self.amount * (1 + self.roi) ** elapsed_years

    def __str__(self):
        return (f"Investment {self.investment_id}: {self.investment_type}, "
                f"Amount: ${self.amount:.2f}, Duration: {self.duration_years} years, "
                f"Risk: {self.risk_level}, ROI: {self.roi:.2%}")

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = {}

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer

    def remove_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
        else:
            print(f"Customer {customer_id} not found in bank records.")

    def get_customer_report(self, customer_id):
        if customer_id not in self.customers:
            return f"Customer {customer_id} not found."
        
        customer = self.customers[customer_id]
        report = f"Customer Report for {customer.name}:\n"
        report += f"Customer ID: {customer.customer_id}\n"
        report += f"Accounts:\n"
        for account_id, account in customer.accounts.items():
            report += f"  {account}\n"
            report += f"  {account.get_investment_summary()}\n"
        return report

    def __str__(self):
        return f"Bank {self.name} with {len(self.customers)} customers."

# Example usage
if __name__ == "__main__":
    # Create Bank
    bank = Bank("Global Finance Bank")

    # Create Customers
    customer1 = Customer("Alice Johnson", 35, "123 Elm Street, Springfield", "alice.j@gmail.com")
    customer2 = Customer("Bob Smith", 42, "456 Oak Avenue, Metropolis", "bob.smith@outlook.com")

    # Add Customers to Bank
    bank.add_customer(customer1)
    bank.add_customer(customer2)

    # Create Accounts for Customers
    savings_account1 = Account("Savings")
    investment_account1 = Account("Investment")
    
    # Add Accounts to Customers
    customer1.add_account(savings_account1)
    customer1.add_account(investment_account1)

    # Add Funds to Accounts
    savings_account1.add_funds(10000)
    investment_account1.add_funds(5000)

    # Create Investments
    investment1 = Investment("Stocks", 2000, 5, "medium")
    investment2 = Investment("Bonds", 3000, 10, "low")

    # Add Investments to Investment Account
    investment_account1.add_investment(investment1)
    investment_account1.add_investment(investment2)

    # Print Customer Reports
    print(bank.get_customer_report(customer1.customer_id))
    print(bank.get_customer_report(customer2.customer_id))
