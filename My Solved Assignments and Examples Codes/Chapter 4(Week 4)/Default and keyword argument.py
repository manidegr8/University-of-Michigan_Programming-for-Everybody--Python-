def get_gender(sex='Unknown'):
    if sex is 'm':
        sex = 'male'
    elif sex is 'f':
        sex = 'female'
    print (sex)

def dumb_sentence(name = 'Lilly',action = 'litter',item = 'smell'):
    print "It's normal to say",name,"always",action,item


get_gender('m')
get_gender('f')
get_gender()

dumb_sentence()
dumb_sentence(name='bully')
dumb_sentence('akhil','esshi','tasty')