"Objectives"
"" '' # Understand that a Subroutine(function) may have a return statement
"" '' # Use a subroutine(function) with a return statement in your program
"" '' # Use parameter(s) in function definition
"" '' # Use argument(s) in function call
"" '' # Inner function
"" '' # Outer and Inner function 


""" declare a function using the def keyword """
"" '' # declare function and pass parameters/arguments as place holder
def userGreetings(name):

    "" '' # declare second/inner function with or without parameters/arguments as place holder
    def userMsg():
        "" '' # the return msg
        return "Hello how are you " 
    
    "" '' # the function userMsg plus the parameter of userGreetings function is assigned to the result variable 
    result = userMsg() + name 

    "" '' # returns the values in the result variable
    return result 
print(userGreetings('Pete'))