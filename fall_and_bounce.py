def bouncing_ball(h, bounce, window):
    #checks if it doesnt fit the requirements 
    #if it doesnt it will return -1
    if not (h>0 and bounce>0.0 and bounce<1.0 and window<h):
        return -1
    #calclautes the inital decreses meaning it will start at 1 fall
    num=h*bounce
    total=1
    #while num is greater than window it will add 2 for a fall and bounce
    #it will also decrease num each time
    while num>window:
        total+=2
        num=num*bounce
    #returns the times the person at the window could see it 
    return total
        
        
