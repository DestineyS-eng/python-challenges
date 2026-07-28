def array_diff(a, b):
    #holds the new list
    new_list=[]
    #assume everying is true unless proven
    for i in a:
        opt=True
        #if b is equal to i its false as then we have to remove it 
        for x in range (len(b)):
            if b[x]==i:
                opt=False
                #stops loooking through b
                break
                
        if opt:
            #if list b is empty return list a as it is 
            new_list.append(i)
    return new_list
