"Objectives"
"" '' # Understand the purpose of parameter and argument
"" '' # Use parameter(s) and argument(s)


"" '' # Functions that uses parameter and arguments are more modular, reuseable, adaptable , flexible and readable.


"" '' # 5. Default values (assign a default value for the greet parameter)
def welcome(name, greet="Welcome"): # assign a default value for the greet parameter
    print(f"{greet}, {name}")

"" '' # call/invoke welcome function
welcome("James") # uses the default value for the greet parameter = "Welcome"

"" '' # 5. Keyword arguments (pass arguments by explicitly specifying the name of the parameter(s)) and  3. Multiple arguments 
welcome("Anna", greet="Goodbye") # overwrite /provide a custom variable for the greet parameter
