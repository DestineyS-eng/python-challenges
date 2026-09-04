#calculate a discounted price for the user
DISCOUNT=0.9

item_price=19.99
quanity=3
is_discounted=True

if is_discounted:
    total=item_price*DISCOUNT*quanity
    print(f"your total of {quanity} items is £{total:.2f}")
elif not is_discount:
    print(f"your total of {quanity} items is £{item_price*quanity:.2f}")
