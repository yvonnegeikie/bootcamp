"""use a while loop when the number of iteration is unknown(dont know how many times you want/going 
to do something for)
A while loop also controls the flow of execution in a program"""

num = 1

#ToDo: Task 1: Explain what is += 1  ?"
# The += operator is an augmented assignment operator. it combines (=) with (+) so is another way of writing:
# num = num +1
num = 1
num += 1
print(num) # output is 2 

"Modify/Make"
#ToDo: Task 2: Modify the whileloop above to count down from 20 to 1 and comment your code"
num = 20
while num > 0:
    print(num)
    num -= 1 # using -= subtract augmented operator to remove 1 as long as num is greater than 0




