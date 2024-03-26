fname    = input("Enter you full name: ")
address   = input("Enter your address: ")
interest = input("Enter your interest: ")
age      =    int(input("Enter your age: "))

"Make"
"To Do: Task 1: Use the code above to ask for user input and then save it to a file called userDetails.txt"

with open('cohort-7-week-9-and-10/Pt7_FilesDictsCodeBase2024V2/data.txt',"a") as data:
    data.write(f"{fname} {address} {interest} {age}")
 



"Further reading"
# https://www.w3schools.com/python/python_file_handling.asp