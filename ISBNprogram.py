ISBNlists=["978030640615","978186197271","978014044913","978006112008","978045152493","978074327356","978031676948","978034533968","978043902348","978054792822","978030747427","978014143951","978038549081","978006231500","978037586902","978074347710","978006085052","978054501022","978014312774","978014028333",]

def CheckdigitCal(lst):
    new=[]
    total=0
    for i in range(len(lst)):
        a=num[i]
        a=int(a)

        if (i+1)%2==0:
            total+=a*3
        elif (i+1)%2!=0:
            total+=a
           
    
    remainder=total%10
   
    checkdigit=10-remainder
    print(checkdigit)
    new.append(str(lst)+str(checkdigit))
    return "".join(new)

with open("ISBNcheckdigit.txt","w") as file:
    for num in ISBNlists:
        file.write(f"\n {CheckdigitCal(num)}")
