"Objectives"
"" '' # Understand Variable Scope
"" '' # Understand what is global scope variable
"" '' # Understand what is a local scope variable
"" '' # Use global scope variable and Local scope variable 


"" '' # What is a variable Scope
"" '' # The scope of a variable is the section of the program where the variable can be accessed and modified.


"" '' # What is a global scope and local scope?
"" '' # Variables can either have global scope or local scope. 

"" '' #  What is a Global scope variabe?
"" '' #  Global scope refers to a variable that can be accessed and modified from anywhere in the program, even from inside subroutines. 
"" '' #  A variable declared in the main part of the program can be accessed globally by all subroutines. 
"" '' #  It cannot be modified unless you explicitly state that the program should modify the global variable. 

"" '' # What is a Local scope variable 
"" '' # Local scope refers to variables that can only be accessed and modified within the code block that they were declared.  


"" '' # Handling Variable Scope
"" '' # Not all programming languages handle scope in the same way Python has been designed to discourage the modification 
"" '' # of global variables, research to find out why and see link below after the exemplar code block of accessing global variables inside a function.
"" '' # Variables are local unless otherwise declared. 


"" '' # To Do: 
"" '' # Task 1: Predict, then Run, and then Investigate the code from line 34 - 46, comment out other lines of code

# This variable has a global scope by default
globalNum = 5

# The subroutine localSubRoutine() is accessing the globalNum variable and displaying it as output. 
def localSubRoutine():
    # Access the globalNum variable declared outside of this subroutine
    print(f"Printed globalNum variable {globalNum}from outside of local subroutine\n")

    localNum = 10  # local variable that is declared inside localSubroutine (local by dfault)
    print(f"Printed localNum variable {localNum} from local subroutine\n")


localSubRoutine()  # call subroutine
print(f"Printed globalNum variable {globalNum} from global\n")


"" '' # To Do: Task 2:
"" '' # Uncomment the line of code with the print function below and then run the file only after you run and understand the code block above

"" '' # The code below will attempt to access locaNum from loacalsubroutine
# print(f"attempt to access locaNum from loacalsubroutine {localNum} \n")

"" '' # Can you explain the output from the terminal when you run the print statement above, you have just uncommented

