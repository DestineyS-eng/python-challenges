def high_and_low(numbers):
    #separate the list by its spaces so the minus numbers dont get seperated
    num=numbers.split(" ")
    #max and min start from the frist value of both
    min=int(num[0])
    max=int(num[0])
    #where the string of the lowest and highest number will go
    output=""
    for i in range (1,len(num)):
        #change it into a integer to allow comparison 
        y= int(num[i])
        if min>y:
            min=y
        elif max<y:
            max=y
    #using concat to join the two integers as a string 
    output+= str(max)+" "+str(min)
    return output
