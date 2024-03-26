"Objectives"
"" '' # Understand that a Subroutine(function) may have a return statement
"" '' # Use a subroutine(function) with a return statement in your program
"" '' # Use parameter(s) in function definition
"" '' # Use argument(s) in function call

def sub():  # define the subtraction function
    # variables inside a  surbroutine/function have local scope
    num1 = int(input(("Enter your first number: ")))
    num2 = int(input(("Enter your second number: ")))
    answer = num1 - num2
    print(f"he answer to {num1} - {num2} is {answer}")   



"If this file is run directly it will automatically call and run the respective subroutines"
if __name__ == "__main__":