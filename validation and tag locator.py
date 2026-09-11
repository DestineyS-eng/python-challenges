#this returns true if the final 3 letters are valid
def ValidEnd(s):
    for char in s:
        if char in INVALID_LETTERS or char.isdigit():
            return False
    return True

def ValidLength(s):
    if len(s)!=7:
        return False
    return True

def ValidStartLetters(s):
    letters=""
    for char in s:
        if not char in INVALID_LETTERS:
            letters+=char
    letters=letters[:2]
    if letters.isalpha() and not letters[0] in INVALID_SECOND_LETTERS:
        return True
    else: 
        return False

def ValidMIddleNUmbers(s):
    num=""
    for char in s:
        if char.isdigit():
            num+=char
    try:
        int(num)
    except ValueError:
        num=1
    if (2<=int(num)<=26) or (51<=int(num)<=76):
        return True
    else:
        return False



user_licence_plate=strip_spaces("BA12DCC").upper()

final_char=user_licence_plate[-3:] 

if not ValidLength(user_licence_plate):
    print('error: this length does not equal 7')
    exit()
elif not ValidStartLetters(user_licence_plate):
    print('error: the starting letters are not valid (QIZJUSTX and digits)')
    exit()
elif not ValidMIddleNUmbers(user_licence_plate):
    print('error: these digits are not in valid ranges (2-26) and (51-76)')
    exit()
elif not ValidEnd(final_char):
    print('error: that is not a valid end')
    exit()
else:
    print("this is a valid licence plate")
   

tag=user_licence_plate[:2]

#items allow me to assgin city, region and tags as seperate variables and to go through each
for cities,(region,tags) in GROUPED_MAP.items():
    #if the tag in in the grouped tag we will print the city and region and then break the loop so else isnt printed
    if tag in tags:
        print(f"region in: {region} registed in: {cities}")
    

    
