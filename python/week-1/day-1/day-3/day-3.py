# for loops
# 1 value = stop point
# 2 values = start, stop
# 3 values = start, stop, step

#ToDo: Task 1: Create a program that uses a for loop to iterate through the letters in your name"
name = "Yvonne"
for letter in name:
    print(letter)
#PRINTS
#Y
#V
#O
#N
#N
#E        

print("Letters in my name")
letterName = "Yvonne"
print(f"Character 1 is: {letterName[0]}")
print(f"Character 2 is: {letterName[1]}")
print(f"Character 3 is: {letterName[2]}")
print(f"Character 4 is: {letterName[3]}")
print(f"Character 5 is: {letterName[4]}")
print(f"Character 6 is: {letterName[5]}")
#PRINTS
#Letters in my name
#Character 1 is: Y
#Character 2 is: v
#Character 3 is: o
#Character 4 is: n
#Character 5 is: n
#Character 6 is: e

number = 4
print ("Guess a number between 1-10")
numGuess = int (input("Guess a number between 1-10"))
while numGuess != number:
    numGuess = int(input("Incorrect\nGuess a number between 1 - 10:"))
    print(f"Tou guessed {numGuess} is corect")
