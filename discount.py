#constants
SALE_DISCOUNT=0.20
REQMET_DISCOUNT=0.10

sale_active=True
#calculate discount
def calDiscount(price,value):
    if sale_active and value>65:
        discount=SALE_DISCOUNT+REQMET_DISCOUNT
        percent=discount*100
        finalprice=((100-percent)/100)*price
        return (f"you are eligblie for a {percent:.0f}% discount! your total price is {finalprice:.2f}")
    elif sale_active:
        discount=SALE_DISCOUNT
        percent=discount*100
        finalprice=((100-percent)/100)*price
        return (f"you are eligblie for a {percent:.0f}% discount! your total price is {finalprice:.2f}")
    elif value>65:
        discount=REQMET_DISCOUNT
        percent=discount*100
        finalprice=((100-percent)/100)*price
        return (f"you are eligblie for a {percent:.0f}% discount! your total price is {finalprice:.2f}")
    else:
        return (f"you are not eligblie for any discounts your total price is {finalprice:.2f}")

#Inputs
try:
    price=float(input("what is the price of your item"))
    value=int(input("input age"))
except ValueError:
    price=-1
    value=-1
if value>=0 and price>0:
    x=calDiscount(price,value)
    print(x)
else:
    print("error invalid value")
