
def main():
    pass

if __name__ == '__main__':
    main()
line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
print words
email = words[1]
pieces = email.split('@')
print '\n',pieces
print pieces[1]