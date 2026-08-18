def duplicate_encode(word):
    #holds the bracket form
    new=""
    #lowers capitalizes so it ingnores diffrent case 
    word=word.lower()
    #goes through each element in a string 
    for i in range (len(word)):
        #if the count of the letter/symbol/space is equal to 1
        #we will then and the non-duplicate bracket 
        #if not we add the duplicate bracket
        if word.count(word[i])==1:
            new+="("
            
        else:
            new+=")"
    return new
