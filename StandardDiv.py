SQUARE=0.5
values=[8,-2,5,8,9,-1,-1.2,8]
def SortingCode(values):
    for i in range(len(values)):
        #starting from the frist element end at minus i index-1
        for j in range(0,len(values)-i-1):
            #if i is less than the next element
            if values[i]<values[i+1]:
                #i will equal be the next element and the next element will be i
                values[i], values[i+1] = values[i+1],values[i]
    return values
        
def StandardDiv(values):
    distance=[]
    total=0
    for num in values:
        total=(num*num)
    total=total**SQUARE
    temp=0
    for nums in values:
        if total>=nums:
            temp=total-nums
            distance.append(f"{nums} is {temp} away from {total}")
        else:
            temp=nums-total
            distance.append(f"{nums} is {temp} away from {total}")
    return ", ".join(distance)

try:
    for num in values:
        int(num)
except ValueError:
    values="a"
if values=="a":
    print("error letter found")
else:
    x=SortingCode(values)
    x=StandardDiv(x)
    print(x)
