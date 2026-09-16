#VAT is currently a 20% increase on what is bought
VAT=1.20
#this function will calcluate the toltal price
def calculate_total(price,discount):
  discount_decimal=(100-discount)/100
  total=price*discount_decimal
  return total*VAT
#validates and stores price and discount 
try:
  price=float(input("enter the price"))
  discount=int(input("enter the % discount"))
except ValueError:
#if it isnt the correct data type it will turn them into a invalid value which will be rejected 
  price=-1.00
  discount=-1
if price<0.00 or 0>discount or discount>100:
  print("error:invalid values entered")
#if not the function will be called and it will print the returned price in a statement too 2 decimal places 
else:
  total=calculate_total(price,discount)
  print(f"your total is £{total:.2f}")
  
