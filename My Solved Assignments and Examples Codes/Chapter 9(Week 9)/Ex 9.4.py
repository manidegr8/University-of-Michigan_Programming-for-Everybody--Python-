name = raw_input("Enter file:")
if len(name) < 1 :
     name = "mbox-short.txt"
handle = open(name)

wordsl = list()
#count = -1
for line in handle:
     line = line.rstrip()
     if not line.startswith('From ') : continue
     words = line.split()
    # print words[1]
    # count = count + 1
    # wordsl[count] = words[1]
     wordsl.append(words[1])


for word in wordsl:
     print word

counts = dict()
for word in wordsl:
    counts[word]=counts.get(word,0)+1
bigcount = 0
bigword = None
for word,count in counts.items():
    if bigcount == None or count > bigcount:
        bigword = word
        bigcount = count
print bigword,bigcount