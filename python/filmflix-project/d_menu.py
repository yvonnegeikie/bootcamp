import add_record, read_records, update_records, delete_record, report

# Create a function to read from a text file
def read_file(file_path): 
    try:
        with open(file_path) as open_file:
            rf = open_file.read()
 
            return rf
    except FileNotFoundError as nf:
        print(f"File not found: {nf}")
 
def tblFilms():
    try:
        option = 0 
        optionsList = ["1","2","3","4","5","6"]
 
        # call/invoke the read_file function and assigned it to a variable
        menu_choices = read_file("filmflix-project\db_menu.txt")
 
        # repeat the menu options stored in the menu_choices variable until the option to quit is selected
        while option not in optionsList:
            # use the print(menu_choices) to display the file contents stored in the db_menu.txt file repeatedly
            print(menu_choices)
 
            option = input("Enter an option from the menu above: ")
 
            if option not in optionsList:
                print(f"{option} is not a valid choice")
        return option
    except FileNotFoundError as e:
        print(f"Add error: {e}")
 
mainProgram = True 
 
while mainProgram: # call/invoke the tblFilms and assigned it to a variable
    main_menu = tblFilms()
 
    if main_menu == "1":
        # call the read_records.read_records()
        read_records.read_records()
    elif main_menu == "2":
        add_record.insert_record()
    elif main_menu == "3":
        update_records.update_record()
    elif main_menu == "4":
        delete_record.delete_record()
    elif main_menu == "5":
        report.search_report()
 
    else: # exit the menu and re-assign the value of mainProgram to False
        mainProgram = False
input("Press Enter to exit....")
 