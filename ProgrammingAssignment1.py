# ------------------------------------------------- main functions ------------------------------------------------------------

def deleteFirstRecord(table):
    print("\n\n")
    print("Are you sure you want to delete the first record? (y/n)")
    option = input("\nEnter your option: ")
    while option != 'y' and option != 'Y' and option != 'n' and option != 'N':
        print("\n\n")
        print("Please enter a valid option (y/n)")
        option = input("\nEnter your option: ")
        if option == 'y' or option == 'Y':
            del table[0] 
            print("\n\n")
            print("The first record was deleted successfully!")
            return
        else:
            print("\n\n")
            print("The first record was not deleted.")
            return


def sumsNumericalField(table):
    totalItemsInStock = 0
    for record in table:
        totalItemsInStock += int(record[3]) 

    print("\n\n")
    print("The total price is: ", totalItemsInStock)
    print("\n\n")


def displayRecordsOnScreen (table):
       for index in range(len(table)):
        (stockID, price, stockDescr, itemsOnStock, itemsOrdered) = table[index]
        print("%-8s%-8.2f%-32s%-4d%-2d" % (stockID, float(price), stockDescr, int(itemsOnStock), int(itemsOrdered) ) )
              


def accendingSort(table): # need to be fixed
    for stockDescr in table:
        listSorted = table.sort(stockDescr)
    print("\n\n")
    print("The sorted Stock is: ", listSorted)
    print("\n\n")










# ------------------------------------------------ MAIN PROGRAM -----------------------------------------------------------------

infile = open('invento.txt')

# (2)
outfile = open('report.txt', 'w')

# (3)
table = [] # starts with an empty list

# (4)
# loads table of records from the file
for data in infile:
    table.append( tuple(data.split() ))

option = '0'
while option != 'Q' or option != 'q':
    print("\n\n")
    print("========MENU========")
    print("1. Delete the first record")
    print("2. Total items in stock")
    print("3. Accending sort for stock")
    print("8. Display the records on the screen")
    print("Q. Quit")

    option = input("\nEnter your option: ")


    if option == '1':
        deleteFirstRecord(table)
    elif option == '2':
        sumsNumericalField(table)
    elif option == '3':
        accendingSort(table)
    elif option == '8':
        displayRecordsOnScreen(table)

print("\n\n")
print(table) # displays the table records

#(6) # closes the files
infile.close()
outfile.close()