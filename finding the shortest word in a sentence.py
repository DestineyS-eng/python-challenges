def find_short(string):
    words=string.split()
#spliting the string so i can compare the indivual lengths
    total=len(words[0])
#starting at the frist string length because no word is less than 0 in length
    for i in range (1,len(words)):
        length=len(words[i])
# finding the length of the string in the for loop before i compare 
        if total>length:
            total=length
#if total is greater than length it will replace what was in total before 
    return total
