def friend(x):
    #holds the confirmed friends
    friends=[]
    #looks at each element in the array x
    for char in x:
        #if the length of char is 4 then it will be added to the array friends 
        if len(char)==4:
            friends.append(char)
        #if not it will just ignore it
        else:
            pass
    return friends
