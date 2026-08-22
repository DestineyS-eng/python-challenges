def str_count(stri, letter):
    #looks at the letters in the word
    for word in stri:
        #if ketter is equal to word we will return the count of letter in the word
        if word==letter:
            return stri.count(letter)
    #if not true it will return 0
    return 0
   
