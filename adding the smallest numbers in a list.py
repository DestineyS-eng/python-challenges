def sum_two_smallest_numbers(numbers):
    if len(numbers)>=4:   #checking in the lenth is equal or above 4
        sort=sorted(numbers)   #order the list so i can always assume the 2 smallest values are at the top
        total=int(sort[0])+int(sort[1])   #total of the 2 smallest values
        return total
    return 0     # if its under the length of 4
        
x=sum_two_smallest_numbers("9234")
print(x)
