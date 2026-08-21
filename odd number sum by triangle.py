def row_sum_odd_numbers(n):
    #starting value to increase
    total=2
    #the frist number on the triangle
    num=1
    #if n is equal to 1 just return 1 as theres no others to add too it
    if n==1:
        return 1
    #for the range of n
    #we will add total too num 
    #then add 2 to total by doing this we get the frist number of the tower row each time 
    for i in range (1,n):
        num+=total
        total=total+2
    #assign the first number of the row to row
    row=num
    #for range 1 to n it will add 2 to num to get the next odd number 
    #then adds that number to row to get the total
    for x in range (1,n):
        num+=2
        row+=num
    return row
    
