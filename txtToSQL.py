# Open the file with with data separated by commas
# Convert it to SQL FORMAT

f = open('noSQLFormat.txt')
i = 0
for x in f:
    line = f.readline()
    tc = len(line)
    valeur = '\"' + "," + '\"'
    line = line.replace(",", valeur)

    cara = "\"),"
    lineall = "(\"" + line + cara.rstrip()
    print(lineall)
    i = i+1
    # open a file to append in SQL Format before INSERT, UPDATE or DELETE
    outF = open("SQLFormat.txt", "a")
     # write line to output file
    outF.write(lineall)
    outF.write("\n")
    outF.close()
    line = f.readline()
f.close()
