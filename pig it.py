def pig_it(text):
    my_list=text.split()   #split words up 
    for i in range (len(my_list)):
        if my_list[i][0:].isalpha() :     #if the whats in my list is a letter then
            my_list[i]= my_list[i][1:] + my_list[i][0] + "ay"   #the rest of the word plus the beginning plus ay
    result=" ".join(my_list)   #join the list together with punctuation 
        
    return result
    
x=pig_it("hello ! world ? ") #don't know how to do this if the grammar is directly next to the letter "hello?"
print(x)
        
