def accum(st):
#seperating each string to be indiviual 
    letters=[str(i) for i in str(st)]
#storing the inital letter as it will always be upper and one 
    hyphen=letters[0].upper()
    for i in range (1,len(letters)):
    #adding the uppercase letter and the repeat if its lower case using i
        lower=letters[i].lower()
        hyphen+="-"+letters[i].upper()+lower*i
    return hyphen
