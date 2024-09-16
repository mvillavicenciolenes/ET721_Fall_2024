"""
Michael Villavicencio
Sep 16, Python Functions
"""

import math
import random

# Example 1: Define a function to print a message. This function doesn't return nor pass a value
def hellofunction():
    print("Hello to Functions!")

# Example 2: Function that passes a username as an argument
def greeting(username):
    print(f"Good Afternoon {username}")

# Example 3: Function with a default parameter, but it doesn't return any value
def usercountry(countryname="Pakistan"):
    print(f"User is from {countryname}")

# Example 4: Function that passes and returns a value
def triplenumber(num):
    return 3 * (num)

# Example 5: Function that passes two numbers and checks if they are divisible by each other. The function returns true or false depending on conditions.
def isdivisible(n1, n2):
    if n1 % n2 == 0 or n2 % n1 == 0:
        return True
    else:
        return False

#example 8:
def rolldice():
    return random.randint(1,6)

# Call a function that doesn't return nor pass a value
print("\n ----------- Example 1 ------------ ")
hellofunction()
hellofunction()

print("\n ----------- Example 2 ------------ ")
username = "Peter Pan"
greeting(username)

print("\n ----------- Example 3: Function with default parameters ------------ ")
usercountry("China")
usercountry()

print("\n ----------- Example 4: Function that passes a number and returns the triple of that number ------------ ")
n = 5
print(f"The triple of {n} is {triplenumber(n)}")

print("\n ----------- Example 5: Functions that pass two numbers and check if they are divisible by each other ------------ ")
n1 = 45
n2 = 15
check1 = isdivisible(n1, n2)
print(f"Is {n1} and {n2} divisible?: {check1}")

print("\n ----------- Example 6: Function that passes a radius and returns the circumference ------------ ")
r = 5
c = circumference(r)
print(f"The circumference of a circle with radius {r} is {c:.2f}")

print("\n ----------- Example 7: Generate random numbers ------------ ")
print(f"Random float between 0 and 1: {random.random()}")
print(f"Random float between -5 and 5: {random.uniform(-5,5)}")
print(f"Random integer between -10 and 10: {random.randint(-10,10)}")

print("\n ----------- Example 8: Roll a dice ------------ ")
print(f"Dice number is {rolldice()}")

