fhand = open('UserDetails.txt')
for line in fhand:
    line = line.rstrip() #Used to leave newline in text file
    if line.startswith('1'):
        print line

