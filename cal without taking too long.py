def power_mod(x, y, n):
    #starts at 1 so we can keep x the same inatially when updating total 
    total=1
    #while y is grater than 0 as y shows us if the equation is done
    while y>0:
        #if there is no remainder when mod by 2 then x is powered by its self and mod by n-update y by dividing by 2
        if y%2==0:
            x=(x*x)%n
            y=y//2
        #if the remainder isnt 0 then total becomes x and then is mod by n-y is reduced by one so that it can now be even 
        elif y%2!=0:
            total=(total*x)%n
            y=y-1
    return total
        
