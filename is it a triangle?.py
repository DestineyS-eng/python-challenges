def is_triangle(a, b, c):
    group=[a,b,c]
    mylist=list(group) #ordered list so i can do pythagorus
    if len(mylist)==3 and (mylist[0]!=0 and  mylist[1]!=0 and  mylist[2]!=0): #making sure there is only 3 lengths #edited so that if 0 is given as a length it returns false
        if (mylist[2]**2)==(mylist[0]**2)+(mylist[1]**2): 
            return True #true returns if it is a triangle 
        elif (mylist[0]+mylist[1]>mylist[2]) and (mylist[0]+mylist[2]>mylist[1]) and (mylist[1]+mylist[2]>mylist[0]): # an iscosolese triangle has too meet these conditions according to length a+b>c , a+c>b and b+c>a
            return True
        elif mylist[1]==mylist[2] and mylist[1]==mylist[0]: #this is for equalateral triangles where all sides are equal
            return True
        else:
            return False # if it doesnt fit these conditions its not a triangle 
    return False # if theres not 3 lengths then return false
