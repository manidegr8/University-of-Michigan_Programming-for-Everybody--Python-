text = "X-DSPAM-Confidence:    0.8475";
#print text
pos = text.find(':');
#print pos
#print text[pos+1:]
string = text[pos+1:];
num = float(string);
print num;