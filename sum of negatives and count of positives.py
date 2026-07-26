def count_positives_sum_negatives(arr):
    #output if there is nthing in arr
    n=[]
    output=[]
    # values that will be added to output 
    total=0
    count=0
    for i in range (len(arr)):
        #if element less than zero add it to total 
        if arr[i]<0:
            total+=arr[i]
    for x in range (len(arr)):
        #if element greater than 0 count increases by one 
        if arr[x]> 0:
            count+=1
    #addding the values to ouput
    output.append(count) 
    output.append(total)
    #if its empty return n else give output 
    if arr==[]:
        return n
    else:
        return output 
            
