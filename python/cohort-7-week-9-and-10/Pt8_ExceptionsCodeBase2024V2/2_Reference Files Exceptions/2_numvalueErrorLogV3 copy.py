import logging
import time
"" ''  # objectives
"" ''  # To configure and log to a file the respective error messages.
"" ''  # Use different logging methods with their severity level(s)
"" ''  # Use try and except to log Errors and Exceptions in a file
"" ''  # log errors with date and timestamp 



"" ''  # To Do: Task 1: Modify
"" ''  # 1. Use your knowledge from working with files to log the errors to the correct folder
"" ''  # 2. Explain what functionality the time.asctime() adds to the program 

logging.basicConfig(filename=r"cohort-7-week-9-and-10\Pt8_ExceptionsCodeBase2024V2/file4.log", 
                    level=logging.DEBUG,
                    format='%(asctime)s[user:%(name)-2s] %(levelname)-2s[Line %(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M',
                    filemode='a') 

try:  # attempt to run the indented code block
    num1 = int(input(("Enter your first number: ")))
    num2 = int(input(("Enter your second number: ")))
    answer = num1 / num2
    

except ZeroDivisionError:  # handles exception if code in try block fails
    #Output for user/what the user see
    print("You can't divide a number by zero")
     #Output for developer/what the developer see
    logging.warning("User attempted to divide by zero")
    # logs 22-03-2024 10:27 WARNING[Line 31] User attempted to divide by zero

else:
    #Output for user/what the user see
    print(f"The answer to {num1} / {num2} = {answer}")
    #Output for developer/what the developer see
    logging.info(f"Divided {num1} / {num2} = {answer}")
finally:
    print("Closing....") 
    


