"Objectives"
"" '' # Understand what is a Subroutine
"" '' # Understand the need for subroutine
"" '' # Explain the difference between custom/user define subroutine(function) and built in subroutine(function)
"" '' # Use a subroutine in your program

"" '' # Notes
"" '' # In python function is a type of subroutine, a subroutine is sequence of instructions to perform a specific task with an identifiable name.

"" '' #  Need for subroutine(function)
"" '' # As your programs become larger and more complex, they need to be broken down into smaller, self-contained sections

"" '' # How to create a subroutine(function)
"" '' # A subroutine(function) definition is used to define the steps within the subroutine(function)

"" '' # Custom built function: is A function that you have created yourself to use in the same program or imported into other programs that you have created created.
"" '' # In built function: is A function that comes with python like int, print, input etc that you can use in your program(s).

"" '' # A subroutine(function) may or may not have a return statement"
"" '' # A subroutine(function) may or may not have parameters"
"" '' # def just defines the subroutine(function)"
"" '' # A subroutine(function) is not executed unless the subroutine is called."
"" '' # A subroutine(function) call tells the program to branch to the function, execute it and come back to the next statement in the main program"


"" '' # syntax
"" '' # def subroutine/functionName():
"" '' #     subroutine/functionBody
"" '' #     subroutine/functionBody
"" '' #     subroutine/functionBody
"" '' #     subroutine/functionBody

"" '' #  To call/invoke the subroutine/function
"" '' #  subroutineName/functionName()


"" '' # To Do: Predict, then Run, and then Investigate"
#name is a global variable 
name = "Emjay"
 
# def define the subroutine/function called 
def user_name(): 
    # this name is a local variable 
    name = input("Enter your name: ") #"James Bond
    print(f"Your name is {name}")

print(name) 
# name is a now a local variable 


# call/invoke the subroutine
user_name()

