#removing duplicates
dupe=[1,3,2,3,1,4]
def removeDupes(numbers):
    dupe=[]
    for num in numbers:
        if not num in dupe:
            dupe.append(num)
        pass
    return dupe
x=removeDupes(dupe)
print(x)
