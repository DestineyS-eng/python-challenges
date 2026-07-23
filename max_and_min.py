def minimum(arr):
#takes the element of the list
    min=arr[0]
    for i in range (1,len(arr)):
        #if its less than min than it replaces it
        if arr[i]<min:
            min=arr[i]
    return min

def maximum(arr):
    #also takes the frist element of the list
    max=arr[0]
    for x in range (1,len(arr)):
        #if its greater than max it replaces it 
        if arr[x]>max:
            max=arr[x]
    return max
