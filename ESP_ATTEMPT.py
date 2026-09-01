#
plot_num=[1,2,3,4]
plot_status=["booked","booked","available","available"]
harv_yeild=[0.0,0.0,0.0,0.0]
print("Veiw all plots|book a plot|record harvest|exit program")
select="nothing"
while select!=4:
    try:
        select=int(input("select one option (1,2,3 or 4)"))
    except ValueError:
        select="string"
    if type(select)==int and (select==1 or select==2 or select==3 or select==4) :
        if select==1:
            for i in range (0,4):
                print(plot_num[i],":",plot_status[i],":",harv_yeild[i])
        elif select==2:
            enter=int(input("enter a plot number 1-4"))
            if type(enter)==int and enter==1 or enter==2 or enter==3 or enter==4:
                if plot_status[enter-1]=="available":
                    plot_status[enter-1]="booked"
                    print("success")
                else:
                    print("unavailable")
            else:
                print("error")
        elif select==3:
            enter=int(input("enter a plot number 1-4"))
            weight=float(input("enter weight"))
    else:
         print("error")
