total_shoes_processed=0
total_revenue_accrued=0.00
running=True
#while running is true the menu will load and if 1 or 2 is selected the calulations will run
#other wise 3 will mean the program will end as running is now false
while running==True:
    print("       MENU      ")
    print("1.Process New Shoe Batch Delivery")
    print("2.Veiw Warehouse Session Statistics")
    print("3.Terminate Application Session")
    option=input("select an option 1-3")
    if option=="3":
        running=False
        print("Session Safely Terminated.Goodbye.")
    elif option=="1":
        #try will try these inputs but if there is a value error the will both become 0 and will be rejected by the next if statments conditions
        #which doesnt allow 0 to be used for either value
        try:
            shoes_amount=int(input("enter the amount of pairs of shoes in a batch"))
            total_distance=float(input("enter the distance travelled"))
        except ValueError:
            shoes_amount=0
            total_distance=0
        if shoes_amount>0 and total_distance>0.00:
            #updates the inital varibles at the begining with the corresponding varibles in option 1 and prints a receipt depending on miles done
            total_shoes_processed+=shoes_amount
            if total_distance>150.00:
                cost=(shoes_amount*1.50)+45
                print("   RECEIPT  ")
                print("Base price: £",cost)
            elif total_distance<=150.00:
                cost=(shoes_amount*1.50)
                print("          RECEIPT        ")
                print("Base price: £",cost)
            total_revenue_accrued+=cost
            #overall summury of product and cost.revenue is forced into 2 decimal places via .2f
    elif option=="2":
        print("        SUMMURAY INTERFACE")
        print(f"total shoes processed:{total_shoes_processed}")
        print(f"total revenue accured: £{total_revenue_accrued:.2f}")
