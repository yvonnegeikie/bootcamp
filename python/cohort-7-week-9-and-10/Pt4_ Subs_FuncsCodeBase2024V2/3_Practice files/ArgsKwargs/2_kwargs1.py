"Objectives"
"" '' # Understand the purpose of using kwargs instead of arguments or parameters
"" '' # Use arguments insteead of parameter

"" '' #  What is **kwargs (Arbitrary keyword arguments) in function definition?
"" '' # It allows for a number of keyword arguments to pass in the subroutine/function call instead of arguments or parameters
"" '' # Think of kwargss as a dictionary

"" '' # How to use arguments in a function definition
"" '' # **kwarg = arguments: declare between the braces of the subroutine/function definition.
"" '' # syntax
"" '' # def functionName(**nameOfKwarg):
"" '' #     pass

"" '' #  A function with a number of paramters
"" '' # This function can only take three values when called/invoked
def userName(paraFullName, paraAddress, paraInterest):
    pass

"" '' # The same function above now modify to use keyword arguments.
"" '' # This function can now take in an unlimited number of values when called/invoked
def userName(**userdata):
    pass


"" '' # using arguments (**kwargs) instead of parameter(s), will return a dictionary when the subroutine/function is called/invoked
def addition(**kwargs): 
    
    "" '' # for loop is used to unpack the dictionary data structure(key value pairs)
    for varNums, numsValue in kwargs.items():
        print(varNums, numsValue)

"" '' # call the addition function with the number of arguments as required
addition(num1=10, num2=20, num3=30)


