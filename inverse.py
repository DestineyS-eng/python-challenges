def invert(lst):
    #holds the inverse list
    new=[]
    #looks at each element in lst
    for num in lst:
        #if its a posistve number return its negative
        #else return the postive 
        if num>0:
            new.append(-num)
        else:
            num=str(num).replace("-","")
            new.append(int(num))
    return new
