#move list:
listMove=[1,2,3,4,5]
def move(listMove,k):
    return listMove[k+1:]+listMove[:-k]
x=move(listMove,2)
print(x)
