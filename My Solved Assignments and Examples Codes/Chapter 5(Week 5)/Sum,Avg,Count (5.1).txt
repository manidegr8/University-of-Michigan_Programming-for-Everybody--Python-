# Code to get total of set of Numbers , Average and Count

count = 0
total = 0

while True:
    inp = raw_input('Enter a number: ')

    # Handle the edge Cases
    if inp == "done" : break
    if len(inp) < 1: break                      # (Ideom) Check for Empty Line

    # Do the work
    try:
        num = float(inp)

    except:
        print 'Invalid Input'
        continue
    count = count + 1
    total = total + num

    print num, total ,count

print 'Average:', total/count

