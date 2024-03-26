"Objectives"
"" '' # Understand what is a while Loop 
"" '' # Use a while Loop to repeatedly executes a block of code as long as a specified condition remains true

"" '' # Notes
"" '' # Iteration is the repetition of code blocks. For example, a while loop or a for loop.
"" '' # while loop is used when the number of iteration is unknown(dont know how many times you want/going to do something for)
"" '' # A while loop also controls the flow of execution in a program

"" '' # When to use a while loop?
"" '' # When the number of iteration is unknown(dont know how many times you want/going to do something for)
"" '' # When your program needs to repeat actions, while a condition is satisfied


"To Do: Predict, then Run, and then Investigate"
"" '' # syntax
"" '' # while condition is true:
"" '' #    do this:

# number = 4 # define a number between  1-10
# numGuess = int(input("Guess a number between 1 and 10: ")) # get user input 
# while numGuess != number: # if number is NOT 4, keep asking hte question. Will keep looping until the number is 4. 
#    numGuess = int(input("Incorrect\nGuess a number between 1 and 10: "))
# print(f"You guessed {numGuess} is correct")

number = 4
while True:
   numGuess = int(input("Guess a number between 1 and 10: "))
 
   if numGuess == number:
      print(f"You guessed {numGuess} is correct")
      break
   else:
      print(f"Incorrect guess try again")



"" '' # To Do: Task1: Add comments to the code above to explain what the while loop is doing
"" '' # Further reading on python while statements"
# https://www.w3schools.com/python/ref_keyword_while.asp