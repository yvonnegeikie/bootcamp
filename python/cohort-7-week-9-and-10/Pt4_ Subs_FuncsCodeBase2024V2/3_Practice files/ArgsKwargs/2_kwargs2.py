"Objectives"
"" '' # Understand the purpose of using kwargs instead of arguments or parameters
"" '' # Use keyword arguments instead of parameter

"" '' #  What is **kwargs (Arbitrary keyword arguments) in function definition?
"" '' # It allows for a number of keyword arguments to pass in the subroutine/function call instead of arguments or parameters
"" '' # Think of kwargss as a dictionary

"" '' # How to use arguments in a function definition
"" '' # **kwarg = arguments: declare between the braces of the subroutine/function definition.
"" '' # syntax
"" '' # def functionName(**nameOfKwarg):
"" '' #     pass

"" '' # using arguments (**kwargs) instead of parameter(s), will return a dictionary when the subroutine/function is called/invoked

def addition(**kwargs):  #
    "" '' # for loop is used to loop through the keys in dictionary data structure
    for varNums in kwargs.keys():
        print(f"The keys {varNums}")

"" '' # call the addition function with the number of arguments as required
addition(num1=10, num2=20, num3=30, name="anna")


def addition(**kwargs):  #     
    "" '' # for loop is used to loop through the values in dictionary data structure
    for numsValue in kwargs.values():
        print(f"Value {numsValue}")


"" '' # call the addition function with the number of arguments as required
addition(num1=10, num2=20, num3=30, city="London")