
def main():
    pass
count = 0
if __name__ == '__main__':
    main()
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
for line in fh:
     line = line.rstrip()
     if not line.startswith('From ') : continue
     words = line.split()
     count = count + 1
     #print words[1]
     pieces = words[1].split('@')
     print pieces[1]

print "There were", count, "lines in the file with From as the first word"
