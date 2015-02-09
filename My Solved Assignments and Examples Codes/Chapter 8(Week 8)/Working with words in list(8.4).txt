
def main():
    pass

if __name__ == '__main__':
    main()
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
   # print line.rstrip()
    words = line.split()
    print words
    for word in words:
      print word
      lst.append(word)

row = []
for word in lst:
    if word not in row:
            row.append(word)

#print lst
row.sort()
print row


