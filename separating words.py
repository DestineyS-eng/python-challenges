def solution(s):
    #space for the new words
    word=""
    for letter in s:
        #if the letter in s is equal to its upper case version then add a space before it 
        if letter== letter.upper():
            word+=" "+letter
        else:
            #if its one word nothing changes
            word+=letter
    return word
        
