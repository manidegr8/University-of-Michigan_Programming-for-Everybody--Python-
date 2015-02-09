name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

wordsl = list()
counts = dict()
for line in handle:
     line = line.rstrip()
     if not line.startswith('From ') : continue
     words = line.split()
     pieces = words[5].split(':')
    #print pieces[0]
     wordsl.append(pieces[0])

#for word in wordsl:
    #print word

for word in wordsl:
    counts[word] = counts.get(word, 0 ) + 1

lst = list()
for key, val in counts.items():
    lst.append( (key, val) )
#lst.sort(reverse=True)
lst.sort()
for val, key in lst:
    print val, key