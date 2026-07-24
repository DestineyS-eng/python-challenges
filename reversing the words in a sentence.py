def reverse_words(text):
    words=text.split(" ") #seperates each word 
    for i in range (len(words)):
        if words[i]!=" ": 
            words[i]=words[i][::-1] #replaces the orginal word with the reversed one 
            reverse=" ".join(words) #turns it into a string 
    return reverse
