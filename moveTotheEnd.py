#moves item selected to the end
listMixed=[0,0,1,0,3,1,0,2,0,"a"]
def item(s,number):
    store=0
    for num in s:
        if num==number:
            store+=1
            s.remove(num)
    for i in range(0,store):
        s.append(number)
    return s
x=item(listMixed,0)
print(x)
