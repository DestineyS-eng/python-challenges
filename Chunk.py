lst=[1,2,3,4,5,6,7,8]
def chunk(lst,size):
    full=[]
    for i in range (0,len(lst),size):
        #lst=str(lst)
        try:
            numbers=lst[i:i+size]
        except IndexError:
            numbers=lst[-(len(list)%size):]
        full.append(numbers)
    return full
x=chunk(lst,5)
print(x)
