def get_middle(s):
    #calculates the middle value
    length=len(s)//2
    #if its even return the letter before as well
    if len(s)%2==0:
        return s[length-1]+s[length]
    #else return the middle element 
    return s[length]
