def longest(a1, a2):
    #will hold the single and ordered letters
    new=[]
    #combines the two lists 
    combined=a1+a2
    #goes through each element in a 
    for char in combined:
        #if it isnt in new then add it too new 
        if char not in new:
            new.append(char)
    #sorts and joins into one string 
    new=sorted(new)
    new="".join(new)
    return new
            
