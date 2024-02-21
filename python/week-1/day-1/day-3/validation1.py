
#ToDo: Task 1: In the terminal Enter numeric values for the first and second number to perform addition and take note of the output
#Enter your first number: 1
#Enter your second number: 2
#The answer to 1 + 2 = 3
#Executing...some code and processes

#ToDo: Task 2: In the terminal Enter a numeric value  for the first number and string value(ten/one/two) for the second number to perform addition and take note of the output"
#Enter your first number: 1
#Enter your second number: Post
#Please Enter Numeric Values
#Executing...some code and processes


try:
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    answer = num1 + num2
    print(f"The answer to {num1} + {num2} = {answer}")

except ValueError:
    print("Please Enter Numeric Values")


print("Executing...some code and processes")

#ToDo: Task 3: Explain why did the program break, when you followed the instructions in task 2 but not in task 1
# input() function only returns string value

# below code creates while loop to continue until valid integers are entered 
while True:
  try:
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    break  # Exit the loop if valid integers are entered
  except ValueError:
    print("Invalid input. Please enter integers only.")

answer = num1 + num2
print(f"The answer to {num1} + {num2} = {answer}")

print("Executing...some code and processes")



# https://www.w3schools.com/python/python_ref_exceptions.asp
# https://docs.python.org/3/library/exceptions.html?highlight=exception#Exception


