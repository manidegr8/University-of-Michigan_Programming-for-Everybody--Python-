# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
sum = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    pos = line.find(':')
    #print pos
    #print line[pos+1:]
    string = line[pos+1:]
    #print "Copy of String:",string
    #print line[pos+1:].strip()
    #print line[pos+1:].lstrip()
    num = float(line[pos+1:])
    print num
    count = count + 1
    sum = sum + num
    #print line

print '\nSum of Extracted numbers is:',sum,'\n'

print "Average of Extracted numbers is:",(sum/count),'\n'
print "Done"
