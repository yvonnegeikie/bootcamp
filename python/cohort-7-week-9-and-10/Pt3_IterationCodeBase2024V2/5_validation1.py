"Objectives"
"" '' # Understand what is Errors and Exceptions 
"" '' # Use a while Loop to repeatedly executes a block of code as long as a specified condition remains true# Read though the code below:


"" '' # Notes
"" '' # Python Exception is represented in class hierarchy using built in or user define exception types
"" '' # object of the class exception will be created when an exception is raised.
"" '' # exception class inherits from the base exception class
"" '' # Both the StandardError and Warning inherits from the Exception class.
"" '' # Standard errors will terminate program if not handle correctly

"" '' # Examples of errors in python
"" '' # ZeroDivisionError: trying to divide by zero.
"" '' # Indentation error: improper indentation of programming/code blocks.

"" '' # How to handle exception in python?
"" '' # An exception is handled using the try and except block.


"" '' # syntax 
"" '' # try:
'' '' #    code to try
"" '' #    code to try
"" '' #    code to try
"" '' # except ErrorName:
"" '' #     print("message about the error been handle")


"" '' # What does the try and except do with your code?  
"" '' # The try statement works as follows.
"" '' # 1. First, the try clause (the statement(s) between the try and except keywords) is executed.
"" '' # 2. If no exception occurs, the except clause is skipped and execution of the try statement is finished.
"" '' # 3. If an exception occurs during execution of the try clause, the rest of the clause is skipped.
"" '' # Then, if its type matches the exception named after the except keyword, the except clause is executed,
"" '' # and then execution continues after the try/except block.
"" '' # 4. If an exception occurs which does not match the exception named in the except clause,
"" '' # it is passed on to outer try statements; if no handler is found, it is an unhandled exception
"" '' # and execution stops with an error message.


# num1 = int(input("Enter your first number: "))
# num2 = int(input("Enter your second number: "))
# answer = num1 + num2
# print(f"The answer to {num1} + {num2} = {answer}")
# print("Executing...some code and processes")

# # ValueError

try: 
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    answer = num1 + num2
    print(f"The answer to {num1} + {num2} = {answer}")
    print("Executing...some code and processes")

except ValueError:
    print("You must enter an integer value")
print("Executing some code .... ")

except IndexError:
    print("Index value is out of range")
print("Executing some code .... ")



