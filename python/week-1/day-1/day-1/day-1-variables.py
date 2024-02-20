""" multiline comment"""
# single time comment 

# to do
print(2*2)
print(2/2)
print(2%2)
print(4-1)

# \n = newline break 

print("Refactored code\n")
"Predict, then run, and investigate" 
#To do: what is he difference in the terminal when the code below is executed? 
print(2*3, "n", 2+3, "\n", 2/3, "n\", 21-3")

# The python onterpreter rints anything as it is, if placed between speach marks/quotations 
print("My name is Yvonne\n welcome to python!")

# To do: use print statement ot print the following:
# Your name
# Your address
# Your interests
print("Yvonne \n Leyton \n Making things look nice")
print("Yvonne")
print("Leyton")
print("Making things look nice")

# Reaseach: What is a variable in Python? 
#In Python, variables are named containers used to store and manage data during program execution. They act like boxes or labels that hold values you can work with within your code.
# like a verable in js but done need a an ID, just the name 

"Object reference 1"
var_num = "an_object" # var_num is now is now referencing hte object "an_object" 
num1 = 10 # intiger whole value 
num2 = 2.0 # float has a decimal point 
bVal1 = True # complex number 
bVal2 = False # Boolean answers MUST have UPPER CASE capitalisatin 


"Predict, then Run, and Investigate"
"What is the function the object's type when used in as shown below?"
print(type(num1))

num1 = 1 # int
num2 = 2.5 # float 
num3 = 3 # int 

"This is what happens when you create a variable in python?"
# 1. Creates and int/float/string object (variable)
# 2. Assign the object the value
# 3. use or print the object


answer1 = num1 + num2
print(answer1) # 3.5
answer2 = num3 * num2
print(answer2) # 7.5
answer3 = answer1 + answer2
print(answer3) # 11.0


"Assign multiple values(objects) to multiple variables in a single line"
#To DO: Complete the code below to assign values to the respective variables
name, address, interest = "Ennovy", "Hackney", "Making things look ugly"
print(name, address, interest)


"Chained assignment"
first_child = second_child = third_child = "Yvonne"
print(
    "I am the first child",
    first_child,
    "\nI am the second child",
    second_child,
    "\nI am the third child",
    third_child,
)

"You have now seen the how to assign multiple values(objects) to multiple variables and chained assignment."
"In your own words, can you explain the difference between the two?"
#The differences = 
# can use \n or ',' to seperate the lines
# can assign multiple objects the same value in one line of code 
# can assign different values to different objects in one line of code  


"Object references 2"
# Rather than creating a new object when num4 = num1 code is executed,
# it creates a symbolic name/reference, and num4 now point to the object with a value of 10
# same as num1
num4 = num1  # multiple references to the same object
print(id(num1))  # id returns the identify of an object
print(id(num4))

"Will the identity of the two objects referenced below be the same ?"
num1 = 10 
num4 = "10" 
print(id(num1))
print(id(num4))

num1 = "10"
print(type(num1)) # float 

num1 = 10.0
print(type(num1)) # string

# num1 = "10"
# print(type(num1))
# num1 = 10.0
# print(type(num1))

"What is the evivalent of python type in JavaScript?"
#The equivalent of 


"Knowledge Check"
#To DO: Write one thing you remember from what we covered so far?


"Read, Run and investigate the lines of code below"

# Variable naming convention
username = "user1"  # meaningful name

# use of camel notation when the variable is a combination of two words
userName = "user2"

 # use snake case/underscore when the variable is a combination of two words
user_name = "user3" 

user4 = "paul0045"  # meaningful name

userAge = 23  # meaningful name

firstname = "Anna"  # meaningful name and use of single quotes in value


"DON'T DO THIS"
AGE = 12  # Unless it is a constant!!
# £cash or $cash
User = "muser"  # dont start variable with upper case
# user name = # no spaces between two words in variable assignment
# 1user = "jam"# no number at start of variable name

# Avoid doing the following:
# £errr = "money"  don't use a symbol
# AGE = 12 variable name should not be in all upper cases
# Username = "toby345" # don't start variable names with upper case character
# 2username = "Coder112345" #dont start variable names with number
# user name = "test user" # no spaces between variable name/s



"Research:" 
"To DO: Is there a difference in using dollar or any other currency symbol to declare variable in JS vs python?"
#Yes, there is a significant difference.

# In JavaScript:
# ($) is a valid character for variable names
# it doesn't have any built-in meaning related to currency
# some developers use the dollar sign as a prefix for variables representing jQuery objects, but this is purely a coding style choice and not enforced by the language itself.

# In Python:
# ($) is not a valid character for variable names. You'll get a syntax error.
# Variable names in Python can only consist of letters, numbers, and underscores.
# Instead of using dollar signs, Python offers ways to work with currency values through libraries like 'decimal' or the 'currencies' module.


"Further reading on variables naming convention and independent learning, see link(s) below"
# https://peps.python.org/pep-0008/#function-and-variable-names
# https://namingconvention.org/python/


# Python constant
AGE = 12  # AGE is constant do not re-assign with a different object
print("\nOriginal age is", AGE)

AGE = 15
print("\nAge is now", AGE)

"Research:" 
"To DO: Investigate how python use make use of constants to answer if there is any similarity with constant use in JavaScript?"
