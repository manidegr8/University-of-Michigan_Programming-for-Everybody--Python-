# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip().upper()
   # line = line.upper()
    print line
