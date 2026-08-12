def square_digits(num):
    #holds the answers from the solved equation 
    fin=""
    #seperates the numbers so we can look at each one indivially
    num=[int(i) for i in str(num)]
    for x in range (len(num)):
        #this will check if the element is a integer 
        if type(num[x])== int:
            #then it will square the number and add the string version of it to fin 
            nums=num[x]**2
            fin+= str(nums)
    #after it will return the integer version of fin 
    return int(fin)
    


             
