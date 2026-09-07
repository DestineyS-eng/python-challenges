MAX_CAPACITY=100
LOW_STOCK_THRESHOLD=20
#input validation checks
item_name=input("enter item name")
try:
  og_price=float(input("enter current price"))
  current_stock=int(input("enter current stock count"))
except ValueError:
  og_price=-1
  current_stock=-1
#gives error if it fits the conditions of being less than 0 or not being a letter or being equal too or less than 10
if og_price<=0 or current_stock<0 or (not item_name.replace(" ","").isalpha()):
  print("error")
  #gives outputs according to critrea 
else:
  if current_stock>LOW_STOCK_THRESHOLD:
    print(f"{item_name} levels are fine")
  elif current_stock>=6 and current_stock<=LOW_STOCK_THRESHOLD:
    percent=(100//MAX_CAPACITY)*current_stock
    print(f"warning {item_name} low at {percent}% relative to {MAX_CAPACITY} maxiumum")
  elif current_stock>=0 and current_stock<=5:
    new_price=og_price*0.60
    print(f"new clearance price for {item_name} is £{new_price:.2f}")

