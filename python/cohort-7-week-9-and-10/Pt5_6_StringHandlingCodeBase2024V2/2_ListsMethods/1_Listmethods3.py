"Objectives"
"" '' # Understand the different types of list methods
"" '' # Be able to apply list method(s) to a list


"" '' # Notes
"" '' # Think of list methods as special functions that are applied to lists. 
"" '' # To call a list method, you need to use dot notation (as in the examples that follow). 
"" '' # Method is a function that belongs to an object.

"" '' # Use list methods to:
    #  list.append(item)"        # add item at end of list
    #  list.insert(index,item)   "  # add item at index
    #  list.pop(index)"       # remove item at index
    #  list.remove(item)   "  # remove item
    #  list.index(item)   "  # search for index of item
    #  list.count(item)"  # get occurrences of item
    #  list.reverse()"   # reverse list
    #  list.sort()"      # sort list

"" '' # Custom  built function:  A function that you have created yourself and imported into other programs that you have created.
"" '' # List: A dynamic data structure that holds items under one name. The items can be of varying data types.


"" '' # Traverse is to move through a sequence.
"" '' # You can use a for loop to traverse a list of elements

"" '' # Task 3:
"" '' # "Use any of two list methods from above to perform operation on the list below called, listOfNames.
#                  0         1         2        3         4        6       7
listOfNames = ["Nicole", "Laura", "Silvia", "Steve", "Juliet", "Laura", "Silvia"]
print(listOfNames)  # Prints the list
print(listOfNames[2])  # Prints Silvia

"" '' #  Task 4: Predict, run and investigate the code above
"" '' #  What is the len() used for in the code below?"
for index in range(len(listOfNames)):
    print(f"{index} : {listOfNames[index]}")

print(f"\n{listOfNames}")

"" '' # Question: What item is returned from the list and why, when the print statment below is executed?
print(f"{listOfNames[3]}\n")


"" '' # Refer to https://www.w3docs.com/learn-python/python-lists.html to support you completeing the tasks if you need to 

