"""
Michael Villavicencio
Lab 3, Python review

"""

print("---------------- Example 1: Control Flow -----------------")
labs = int(input("Enter Lab's Grade: "))
exams = int(input("Enter Exam's Grade: "))

if 0 <= labs <= 100 and 0 <= exams <= 100:  
    finalGrade = (labs + exams) / 2
    gpa = ''
    
    if 100 >= finalGrade >= 90:
        gpa = 'A'
    elif 90 > finalGrade >= 80:
        gpa = 'B'
    elif 80 > finalGrade >= 70:
        gpa = 'C'
    elif 70 > finalGrade >= 60:
        gpa = 'D'
    elif 60 > finalGrade >= 0:
        gpa = 'F'
    else:
        gpa = "UNDEFINED!!!"
else:
    # Handle invalid grades
    if not (0 <= labs <= 100):
        print(f"Grade for lab {labs} is invalid")
    if not (0 <= exams <= 100):
        print(f"Grade for exam {exams} is invalid")
    gpa = 'UNDEFINED'

print(f"Your final grade for the class is {gpa}")

print("----------------- Example 2: Loops --------------------")
secret = 8
userGuess = int(input("Guess a number between  1 and 10: "))
while not(secret == userGuess):
    userGuess = int(input("Wrong guess. Guess again: "))

print(f"Congrats! {userGuess} is the right number!!!")

print("----------------- Example 3: Loops, Break statement --------------------")
balance = 1000
withdraw = 0
deposit = 0

while True:
    userinput = input("Do you want to withdraw, press w, or deposit ,press d? ")
    if userinput ==  'w' or userinput ==  'W':
        w_amount = int(input('How much do you wat to withdraw? '))
        if w_amount > balance:
            print("Insufficient funds!!! \n Can't withdraw more than {balance} ")
        else:
            balance -= w_amount

    elif userinput == 'd' or userinput == 'D':
            d_amount = int(input('How much do yu want to deposit? '))
            balance += d_amount
            print(f"Your new balance is {balance}")
    else:
            print("Invalid Selection")

    choice = input("Would you like to make another transaction? (y,n)")
    if not(choice == 'y' or choice == 'y'):
        break

print("Thank you for banking with us!")

print("----------------- Example 4: For Loops as a counter --------------------")

for n in range(-5,3,2):
    print(f"counting = {n}")

print("----------------- Example 5: for loop in a list --------------------")

colors = ['magenta', 'babyblue', 'olive']

for c in colors:
    print(f"color = {c}")

print("-----------------------------------------------------------------------")
