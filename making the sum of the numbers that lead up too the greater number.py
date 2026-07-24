def get_sum(a,b):
    m=[a,b] #puts the two numbers into a list 
    mylist=sorted(m) #sorts the list
    diff=mylist[1] - mylist[0] #finds the diffrence of the two numbers
    total=mylist[0] #for loop will add one from this value till  diff is pasted
    overall=mylist[0] # overall total is all numbers added togther that are created from total
    for i in range (diff):
        total=total+1
        overall=overall+total
    return overall
