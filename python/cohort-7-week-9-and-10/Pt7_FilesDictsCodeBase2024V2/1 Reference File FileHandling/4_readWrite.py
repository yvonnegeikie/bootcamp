"Objectives"
"" '' # Use the r+ to read and write to a file

"" '' # Notes:
"" '' # In order to read the data stored in a text file, you must open it first. 
"" '' # Just like a book. You cant read what is inside if you dont open it first.
"" '' # There are four modes for opening a file:
"" '' # r for only reading files
"" '' # w for only writing to file and creating the file if it does not exists but overwrites existing file contents
"" '' # a for adding to an existing file
"" '' # r+ for reading and writing files


with open('pathtofolder/parthtofile/fileName.txt',"r+") as filePath1:# folder/folder/filename
    print(filePath1.read()) #read from file
    readContents = filePath1.read()
    print(readContents)
    contents ="\nYourA\ntext\ngoes\nhere\nin\nnewlines"
    filePath1.write(contents) #write to file 

"" '' # To Do: Task 1: Modify the code above to
"" '' # Read the contents from your file (yourName.txt) and write to your file  
"" '' # use the with the correct mode and ensure you use both the read and the write() methods to perform their respective operations


