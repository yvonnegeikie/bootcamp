"" '' # Break in Python Python break is generally used to terminate a loop. 
"" '' # This means whenever the interpreter encounters the break keyword, 
"" '' # it simply exits out of the loop. Once it breaks out of the loop, 
"" '' # the control shifts to the immediate next statement.

"" '' # To Do: Predict, then Run, and then Investigate"

"" '' #How to combine iteration and Selection"

numList = [1, 3, 4, 6, 1, 3, 5, 7]

found = False
for number in numList:
    if number == 30:
        print("Found", number)
        found = True
        break
    else:
        print(f"Number {number} not found")

if not found:
    print("Number 3 not found in the list")

