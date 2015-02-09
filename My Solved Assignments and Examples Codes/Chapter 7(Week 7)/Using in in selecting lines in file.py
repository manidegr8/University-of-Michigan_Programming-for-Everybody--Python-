akhil = open('UserDetails.txt')
for line in akhil:
    line = line.rstrip()
    if not 'student' in line :
        continue
    print line