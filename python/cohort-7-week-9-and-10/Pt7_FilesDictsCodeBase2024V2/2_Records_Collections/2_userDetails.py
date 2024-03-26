# fname    = input("Enter you full name: ")
# address   = input("Enter your address: ")
# interest = input("Enter your interest: ")
# age      =    int(input("Enter your age: "))


# create a dictionary 
dict1 = {"Fullname": "Jane Smith", "Age": 23, "Hobby":"Coding", 1:"Gamer"}

# create a dictionary with keys but no values 
print("dictionary with keys but no values")
userDetails1 = {"fname": "", "address": "", "interest": "", "age": "","country": "","city": ""}
print(userDetails1)

# Use key to add values to dictionary 
userDetails1["fname"] = input("Enter you full name: ")
print(userDetails1)

# use a loop to add values to a dictionary
for aKey in userDetails1: # aKey = fname, address, interests, age
    userDetails1[aKey] = input(f"Enter your {aKey}:") # for loop will enter all aKeys as listed above 

"Extension"
"Modify"
"To Do: Task 1: write the input statement to add the remaining values to the userDetails1 dictionary above"

# create a dictionary with no keys and no values 
print("dictionary with no keys and no values")

"Make"
"To Do: Task 2: Create a dictionary with no keys as shown below, then write the input statement to add the keys and values."
userDetails2 = {}
print(userDetails2)

addKeyVal = True 

while addKeyVal: 
    key = input("Enter key: ")
    value = input(f"Enter value for: {key}")
    userDetails2[key] = value
    
    # ask to continue or not 
    newKeyVal = input("Add another key value pairs(Y/N): ").upper()
    # compare/check 
    if newKeyVal == "N":
        # re-assign the addKeyVal a False boolean variable to exit the loop 
        addKeyVal = False
        print("All required key value pairs added to dictionary")
print(userDetails2)