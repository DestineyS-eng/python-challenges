def enough(cap, on, wait):
    #show the amount of seats left 
    total=cap-on
    #while the amount of seats left does not equal 0
    #remove 1 from both wait and total
    while total!=0:
        total=total-1
        wait=wait-1
    #if wait is less than 0 return 0
    #if not return wait
    if wait<0:
        return 0
    else:
        return wait
