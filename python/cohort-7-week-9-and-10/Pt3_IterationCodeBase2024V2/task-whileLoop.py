
# Task 1:
# Add comments to the code in the python file 3_whileloop1.py 

# Further reading on python while statements"
# https://www.w3schools.com/python/ref_keyword_while.asp



# "Task 2:
# "Explain what is the purpose of  "+=1" in the python file 3_whileLoop2.py?" 

# Task 3: 
# Modify the whileloop in the python file 3_whileLoop2.py to count down from 20 to 1, and comment your code where applicable"

# num = 20
# while num >=1:
#     print(f"The number {num}")


# Task 4: 
# Modify the userNum variable in the 3_whileLoop3.py to use a randomly generated number between 1 - 20"

import random

num = 1  # int(input("Enter a number: "))
userNum = random.randint(1, 20)
print(f"While value of {userNum}\n")
while num <= 20: # start from 1 and keep looping to 20 when condition is met 
    print (f"The number is {num}")
    if num == userNum:
        break
    num =+ 1

# Further reading on python while statements
# https://www.w3schools.com/python/ref_keyword_while.asp
# https://www.w3schools.com/python/python_ref_keywords.asp
# https://www.w3schools.com/python/python_reference.asp


# Task 5: 
# 1. Explain and comment as many lines to demonstrate understanding in the match case code block in the python file matchCase.py
# 2. Use the example in the python file matchCase.py to create your own days in the week program using match case