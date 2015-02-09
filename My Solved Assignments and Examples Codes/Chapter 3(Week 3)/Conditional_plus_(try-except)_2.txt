try:
    inp = raw_input("Please enter number of Hours:")
    hours = float(inp)
    inp = raw_input("Please enter rate of pay for Hour:")
    rate = float(inp)
except:
    print "Error,Please enter numeric input"
    quit()
print "Hours : ",hours,"Rate : ",rate
if hours<= 40:
    pay = rate * hours

else:
    pay = rate*40 +(rate*1.5*(hours-40))

print "Amount of pay for total working hours is: ",pay

