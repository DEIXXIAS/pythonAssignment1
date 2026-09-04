# ------------------------------------------------- main functions ------------------------------------------------------------

def deleteFirstRecord(table): # function (1) will delete the first record based on user input
    print("\n\n") # ensuring that the option is not case-sensitive
    print("\nAre you sure you want to delete the first record? (y/n)") # if the option given by user is not either (Y/N)
    option = input("Enter your option: ") # user needs to answer w/ either yes or no, otherwise they are forced into a while loop

    while option != 'y' and option != 'Y' and option != 'n' and option != 'N': # ensuring that the option is not case-sensitive
        print("\nPlease enter either 'y' or 'n'") # reprompting if entered in a bad option
        option = input("Enter your option:") # reprompting
    if option == 'y' or option == 'Y': # if the user wants to delete the record
            del table[0] # the first table within the list is deleted
            print("\nThe first record has been deleted successfully!") # message confirmation is sent back
            print("\n") # spacing
    else: # if a user decides not to delete the records
            print("\nThe first record was not deleted.") # user will receive message confirmation
            print("\n") #spacing


def sumsNumericalField(table): # function (2) grabs all current prices for books available in the list
    totalPrice4Items = 0 # starts off with 0
    for index in table: # while each index in the table is being read
        totalPrice4Items += float(index[1]) # we are grabbing the float number for the prices of each item and storing it in totalPrice
    formattedNum = "%.2f" % totalPrice4Items # to format the numbers better, this executes after the end of the for loop
    print("\n") # spacing
    print("The total price is: $",formattedNum) # message confirmation with total price for all items


def largestValue(table): # function (3) finds the largest value for in-stock items
    inStockItems = [] # holds an empty list for the in-stock items
    for index in table: # while going through each index in the table
        inStockItems.append(int(index[3])) # store the in-stock values into the empty list
    print("\nLargest value for in-stock items is:", max(inStockItems)) # print the largest value in the list


def ascendingSort(table):  # function (4) sorts the table items based on name in ascending order
    ascendList = [] # empty ascending list
    counter = int(0) # initializing my variables
    for index in table: # while going through each index in the table
        ascendList.append(str(index[2]))  # append each name description to the empty list
    sortedList = sorted(ascendList) # sort each name and place into the sorted list
    print("\n")
    print("The stock in ascending order is: ") # printing header
    while counter < len(sortedList): # while going through each index in the sorted list
        print(sortedList[counter]) # print each name separately
        counter += 1 # increase counter
    return


def descendingSort(table): # function (5) sorts the table items based on name in descending order
    descList = [] # empty descending list
    counter = int(0)  # initializing my variables
    for index in table: # while going through each index in the table
        descList.append(str(index[2])) # append each name to the empty list
    sortedList = sorted(descList, reverse=True) # sort the names in descending order and place into a sorted list
    print("\n")
    print("The stock in descending order is: ") # printing header
    while counter < len(sortedList): # while going through each index in the sorted list
        print(sortedList[counter]) # print each name separately
        counter += 1 # increase counter
    return


def printReport(table): #function (6) prints the table of records to REPORT.TXT (Sorta works)
    outfile = 'report.txt' # assigning the outfile (as report.txt)
    index = int(0) # initializing my variables
    with open(outfile, 'w') as file_object:  # while the file is open and is being written with file_object
        file_object.write("\nID # - Price -- Stock Item ------------------ Item in Stock - Items Ordered ")# header format
        file_object.write("\n") # spacing
        while index < len(table): # while going through each index in the table
            file_object.writelines("{}\n".format(table[index])) # writing the indexes for each row in the table
            file_object.write("\n") # spacing for the table
            index += 1 # increasing the index
        print("\nReport has been printed successfully!") # after everything prints, printing a confirmation message
        file_object.close() # closing the file after


def IDrecordDelete(table): # function (7) deletes a record based off an ID Key
    displayRecordsOnScreen(table) # display records on the screen so user can see record ID, even if they did not prompt before
    index = int(0) # initializing my variables
    IDfound = bool(False) # initializing my boolean value
    print("\n") # spacing for prompt
    keyID = input("\nEnter the ID # to delete: ") # prompting the user for input for ID #
    while IDfound is False and index < len(table): # while the ID has not been found and the index is less than the length of the table
        if keyID == table[index][0]: # go through each key ID and if it equals the table index for ID #
            IDfound = True # boolean switches to true
            del table[index] # the table index that is storing that value is deleted
            print("The ID # has been deleted.") # confirmation message
        else: # otherwise if not found
            index += 1 # increase the index by one
    print("\nID # could not be found") # error message is displayed if the ID # could not be found
    return # returns to menu


def displayRecordsOnScreen(table): # function (8) displays the records of the list
    print("\nID # - Price -- Stock Item ------------------ Item in Stock - Items Ordered ") # header format
    for index in range(len(table)): # while going through the range of the list
        (stockID, price, stockDescr, itemsOnStock, itemsOrdered) = table[index] # order the items in each index
        print("%-8s%-8.2f%-32s%-4d%12d" % (stockID, float(price), stockDescr, int(itemsOnStock), int(itemsOrdered))) #print formatting for the list


# ------------------------------------------------ MAIN PROGRAM -----------------------------------------------------------------

infile = open('invento.txt') #opening up the table from the files

table = [] # starts with an empty list

for data in infile: # while going through each index of the infile
    table.append( tuple(data.split() )) # they are split into different places and placed into the empty table list

option = '0' # initializing my variable
while option != 'q' or  option != 'Q': # while the initial variable is not 'quit'
    print("\n\n") # spacing for menu
    print("++++============MENU============++++")
    print("1. Delete the first record")
    print("2. Total price for all current items")
    print("3. The largest value for in-stock items")
    print("4. Ascending sort for stock")
    print("5. Descending sort for stock")
    print("6. Print current list to Report file")
    print("7. Delete a record based on Stock ID")
    print("8. Display the records on the screen")
    print("Q. Quit")

    option = input("\nEnter your option: ") # prompting for user input


    if option == '1': # function one
        deleteFirstRecord(table)
    elif option == '2': # function two
        sumsNumericalField(table)
    elif option == '3': # function three
        largestValue(table)
    elif option == '4': # function four
        ascendingSort(table)
    elif option == '5': # function five
        descendingSort(table)
    elif option == '6': # function six
        printReport(table)
    elif option == '7': # function seven
        IDrecordDelete(table)
    elif option == '8': # function eight
        displayRecordsOnScreen(table)
    elif option == 'Q' or option == 'q': # when user inputs 'Q', which quits the program
        infile.close() # closes the infile (invento.txt)
        print("\n\n") # spacing for the end message
        print("Thank you for using this program!") # output
        print("Quitting...") # verification for exiting
        print("\n") # spacing
        exit() # closes the program
    else: # if the user does not choose a valid option
        option = input("Please enter a valid option: ") # user will be reprompted