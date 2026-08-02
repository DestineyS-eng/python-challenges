def camel_case(s):
    #will hold the new word
    new=[]
    #if theres nothing in s it will return nothing 
    if not s:
        return ""
    #if the first letter of s doesnt equal space add the capilitzed version to the new array 
    elif s[0]!="":
        new.append(s[0].upper())
    #moving through the letters of s-excluding the frist element          
    for i in range (1,len(s)):
        #if the element in s is a letter it moves to the next if stament 
        if s[i].isalpha():
            #if the element before is a space then we will add the capilized version to the new array 
            if s[i-1]==" ":
                new.append(s[i].upper())
            #anything else we just append as it is 
            else:
                new.append(s[i])
    #this takes new out of array format into a string with no commas betweeen
    new="".join(new)
    #this removes any remaining spaces 
    new=new.replace(" ","")
    return new
