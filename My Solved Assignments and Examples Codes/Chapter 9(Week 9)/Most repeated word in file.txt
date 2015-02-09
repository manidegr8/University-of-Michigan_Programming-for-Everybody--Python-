#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      AKHIL REDDY
#
# Created:     08/12/2014
# Copyright:   (c) AKHIL REDDY 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

def Input():
    name = raw_input("Enter File")
    handle = open(name)
    text = handle.read()
    words = text.split()
    return words

if __name__ == '__main__':
    main()
    words = Input()
    counts = dict()
    for word in words:
        counts[word]=counts.get(word,0)+1
    bigcount = 0
    bigword = None
    for word,count in counts.items():
        if bigcount == None or count > bigcount:
            bigword = word
            bigcount = count
    print bigword,bigcount
