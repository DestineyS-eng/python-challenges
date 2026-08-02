def move_zeros(lst):
    #will hold the new list 
    new=[]
    #will take the count of os in the list 
    count=lst.count(0)
    #will go through each character in the list 
    for char in lst:
        #if the character doesnt equal 0 add it too new list 
        if not char== 0:
            new.append(char)
    #for the 0s counted they will add a 0 to the end of new list
    for i in range (0,(count)):
        new.append(0)
    return new
