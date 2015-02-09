def ComputePay(h,r):
    print "In ComputePay h= ",h," r= ",r
    if h<= 40:
        p = r * h
    else:
        p = r*40 +(r*1.5*(h-40))
    print"Finished with ComputePay",p
    return p

try:
    inp = raw_input("Please enter number of Hours:")
    hours = float(inp)
    inp = raw_input("Please enter rate of pay for Hour:")
    rate = float(inp)
except:
    print "Error,Please enter numeric input"
    quit()

print "In the main code",rate,hours
pay = ComputePay(hours,rate)
print "We are back ",pay