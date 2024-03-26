"Objectives"
"" '' # Understand what is a match case 
"" '' # Use a while Loop to repeatedly executes a block of code as long as a specified condition remains true# Read though the code below:


"" '' # Notes
"" '' # A match statement takes an expression and compares its value to successive
"" '' # patterns given as one or more case blocks. Specifically, pattern matching operates by:
"" '' #  -- 1. using data with type and shape (the subject)
"" '' #  -- 2. evaluating the subject in the match statement
"" '' #  -- 3. comparing the subject with each pattern in a case statement from top to bottom until a match is confirmed.
"" '' #  -- 4. executing the action associated with the pattern of the confirmed match
"" '' #  -- 5. If an exact match is not confirmed, the last case, a wildcard_, if provided, will be used as the matching case.


"" '' # syntax 
"" '' # match subject:
"" '' #     case <pattern_1>:
"" '' #         <action_1>
"" '' #     case <pattern_2>:
"" '' #         <action_2>
"" '' #     case <pattern_3>:
"" '' #         <action_3>
"" '' #     case _:
"" '' #         <action_wil

import random

weeks = ["wk1", "wk2", "wk3", "wk4", "wk5", "wk6", "wk7", "wk8", "wk9", "wk10", "wk11", "wk12"] # creating a list 
aWeek = random.choice(weeks) # generating a random choice from the list 
print(aWeek) # random value will be printed 

match aWeek: # prints specified message according to the wk randomly selected # cleaner code than using if/else for all 
    case "wk1":
        print("Welcome to SDLC.")
    case "wk2":
        print("Welcome HTML.")
    case "wk3":
        print("Welcome to CSS.")
    case "wk4":
        print("Still CSS week.")
    case "wk5":
        print("Welcome to JavaScript.")
    case "wk6":
        print("Welcome JavaScript project.")
    case "wk7":
        print("Welcome to Database.")
    case "wk8":
        print("Still database week.")
    case "wk9":
        print("Welcome Python .")
    case "wk10":
        print("Still Python week.")
    case "wk11":
        print("Welcome Python Project week.")
    case "wk12":
        cohortName = input("Enter cohort name: ")
        if cohortName == "Man":
            print("Microsoft Azure week.")
        else:
            print("Portfolio week.")
    # In the last case block, we defined case _, where the variable 
    # name _ acts as a wildcard and it will never fail to match.
    # If no case matches in the upper code then the last case block is executed.
    case _:
        print("Matches anything.")

  