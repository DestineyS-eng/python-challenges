values=[7,9,6,4,5,-1,2]
def SortingCode(values):
    for i in range(len(values)):
        #starting from the frist element end at minus i index-1
        for j in range(0,len(values)-i-1):
            #if i is less than the next element
            if values[i]<values[i+1]:
                #i will equal be the next element and the next element will be i
                values[i], values[i+1] = values[i+1],values[i]
    return values
        
def medianValue(values):
    length=len(values)
    median=length//2
    if length%2==0:
        median=(values[median]+values[median-1])/2
        return median
    else:
        median=(length//2)
        return values[median] 
try:
    for num in values:
        int(num)
except ValueError:
    values="a"
if values=="a":
    print("error letter found")
else:
    x=SortingCode(values)
    x=medianValue(x)
    print(x)
