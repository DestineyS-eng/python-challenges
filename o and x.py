def xo(s):
    text=s.lower()   #makes the letters all lowercase
    if text.count("x")!=text.count("o"):   #if there no matching amount it will do nothing
        pass
    else:
        return True   #if there are equal amounts the output will be true
        
    return False     #if the pass happens the output will be false as they arent equal
    
p=xo("xxoo")
print(p)
