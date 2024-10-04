"""
Michael Villavicencio
Sep 30, Unit Testing Input Data
"""
def main():
    # Loop to collect the number of students
    while True:
        try:
            num_student = int(input("Enter the number of students: "))
            if num_student > 0:
                break
            else:
                print("Invalid Input.")
        except ValueError:
                print("Invalid Input. Try again.")
    
    # Nested loop to collect the grades for each students
    totalSumGrade = 0
    for i in range(num_student):
         while True:
                try:
                     grade = float(input(f"Enter the grade for student: "))
                     if 0 <= grade <= 100:
                          totalSumGrade += grade
                          break
                     else:
                          print("Invalid Input. Grade must be between 0 and 100.")
                except ValueError:
                    print("Invalid Input. Try again.")

    average = totalSumGrade / num_student
    print(f"The class average is {average:.2f}")

if __name__ == "__main__":
    main()  


    #Villavicencio_Lab9_Unit_Testting/testingstudentgrade.py
    #/Users/zaranoia/Desktop/School/ET721_Fall_2024/Villavicencio_Lab9/Villavicencio_Lab9_Unit_Testting/testingstudentgrade.py