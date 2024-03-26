"Objectives"
"" '' # Understand Variable Scope
"" '' # Understand what is global scope variable
"" '' # Understand what is a local scope variable
"" '' # Use global scope variable and Local scope variable 


"" '' # What is a variable Scope
"" '' # The scope of a variable is the section of the program where the variable can be accessed and modified.


"" '' # What is a global scope and local scope?
"" '' # Variables can either have global scope or local scope. 

"" '' #  What is a Global scope variabe?
"" '' #  Global scope refers to a variable that can be accessed and modified from anywhere in the program, even from inside subroutines. 
"" '' #  A variable declared in the main part of the program can be accessed globally by all subroutines. 
"" '' #  It cannot be modified unless you explicitly state that the program should modify the global variable. 

"" '' # What is a Local scope variable 
"" '' # Local scope refers to variables that can only be accessed and modified within the code block that they were declared.  


"" '' # Handling Variable Scope
"" '' # Not all programming languages handle scope in the same way Python has been designed to discourage the modification 
"" '' # of global variables, research to find out why and see link below after the exemplar code block of accessing global variables inside a function.
"" '' # Variables are local unless otherwise declared. 


"" '' # Task 3: Predict, then Run, and then Investigate the code from line 63 - 71, comment out other lines of code that if you need to.
"" '' # comment and uncomment line 62 when you run the block of code and explain the difference
"" '' # Now call the function 'localSubGlobalVariable()' while you comment and uncomment line 62 when you run the block of code and explain the difference

"" '' # Variables are local unless otherwise declared.
globalVarNum2 = 100

def localSubGlobalVariable():
    # The use of the global keyword ensure this variable can now be accessed globally
    global globalVarNum2
    globalVarNum2 = 15
    print(f"This is globalVarNum2 variable with a value {globalVarNum2} defined from inside the function localSubGlobalVariable()")

localSubGlobalVariable() # call/invoke localSubGlobalVariable()
print(f"This is a globalVarNum2 variable with a value {globalVarNum2} defined on line 63 outside any function ")

# Use the link below for required further reading
# https://www.programiz.com/python-programming/global-keyword




