"Objectives"
"" '' # Understand that a Subroutine(function) may have a return statement
"" '' # Use a subroutine(function) with a return statement in your program
"" '' # Use parameter(s) in function definition
"" '' # Use argument(s) in function call
"" '' # Outer and Inner function 


"" '' # an outer function with parameter
def hello(fullname):

    "" '' # define the inner function
    def userdata():
        print(f"Your name is: {fullname}")
    
    "" '' # call the inner function
    userdata()


"" '' # call the outer function 
hello('James Bond')


