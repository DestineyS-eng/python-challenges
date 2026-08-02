def letters_to_numbers(s):
    #will hold the total value of the sentence 
    total=0
    #will pass through the whole alphabet so i can compare 
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    # passes through each character in s 
    for char in s:
        #if char is a digit it will had its interger form to total
        if char.isdigit():
            total+=int(char)
        #this will go through each letter in the alphabet 
        for x in range (len(alphabet)):
            #if char is equal to the letter the current position value will be added by one and added to total 
            if char==alphabet[x]:
                n=x+1
                total+=n
            #if the char is equal to an uppercase version of the letter it will incrrease the position value by 1 and then double it-adding it to total
            elif char==alphabet[x].upper():
                n=x+1
                total+=(n+n)
    return total
        
        
