"Objectives"
"" '' # Understand that a Subroutine(function) may have a return statement
"" '' # Use a subroutine(function) with a return statement in your program
"" '' # Use parameter(s) in function definition
"" '' # Use argument(s) in function call
"" '' # Outer and Inner function 

"" '' # an outer function without parameter
def hello():

    "" '' # define a variable outside of the inner function 
    fullname = "Johnny Test" # input("Enter your name")

    "" '' #define the inner function
    def userdata():
        print(f"Your name is: {fullname}")

    "" '' # call the inner function
    userdata()


"" '' # call the outer function 
hello()
