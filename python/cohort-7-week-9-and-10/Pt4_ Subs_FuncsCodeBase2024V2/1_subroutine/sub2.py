"Objectives"
"" '' # Understand what is a Subroutine
"" '' # Understand the need for subroutine
"" '' # Explain the difference between custom/user define subroutine(function) and built in subroutine(function)
"" '' # Use a subroutine in your program

"To Do: Predict, then Run, and then Investigate"
def addition():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    answer = num1 + num2
    print(f"The answer to {num1} + {num2} = {answer}")


"" '' # prevents the automatic running of the subroutine when it is imported in to another python file/application
"If this file is run directly it will automatically call and run the respective subroutines"
if __name__ == "__main__":
    addition()


