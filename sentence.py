def smash(words):
    #will hold the new sentence
    sentence=""
    #goes through each word in the array words
    for i in range (len(words)):
        #stores the last position value of the array 
        length=len(words)-1
        #if it doesn't equal the last value of the array add the word with a space after
        if not words[i]==words[length]:
            sentence+=words[i]+" "
        #if it does equal the last value just add the word
        elif words[i]==words[length]:
            sentence+= words[i]
    return sentence
