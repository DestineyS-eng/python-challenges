def to_weird_case(words):
    #holds the new string
    letters=""
    #works as an index as char doesn't allow me to use index 
    index=0
    #will go through every character 
    for char in words:
        #if theres a space it will add it to letter but won't increase the index
        if char==" ":
            letters+=" "
            index=0
        else:
            #if the MOD if the index by 2 equals 0 then uppercase it
            #if the char doesnt its lower this index increses on either one by 1
            if index % 2==0:
                letters+=char.upper()
            else:
                letters+=char.lower()
            index+=1
    return letters
        
