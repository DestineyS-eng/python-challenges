def dig_pow(n, p):
# a list that will keep each element a interger 
    num=[int(i) for i in str(n)]
# im having this as the starting value as its harder to do it within the loop
    total=num[0]**p
    for i in range (1,len(num)):
# each time n is powered by p+the number i is on 
        total+=num[i]**(p+i)
    new_num= total//n
    if total%n==0:
        return new_num
    else:
        return -1
            
