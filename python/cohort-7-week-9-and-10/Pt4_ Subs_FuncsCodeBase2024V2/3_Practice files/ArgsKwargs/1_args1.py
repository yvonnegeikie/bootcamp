"Objectives"
"" '' # Understand the purpose of using arguments instead of parameters
"" '' # Use arguments insteead of parameter

"" '' #  What is *arg (Arbitrary Positional Arguments) in function definition?
"" '' # It allows for a number of arguments to pass in the subroutine/function call instead of a number of parameters
"" '' # Think of argss as a tuple

"" '' # How to use arguments in a function definition
"" '' # *arg = arguments: declare between the braces of the subroutine/function definition.
"" '' # syntax
"" '' # def functionName(*nameOfArg):
"" '' #     pass


"" '' #  A function with a number of paramters
"" '' # This function can only take three values when called/invoked
def userName(paraFullName, paraAddress, paraInterest):
    pass


"" '' # The same function above now modify to use arguments.
"" '' # This function can now take in an unlimited number of values when called/invoked
def userName(*userdata):
    pass


"" '' # using arguments (*args) instead of parameter(s), will return a tuple when the subroutine/function is called/invoked

"" '' # define a subrouitine called userName
def userName(*args):  # userDetails
    for userData in args:
        print(userData)

"" '' # call the userName function with the number of arguments as required
userName("Abdul")
userName("Abdul", "Coding")
userName("AA", "BB", "CC")



"" '' # define a subrouitine called userDetails
def userDetails(*userDetails): 
    "" '' # use a for loop to loop through the values that will be passed in the function call
    for userinfo in userDetails:
        print(userinfo)


"" '' # call the userName function with the number of arguments as required
userDetails("Abdul", "Address", "Coding", 12, 13.5, True)

