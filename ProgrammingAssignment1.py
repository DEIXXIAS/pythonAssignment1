# ------------------------------------------------- main functions ------------------------------------------------------------


def deleteFirstRecord(table): # function (1) will delete the first record based on user input
    print("\n\n")
    print("Are you sure you want to delete the first record? (y/n)") # final verification to delete the record
    option = input("\nEnter your option: ") # asking for user input while storing the answer within option

    while option != 'y' and option != 'Y' and option != 'n' and option != 'N': # ensuring that the option is not case-sensitive
        print("\nPlease enter either 'y' or 'n'") # if the option given by user is not either (Y/N)
        option = input("Enter your option: ") # user needs to answer w/ either yes or no, otherwise they are forced into a while loop
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


#def largestValue(table): # function (3) finds the largest value for in-stock items








def accendingSort(table):  # function (4) sorts the table items based on name in ascending order
    for index in table:
        newList = str(index[2])
    sortedList = sorted(newList)
    print("\n")
    print("The sorted Stock is: ", sortedList)
    print("\n")


#def descendingSort(table): # function (5) sorts the table items based on name in descending order






def printReport(table): #function (6) prints the table of records to REPORT.TXT (Sorta works)
    outfile = 'report.txt'
    with open(outfile, 'w') as file_object:
        file_object.write("\nID # - Price -- Stock Item ------------------ Item in Stock - Items Ordered ")# header format
        file_object.write("\n")
        for index in table:
            file_object.writelines("{}\n".format(index))
            file_object.write("\n")
        file_object.close()




def IDrecordDelete(table): # function (7) deletes a record based off a ID Key
    displayRecordsOnScreen(table)
    print("\n")
    KeyID = input("\nEnter the ID # to delete, or enter Q to quit: ")
    while KeyID != 'q' and KeyID != 'Q':
        for index in table:
            if (index[0]) == (KeyID):
                del table[index]
            else:
                print("\nPlease enter a valid ID # to delete")
    print("\nID # was not deleted.")



def displayRecordsOnScreen(table): # function (8) displays the records of the list
    print("\nID # - Price -- Stock Item ------------------ Item in Stock - Items Ordered ") # header format
    for index in range(len(table)): # while going through the range of the list
        (stockID, price, stockDescr, itemsOnStock, itemsOrdered) = table[index] # order the items in each index
        print("%-8s%-8.2f%-32s%-4d%12d" % (stockID, float(price), stockDescr, int(itemsOnStock), int(itemsOrdered))) #print formatting for the list


# ------------------------------------------------ MAIN PROGRAM -----------------------------------------------------------------

infile = open('invento.txt')


# (3)
table = [] # starts with an empty list

# (4)
# loads table of records from the file
for data in infile:
    table.append( tuple(data.split() ))

option = '0'
while option != 'Q' or option != 'q':
    print("\n\n")
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

    option = input("\nEnter your option: ")


    if option == '1':
        deleteFirstRecord(table)
    elif option == '2':
        sumsNumericalField(table)
    elif option == '3':
        largestValue(table)
    elif option == '4':
        accendingSort(table)
    elif option == '5':
        descendingSort(table)
    elif option == '6':
        printReport(table)
    elif option == '7':
        IDrecordDelete(table)
    elif option == '8':
        displayRecordsOnScreen(table)

print("\n\n")
print(table) # displays the table records

#(6) # closes the files
infile.close()