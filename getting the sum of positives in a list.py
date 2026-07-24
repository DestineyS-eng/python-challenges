def positive_sum(arr):
    total=0 # will hold the sum
    for i in range (len(arr)): #goes through each value 
        if arr[i]>0: #if its gretere than 0 so that theres no negatives or 0
            total=total+arr[i]
        
    return total

    
x=positive_sum([-1,2,3,4,-5])
print(x)
   
