def likes(names):
    mylist=list(names)
    length=len(mylist)
    output=""
    if length==1:
        output=f"{mylist[length-1]} likes this"  #shows only one person liked your post
    elif length==2:
        output=f"{mylist[0]} and {mylist[1]} like this" #shows 2 peple liked 
    elif length==3:
        output=f"{mylist[0]}, {mylist[1]} and {mylist[2]} like this" #shows 3 people liked 
    elif length>=4:
        output=f"{mylist[0]}, {mylist[1]} and {len(mylist[2:])} others like this" #if 4 or more like the frist 2 will show and then the number of the rest 
    else:
        output="no one likes this"
    return output
