def which_hand(string):
    #list of keys that can be typed by the left or right had in qwerty
    left=["q","w","e","r","t","a","s","d","f","g","z","x","c","v","b"]
    right=["y","u","i","o","p","h","j","k","l","n","m"]
    #lowers any uppercases so that it can be counted
    string=string.lower()
    #the amount of each key on the left or right side will be held here
    left_value=0
    right_value=0
    #goes through each letter if its in one of the lists they add 1 to the value
    for letter in string:
        for i in range (len(left)):
            if letter == left[i]:
                left_value+=1
        for x in range (len(right)):
            if letter == right[x]:
                right_value+=1
    #gives what should be returned depending on the spread of values
    if left_value>0 and right_value==0:
        return "LEFT"
    elif right_value>0 and left_value==0:
        return "RIGHT"
    elif left_value>0 and right_value>0:
        return "BOTH"
    elif left_value==0 and right_value==0:
        return "NONE"

x=which_hand("HELLO hello")
print(x)
