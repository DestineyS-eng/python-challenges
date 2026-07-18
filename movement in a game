def is_valid_walk(walk):
 # reprresents a x-axis and y-axis for compass movement (n,e,s,w) and the count of steps as it must equal 10    
    start=[0,0] 
    total=0     
#the range of the list containing compass directions    
    for i in range (len(walk)): 
#this section is designed to add one to the total after evey direction as it takes 1 min each time. it will also subract or add from the x or y axis depending on the movement 
        if walk[i]=="n":
            total+=1
            start[1]=start[1]+1
        elif walk[i]=="s":
            total+=1
            start[1]=start[1]-1
        elif walk[i]=="w":
            total+=1
            start[0]=start[0]-1
        elif walk[i]=="e":
            total+=1
            start[0]=start[0]+1
    if start==[0,0] and total==10:
#this section will return true if it took 10 mins and they are at the starting position again 
        return True
    else:
        return False
        
        
            
