def count(s):
    #holds the letter and its count
    new={}
    #if its empty return {}
    if s=="":
        return {}
    #looks through each letter in s
    for letter in s:#
        #if letter is alredy in new we dont add it again 
        if letter in new:
            pass
        #if not we update new with the letter ans its count in s
        else:
             new.update({letter:s.count(letter)})
            
    return new
        
