"Objectives"
"" '' # Understand the purpose of using arguments instead of parameters
"" '' # Use arguments instead of parameter

"" '' # using arguments (*args) instead of parameter(s), will return a tuple when the subroutine/function is called/invoked

"" '' # define a subrouitine called userDetails
def userDetails(*userDetails): 
    "" '' # use a for loop to loop through the values that will be passed in the function call
    for userinfo in userDetails:
        print(userinfo)


"" '' # How to convert the subroutine above into a function?

print("\nSolution 1")
"" '' #  Solution 1 
def userDetails1(*userDetails):  #
    return userDetails
  
"" '' # call the userName function with the number of arguments as required
print(userDetails1("Em", "Jay", "Python", "JS"))
data = userDetails1("Em", "Jay", "Python")


"" '' # Access the and print the value Python
print(data[2])


print("\nSolution 2")
"" '' #  Solution 2
def userDetails2(*userDetails):  #
    allData = []  # create an empty list
    # loop through data provided as arguments in the sub/func call
    for userinfo in userDetails:
        # add each data to the list
        allData.append(userinfo)
        # return items from the list
    return allData


"" '' # call the userName function with the number of arguments as required
print(userDetails2("Em", "Jay", "Python"))
data = userDetails2("Em", "Jay", "Python")
print(data[2])

print("UserDetails2\n")
data1 = userDetails2("Abdul", "Address", "Coding", 12, 13.5, True)
print(f"UserDetails2\n{data1}")
