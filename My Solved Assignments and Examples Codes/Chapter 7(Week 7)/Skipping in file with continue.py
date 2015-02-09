fhand = open('UserDetails.txt')
for line in fhand:
    line = line.rstrip()
    if  line.startswith('1') : # 'or' if not line.startswith('1') :
        continue
    print line