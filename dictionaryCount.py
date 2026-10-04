lst2=['a','a','a','b','b','c','a','a','d']
def run_length_encode(lst):
    newlist=[]
    dic={}
    for letter in lst:
        if not letter in dic:
            dic={letter,str(lst.count(letter))}
            newlist.append(dic)
    if newlist[0]==newlist[len(newlist)]:
        newlist.remove
    return newlist
x=run_length_encode(lst2)
print(x)
