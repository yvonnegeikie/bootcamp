"Objectives"
"" '' # Understand that a Subroutine(function) may have a return statement
"" '' # Use a subroutine(function) with a return statement in your program
"" '' # Use parameter(s) in function definition
"" '' # Use argument(s) in function call


def userName():  # define a subrouitine called userName
    fullName = input("Enter your name: ")
    address = input("Enter your address: ")
    interest = input("Any interest? ")
    print(f"my name is {fullName}, my address is {address} and my interest is {interest}")



"If this file is run directly it will automatically call and run the respective subroutines"
if __name__ == "__main__":