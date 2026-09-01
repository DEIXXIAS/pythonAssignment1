# (1)
infile = open('invento.txt')

# (2)
outfile = open('report.txt', 'w')

# (3)
table = list() # starts with an empty list

# (4)
# loads table of records from the file
for data in infile:
    table.append( tuple(data.split() ))

# (5)
print(table) # displays the table of records

#(6) # closes the files
infile.close()
outfile.close()
