def century(year):
#will always give the century base number 
    cent=year//100
    numbers=[int(i) for i in str(year)]
# so i can put the intergers as themself in a list 
    if (len(numbers))==4:
#if the year is  4 of length then minus 2
        total=(len(numbers))-2
    elif (len(numbers))==1:
#if the year is 1 length then minus 1
        total=(len(numbers))-1
    else:
        total=(len(numbers))-2
    for i in range (total,len(numbers)):
#it will start at the point without century number and end at the normal length ive done this so i can compare the years indiviually
        if numbers[i]>0:
#if i in numbers is greater than its the next cenutry and it will return it 
            cent+=1
            return cent
    return cent 
