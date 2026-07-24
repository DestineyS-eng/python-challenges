def same_structure_as(original,other):
    #checks if they both arent a list/array so that it can return false
    if isinstance(original,list)!=isinstance(other,list):
        return False
    # reverses the statment to check if they are both a list/array so it can pass
    elif isinstance(original,list) and isinstance(other,list):
        #if the length doesnt equal the same return false
        if len(other)!=len(original):
            return False
        #this allows us to compare individual elements throught the previous code if it doesnt match return false
        for i in range (len(original)):
            if not same_structure_as(original[i],other[i]):
                return False
    return True
        
