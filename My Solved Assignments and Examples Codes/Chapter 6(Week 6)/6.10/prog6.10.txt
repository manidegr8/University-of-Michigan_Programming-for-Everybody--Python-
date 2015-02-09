
text = "X-DSPAM-Confidence:    0.8475"
print text
pos = text.find(':')
print pos
print text[pos+1:]
string = text[pos+1:]
print "Copy of String:",string
print text[pos+1:].strip()
print text[pos+1:].lstrip()
num = float(text[pos+1:])
print num
text = text[pos+1:].lstrip()
print text



