try:
    loyalty_points=int(input("enter the customers current amount of loyalty point"))
    total_cost=float(input("enter the customers total cost"))
except ValueError:
    loyalty_points="string"
    total_cost="string"
if type(loyalty_points)==int and type(total_cost)==float and loyalty_points>=0 and total_cost>=0.0:
    loyalty_points+=total_cost*10
    if loyalty_points>=100:
        question=input("Target reached! This customer qualifies for a FREE coffee.Deduct 100 points? Y OR N")
        if type(question)==str and question=="Y":
            loyalty_points-=100
            print(loyalty_points)
        elif type(question)==str and question=="N" :
            print("points kept the same at ",loyalty_points)
        else:
            print("error")
    else:
        print("customer has ",loyalty_points," points.They need ",100-loyalty_points," more points for a free coffee")
else:
    print("error")
