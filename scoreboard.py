def points(games):
    #will hold the total score 
    total=0
    #will go through the list allowing us to assign values 
    for number in games:
        #we will assign the numbers left after turning ":" into a partition directly into x and y
        x,y= number.split(":")
        #compares the number to see which score should be assigned
        if int(x)>int(y):
            total+=3
        elif int(x)==int(y):
            total+=1
    return total
    
