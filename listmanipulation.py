numberList=[3,6,1,2,7,8,2,9,10]
print((numberList))
#backwards function
def backwards(s):
    back=[]
    for i in range (len(s),0,-1):
        back.append(str(s[i-1]))
    return ", ".join(back)
x=backwards(numberList)
print(x)
#finds summ of numbers
def Sum(s):
    total=0
    for num in s:
        total+=num
    return total
x=Sum(numberList)
print(x)
#prints only numbers that are even 
def EvenOnly(s):
    Even=[]
    for num in s:
        if num%2==0:
            Even.append(str(num))
    return ", ".join(Even)
x=EvenOnly(numberList)
print(x)
#print only numbers that are factors of a given number
def factors(numbers,user):
    factors=[]
    for num in numbers:
        if user%num==0:
            factors.append(str(num))
    return ", ".join(factors)
user=int(input("enter a number"))
x=factors(numberList,user)
print(x)
#print squared list
def squared(s):
    squared=[]
    for num in s:
        squared.append(str(num*num))
    return ", ".join(squared)
x=squared(numberList)
print(x)
#backwards
print(numberList[::-1])
