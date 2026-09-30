#contants
MAX_DATE=31
MIN_DATE=28
PIN=8946
FUNDS=1000
PIN_LENGTH=4
CARD_LENGTH=16
CHANCES=3

#strip spaces
def strip_spaces(s):
    s==str(s).strip()
    return s
#check valid pin 
def validPin(s):
    if s!=PIN and len(str(s))!=PIN_LENGTH:
        return False
    return True
#check valid card card numbers 
def validCardNum(s):
    for num in str(s):
        if num.isalpha():
            return False
        elif len(str(s))!=CARD_LENGTH:
            return False
    return True

#check valid date
def validDate(s):
    s=s.replace("/","")
    try:
        s1=int(s[:1])
        s2=int(s[2:])
    except ValueError:
        s=0
    if 0<int(s[1]) and 0<=int(s[0]) and MIN_DATE<=s2<=MAX_DATE and len(s)==4:
        return True
    elif 10<=s1<=12 and MIN_DATE<=s2<=MAX_DATE and len(s)==4:
        return True
    else:
        return False
attempts=0
while attempts!=CHANCES:
    print("Welcome to Llyods Bank insert your card")
    try:
        card=int(input("enter card number: "))
    except ValueError:
        card=0
    date=input("enter expiry date in the format MM/YY: ")
    card=strip_spaces(card)
    date=strip_spaces(date)
    if not validCardNum(card) or not validDate(date):
        print("error invalid card used")
        attempts+=1
    else:
        try:
            amount=int(input("Enter an amount to withdraw: "))
            pin=int(input("Enter PIN: "))
        except ValueError:
            amount=-1
            pin=0
        if amount>FUNDS or amount<=0:
            print("insufficent funds")
            attempts+=1
        elif PIN!=pin:
            print("error:wrong pin")
            attempts+=1
        elif 0<=amount<=FUNDS or validPin(pin):
            FUNDS-=amount
            print(f"you have succesfully withdrawn {amount:.2f} your current balance is {FUNDS:.2f}")
            print("\nReceipt")
            print(f"WITHDRAWN:{amount:.2f}")
            exit("Goodbye!")

print("exiting program: too many attempts made")
