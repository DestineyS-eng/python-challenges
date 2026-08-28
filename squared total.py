def square_sum(numbers):
    #hold the total 
    total=0
    #goes through each number
    #the current number show by digi is squared and added to total
    for digi in numbers:
        total+=digi*digi
    return total
