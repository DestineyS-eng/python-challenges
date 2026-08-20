def alphabet_position(text):
    #holds the numeric places of letters 
    new=""
    #so letters can be identified as alpha is lowercase 
    text=text.lower()
    #so I can compare letters too see if I should add the value to new  
    alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    #looks at the indiviual words in a sentence 
    for word in text:
        #looks at the letters within the words
        for i in range (len(word)):
            #looks at the letters in alpha 
            for x in range (len(alpha)):
                #if the word in the sentence is a letter and equal to one of the letters in the alphabet
                #then we and the position of the letter as a string and a space
                if word[i]==alpha[x] and word[i].isalpha():
                    new+=str(x+1)+" "
    #returns without the extra space at the end                
    return new[0:len(new)-1]
            
