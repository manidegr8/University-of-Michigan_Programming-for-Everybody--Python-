score = raw_input("Pls give score:")
print "Score is: ",score
s = float(score)
try:
    if s >= 0.9 and s<1.0:
            print "A"

except:
    print "error,Value is out of range"
    exit()