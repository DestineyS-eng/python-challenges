def fake_bin(x):
    #allows me to use comparative operations 
    num= [int(i) for i in str(x)]
    #will hold the new numbers as a string
    string=""
    for i in range (len(num)):
        #if greater than or equal to 5 add 1 to string 
        if num[i]>=5:
            string+="1"
        #if string is less than or equal to 5 add 0 to string 
        elif num[i]<=5:
            string+="0"
    
    return string
            
