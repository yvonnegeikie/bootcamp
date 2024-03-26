"Objectives"
"" '' # Understand the purpose of using kwargs, arguments and parameters
"" '' # Use kwargs, arguments and parameters

"" '' # define a subroutine thats uses kwargs, arguments and parameters
def userInfo(paratest, *nums, **userDetails):  # userDetails
    print(f"The parameter is: {paratest}\n")
    print(f"The args are: {nums}\n")
    print(f"The kwargs are: {userDetails}")


"" '' # call the addition function with the number of arguments as required
userInfo("This is a test",1,2,3,4,5, 6, 7, firstPerson="Anna", secondPerson="Peter")