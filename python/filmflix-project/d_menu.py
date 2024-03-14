import add_record, read_records, update_records, delete_record, report

# Create a function to read from a text file
def read_file(file_path): #file_path is the parameter or value
    try:
        with open(file_path) as open_file:
            # read() reads the file content and save it in the variable called rf
            rf = open_file.read()
 
            return rf
    except FileNotFoundError as nf:
        print(f"File not found: {nf}")
 
def tblFilms():
    try:
        option = 0 # initialise the option variable with the integer value 0
        optionsList = ["1","2","3","4","5","6"] # create a list data structure with string values
 
        # call/invoke the read_file function and assigned it to a variable
        menu_choices = read_file("filmflix-project/filmflix 2.db")
 
        # repeat the menu options stored in the menu_choices variable until the option to quit is selected
        while option not in optionsList:
            # use the print(menu_choices) to display the file contents stored in the dbmenu.txt file repeatedly
            print(menu_choices)
 
            # re-assign the option variable as a string value
            option = input("Enter an option from the menu above: ")
 
            # check if the input provided/stored in the re-assigned
            # option variable is present in the optionsList variable
            if option not in optionsList:
                print(f"{option} is not a valid choice")
        return option
    except FileNotFoundError as e:
        print(f"Add error: {e}")
 
# create a boolean Variable
mainProgram = True #can be toggle to False to exit out off the loop below
 
while mainProgram: # same as while True
    # call/invoke the tblFilms and assigned it to a variable
    main_menu = tblFilms()
 
    if main_menu == "1":
        # call the readrecords.read_records()
        readrecords.read_records()
    elif main_menu == "2":
        addrecord.insert_record()
    elif main_menu == "3":
        updaterecordV2.update_record()
    elif main_menu == "4":
        deleterecord.delete_record()
    elif main_menu == "5":
        report.search_report()
 
    else: # exit the menu and re-assign the value of mainProgram to False
        mainProgram = False
input("Press Enter to exit....")
 