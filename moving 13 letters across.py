def rot13(message):
    #split the alphabet in half so i can refer to its equal after 13 positions easily
    alpha1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    alpha2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    #will hold the new string
    word=""
    #will look at each indival character in message
    for char in message:
        #if its not a letter it will be added and will skip the loops for the character 
        if not char.isalpha():
            word+=char
            continue
        #if the letter in the frist alphabet list is the same as the charater from message then add the word from the same position in list 2 then it will stop looking in alpha 
        for x in range (len(alpha1)):
            if alpha1[x] == char:
                word+=alpha2[x]
                break
            #this is the same princible execpt its uppercase 
            elif alpha1[x].upper() == char:
                word+=alpha2[x].upper()
                break
        #if the letter is found in list 2 it will add its equal from list 1 and break the loop to stop screaching 
        for y in range (len(alpha2)):
            if alpha2[y]==char:
                word+=alpha1[y]
                break
            #the same code just for uppercase letters 
            elif alpha2[y].upper()==char:
                word+=alpha1[y].upper()
                break
    return word
    
    
