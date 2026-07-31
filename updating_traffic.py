def update_light(current):
    #list for traffic light colours 
    lights=["green","yellow","red"]
    #if current is a interger it will return none
    if type(current)==int:
        return None
    #if the lowercase of current equals red it will return green
    elif current.lower()=="red":
        return lights[0]
    #this for loop will check the current lowercase is equal to lights element and return the next elewment
    for i in range (len(lights)):
        if lights[i]==current.lower():
            return lights[i+1]
    else:
        #if it doesnt fit these conditions return None
        return None
