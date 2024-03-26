"" '' # Objectives
"" '' # Use the r to read from a file

"" '' # Notes
"" '' # There are four modes for opening a file
"" '' # w for only writing to file and creating the file if it does not exists but overwrites existing file contents
"" '' # a for adding to an existing file
"" '' # r for reading and writing files



"To Do: Task 2:Modify the code below to:"
"" '' # Read the contents of your file (yourName.txt) by replacing the:
"" '' # 1. "w" mode after the file path with the "r"
"" '' # 2. the write() method with the read method()
"" '' # 3. Unlike the write mode, no argument is required within the parenthesis of the read mode.
"" '' # 4. Remember to use the print function to display contents in the file
"" '' # 5. Investigate readline() and readlines() methods as you have use the read() method

"Syntax :  varName = openMethod('pathtofolder/parthtofile//fileName.txt', 'r')"
filePath1 = open('cohort-7-week-9-and-10/Pt7_FilesDictsCodeBase2024V2/fileName.txt', 'r') #creates a new file based on the name provided but will not update/edit an existing file 
# folder/folder/filename
# filePath1.write("Python Programming")
# filePath1.close()
#TODO take care to comment out any contradicting code to prevent errors eg. read(), write() etc and make sure to change 'w' or 'r' 'r+' for read and write etc 
print(filePath1.read()) # method 1 to read 
contents = filePath1.read() # method 2 to read - both achieve same outcome 
print(contents)

"Further reading"
# https://www.w3docs.com/snippets/python/how-to-read-a-text-file-into-a-list-or-an-array-with-python.html

