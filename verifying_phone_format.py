def valid_phone_number(phone_number):
    #splits the number into a list of 2
    phone=phone_number.split()
    #if the length of the list has 2 elements 
    if len(phone)==2:
        #if anywhere out side mandatory punctuation is a interger
        if phone[0][1:4].isdigit() and phone[1][0:3].isdigit() and phone[1][4:].isdigit():
            #if the length of the frist element is 5  and brackets in the correct position 
            if len(phone[0])==5 and phone_number[0]=="(" and phone_number[4]==")":
                #if there is a space in this area only 
                if phone_number[5]==" ":
                    #if the length if the second element is 8 and the hypen is in position 9
                    if len(phone[1])==8 and phone_number[9]=="-":
                        #once all these conditions are true return true
                        return True
                    
    #if any arent true false will be returned       
    return False
