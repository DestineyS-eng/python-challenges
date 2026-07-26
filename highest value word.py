def high(x):
    #this will hold the largest value 
    max_score=0
    #this will hold the word with the word with the largest value 
    highest=""
    #the full alphabet so i can easily assign the value to the word
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    #spliting the sentence by the spaces 
    letters=x.split()
    for words in letters:
        #for every letter total will reset to 0
        total=0
        for y in range (len(words)):
            for i in range (len(alphabet)):
                        #if the alphabet letter is equal to the letter in the word total will increase by its value for that word  
                        if alphabet[i]==words[y]:
                            total+=(i+1)
        #if the total is greater than the max score it will replace it and the word with it will become the highest
        if total> max_score:
            highest=words
            max_score=total
                                
    return highest
                            

                            
        
