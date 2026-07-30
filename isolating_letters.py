def unique_in_order(seq):
    #new list to collect singles values 
    newlist=[]
    for x in range (len(seq)):
        #if x==0 this means the frist position is stored in the new list 
        if x==0:
            newlist.append(seq[x])
        elif seq[x-1]!=seq[x] :
            #if the letter/number before and arent equal append the current x as its the frist position 
            newlist.append(seq[x])
    return newlist
        
