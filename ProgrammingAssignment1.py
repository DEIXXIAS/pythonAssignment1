# ------------------------------------------------- main functions ------------------------------------------------------------

def deleteFirstRecord (table):  
    return table[1:] # returns a new list without the first record
 



def displayRecordsOnScreen (table):
        for index in range(len(table)):
            (stockID, price, stockDescr, itemsOnStock, itemsOrdered) = table(index)

        print("%-2d%-8s%-8.2f%-29s%-4d%-2d" % (int(index + 1), stockID, float(price), stockDescr, int(itemsOnStock), int(itemsOrdered) ) )
              











# ------------------------------------------------ MAIN PROGRAM -----------------------------------------------------------------

infile = open('invento.txt')

# (2)
outfile = open('report.txt', 'w')

# (3)
table = list() # starts with an empty list

# (4)
# loads table of records from the file
for data in infile:
    table.append( tuple(data.split() ))

option = '0'
while option != 'Q':
    print("========MENU========")
    print("1. Delete the first record")
    print("8. Display the records on the screen")
    print("Q. Quit")

    option = input("\nEnter your option: ")


    if option == '9':
        displayRecordsOnScreen(table)

print("\n\n")
print(table) # displays the table records

#(6) # closes the files
infile.close()
outfile.close()