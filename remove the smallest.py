def remove_smallest(numbers):
    #if its empty return brackets
    if numbers==[]:
        return []
    #holds the new list excluding the most boring place
    new=[]
    #sorted the list and took the frist element to get the smallest number 
    num=sorted(numbers)
    num=num[0]
    #in this for loop it will first check if the current elsement is greater than num
    #if so ir will append it into new list
    for i in range (len(numbers)):
        if numbers[i]>num:
            new.append(numbers[i])
        #if not it will then check if the element is equal to num
        #if there is num before this element
        #if the overall count of num is greater than 1
        elif numbers[i]==num and numbers[:i] and numbers.count(num)>1:
            new.append(numbers[i])
        else:
            pass
        #this will result in the frist smallest number being excluded leaving the rest
    return new
                
        
