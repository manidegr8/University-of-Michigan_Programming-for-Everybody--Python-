fname = raw_input('Enter the file name:  ')
Lithin = open(fname)
count = 0
for line in Lithin:
    if line.startswith('1') :
        count = count + 1
print 'There were', count, 'subject lines in', fname
