def feast(beast, dish):
    #gets the position of the last letter
    length1=len(beast)-1
    length=len(dish)-1
    #checks if the last letters are the same and the first letters are the same
    #if so it returns true
    #if not it will return false 
    if (dish[length]==beast[length1] and dish[0]==beast[0]):
        return True
    else:
        return False
    
