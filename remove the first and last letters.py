def remove_char(s):
    #holds the new string
    new=""
    #for loop that excludes the frist and last element 
    for i in range (1,len(s)-1):
        #adds the letters in its current postion to new
        new+=s[i]
    return new
