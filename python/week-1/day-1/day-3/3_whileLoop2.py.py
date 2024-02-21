"""use a while loop when the number of iteration is unknown(dont know how many times you want/going 
to do something for)
A while loop also controls the flow of execution in a program"""


#ToDo: Predict, then Run, and then Investigate"

num = 1  # int(input("Enter a number: "))
userNum = 12
# while 1 <= 20

while num <= 20:  # start from 1 and keep looping to 20(condition is met)
    print(f"The number is {num}")
    if num == userNum:  # check if the value in userNum is the same as the value in num
        print(f"Exited loop")
        break  # break/exit the loop
    num += 1  

"Modify/Make"
#ToDo: Task1: modify the userNum variable to use a randomly generated number between 1 - 20"
"Further reading on python while statements"

import random # use the random module, this is needed to generate randome number 
userNum = random.randint(1, 20)# generate random number between 1-20 
print (f"Random number is: {userNum}") 

num = 1

while num <= 20: #compares userNum and num inside loop 
    print(f"The number is {num}")
    if num == userNum:  
        print(f"Exited loop")
        break  
    else: 
        print("Exited loop") 
   
    
#Random number is: 2
#The number is 1
#The number is 2
#Exited loop 
    
#Random number is: 10
#The number is 1
#The number is 2
#The number is 3
#The number is 4
#The number is 5
#The number is 6
#The number is 7
#The number is 8
#The number is 9
#The number is 10
#Exited loop


# https://www.w3schools.com/python/ref_keyword_while.asp
# https://www.w3schools.com/python/python_ref_keywords.asp
# https://www.w3schools.com/python/python_reference.asp


