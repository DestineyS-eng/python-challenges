import random
#DVLA programme to check and generate licence plate

#define my CONSTANTS
SEPFEB_ADD_ON = 50
REQ_CHARS = 7
INVALID_LETTERS = 'QIZ'
INVALID_SECOND_LETTERS='JUTX'
INVALID_LAST_LETTERS='QI'
VALID_LAST_3_LETTERS=["A","B","C","D","E","F","G","H","K","L","M","N","O","P","R","S","V","W","Y","J","U","S","T","X","Z"]
VALID_SECOND_LETTERS=["A","B","C","D","E","F","G","H","K","L","M","N","O","P","R","S","V","W","Y","J","U","S","T","X"]
VALID_LETTERS=["A","B","C","D","E","F","G","H","K","L","M","N","O","P","R","S","V","W","Y"]


#listed all the offices and their tags
GROUPED_MAP= {
    # ANGLIA
    "Peterborough": ("Anglia", ["AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AJ", "AK", "AL", "AM", "AN"]),
    "Norwich": ("Anglia", ["AO", "AP", "AR", "AS", "AT", "AU"]),
    "Ipswich": ("Anglia", ["AV", "AW", "AX", "AY"]),
    
    # BIRMINGHAM
    "Birmingham":("Birmingham",["BA", "BB", "BC", "BD", "BE", "BF", "BG", "BH", "BJ", "BK", "BL", "BM", "BN", "BO", "BP", "BR", "BS", "BT", "BU", "BV", "BW", "BX", "BY"]),
    
    # CYMRU (WALES)
    "Cardiff": ("Cymru/Wales", ["CA", "CB", "CC", "CD", "CE", "CF", "CG", "CH", "CJ", "CK", "CL"]),
    "Swansea": ("Cymru/Wales", ["CM", "CN", "CO"]),
    "Bangor": ("Cymru/Wales", ["CP", "CR", "CS", "CT", "CU", "CV"]),
    
    # DEESIDE TO SHREWSBURY
    "Chester": ("Deeside / Shrewsbury", ["DA", "DB", "DC", "DD", "DE", "DF", "DG", "DH", "DJ"]),
    "Shrewsbury": ("Deeside / Shrewsbury", ["DK", "DL", "DM", "DN", "DO", "DP", "DR", "DS", "DT", "DU", "DV", "DW", "DX", "DY"]),
    
    # ESSEX
    "Chelmsford": ("Essex", ["EA", "EB", "EC", "ED", "EE", "EF", "EG", "EH", "EJ", "EK", "EL", "EM", "EN", "EO", "EP", "ER", "ES", "ET", "EU", "EV", "EW", "EX", "EY"]),
    
    # FOREST AND FENS
    "Nottingham": ("Forest and Fens", ["FA", "FB", "FC", "FD", "FE", "FF", "FG", "FH", "FJ", "FK", "FL", "FM", "FN", "FP"]),
    "Lincoln": ("Forest and Fens", ["FR", "FS", "FT", "FV", "FW", "FX", "FY"]),
    
    # GARDEN OF ENGLAND
    "Maidstone": ("Garden of England", ["GA", "GB", "GC", "GD", "GE", "GF", "GG", "GH", "GJ", "GK", "GL", "GM", "GN"]),
    "Brighton": ("Garden of England", ["GO", "GP", "GR", "GS", "GT", "GU", "GV", "GW", "GX", "GY"]),
    
    # HAMPSHIRE AND DORSET
    "Bournemouth": ("Hampshire and Dorset", ["HA", "HB", "HC", "HD", "HE", "HF", "HG", "HH", "HJ"]),
    "Portsmouth": ("Hampshire and Dorset", ["HK", "HL", "HM", "HN", "HO", "HP", "HR", "HS", "HT", "HU", "HV", "HW", "HX", "HY"]),
    
    # LUTON AND NORTHAMPTON
    "Luton": ("Luton / Northampton", ["KA", "KB", "KC", "KD", "KE", "KF", "KG", "KH", "KJ", "KK", "KL"]),
    "Northampton": ("Luton / Northampton", ["KM", "KN", "KO", "KP", "KR", "KS", "KT", "KU", "KV", "KW", "KX", "KY"]),
    
    # LONDON
    "Wimbledon": ("London", ["LA", "LB", "LC", "LD", "LE", "LF", "LG", "LH", "LJ"]),
    "Stanmore": ("London", ["LK", "LL", "LM", "LN", "LO", "LP", "LR", "LS", "LT"]),
    "Sidcup": ("London", ["LU", "LV", "LW", "LX", "LY"]),
    
    # MANCHESTER AND MERSEYSIDE
    "Manchester":("Manchester",["MA", "MB", "MC", "MD", "ME", "MF", "MG", "MH", "MJ", "MK", "ML", "MM", "MN", "MP", "MT", "MU", "MV", "MW", "MX", "MY","MS"]),
    
    # NORTH
    "Newcastle": ("North", ["NA", "NB", "NC", "ND", "NE", "NF", "NG", "NH", "NJ", "NK", "NL", "NM", "NN", "NO"]),
    "Stockton": ("North", ["NP", "NR", "NS", "NT", "NU", "NV", "NW", "NX", "NY"]),
    
    # OXFORD
    "Oxford": ("Oxford", ["OA", "OB", "OC", "OD", "OE", "OF", "OG", "OH", "OJ", "OK", "OL", "OM", "ON", "OO", "OP", "OR", "OS", "OT", "OU", "OV", "OW", "OX", "OY"]),
    
    # PRESTON
    "Preston": ("Preston / Carlisle", ["PA", "PB", "PC", "PD", "PE", "PF", "PG", "PH", "PJ", "PK", "PL", "PM", "PN", "PO", "PP", "PR", "PS", "PT", "PU", "PV", "PW", "PX", "PY"]),
    
    # READING
    "Reading": ("Reading", ["RA", "RB", "RC", "RD", "RE", "RF", "RG", "RH", "RJ", "RK", "RL", "RM", "RN", "RO", "RP", "RR", "RS", "RT", "RU", "RV", "RW", "RX", "RY"]),
    
    # SCOTLAND
    "Glasgow": ("Scotland", ["SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SJ"]),
    "Edinburgh": ("Scotland", ["SK", "SL", "SM", "SN", "SO"]),
    "Dundee": ("Scotland", ["SP", "SR", "SS", "ST"]),
    "Aberdeen": ("Scotland", ["SU", "SV", "SW", "SX"]),
    "Inverness": ("Scotland", ["SY"]),
    
    # SEVERN VALLEY
    "Worcester": ("Severn Valley", ["VA", "VB", "VC", "VD", "VE", "VF", "VG", "VH", "VJ", "VK", "VL", "VM", "VN", "VO", "VP", "VR", "VS", "VT", "VU", "VV", "VW", "VX", "VY"]),
    
    # WEST OF ENGLAND
    "Exeter": ("West of England", ["WA", "WB", "WC", "WD", "WE", "WF", "WG", "WH"]),
    "Truro": ("West of England", ["WJ", "WK", "WL"]),
    "Bristol": ("West of England", ["WM", "WN", "WO", "WP", "WR", "WS", "WT", "WU", "WV", "WW", "WX", "WY"]),
    
    # YORKSHIRE
    "Leeds": ("Yorkshire", ["YA", "YB", "YC", "YD", "YE", "YF", "YG", "YH", "YJ", "YK", "YL"]),
    "Sheffield": ("Yorkshire", ["YM", "YN", "YO", "YP", "YR", "YS", "YT", "YU", "YV"]),
    "Beverley": ("Yorkshire", ["YW", "YX", "YY"])
}

#this function takes a string and strips out the spaces
def strip_spaces(s):
    s=s.replace(" ","")
    return s

#this returns true if the final 3 letters are valid
def ValidEnd(s):
    for char in s:
        if char in INVALID_LAST_LETTERS or char.isdigit():
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

ChooseOption=""
while ChooseOption!="0":
    print("0.Exit program|1.Check for valid licence plate|2.Find age of the car|3.Find the city registered in|4.Generate example licence plate")
    ChooseOption=input("pick one option 0-4")

    if not ChooseOption in "1234":
            print("Error not a valid number")

    elif ChooseOption=="4":
        #generates an example licence plate 
        randomNum=random.choice([random.randint(2,26),random.randint(51,76)])
        randomfristLetter=random.choice(VALID_LETTERS)
        randomSecondLetter=random.choice(VALID_SECOND_LETTERS)
    
        randomlast3=random.sample(VALID_LAST_3_LETTERS,3)
        randomlast3="".join(randomlast3)
        
        if randomNum<10:
            GenlicencePlate=randomfristLetter+randomSecondLetter+"0"+str(randomNum)+randomlast3
            print(f"an example licence plate would be {GenlicencePlate}")
            
        else:
            GenlicencePlate=randomfristLetter+randomSecondLetter+str(randomNum)+randomlast3
            print(f"an example licence plate would be {GenlicencePlate}")
            
    elif ChooseOption=="1":
        user_licence_plate=input("enter valid licence plate")
        user_licence_plate=strip_spaces(user_licence_plate).upper()
        #checks for a valid licence plate 
        final_char=user_licence_plate[-3:] 
        
        if not ValidLength(user_licence_plate):
            print('error: this length does not equal 7')#
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
            exit()
            

    elif ChooseOption=="2":
        user_licence_plate=input("enter valid licence plate")
        user_licence_plate=strip_spaces(user_licence_plate).upper()
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
        
        
        numbers=int(user_licence_plate[2:4])
        
        #gives the year and approx months
        if numbers<10:
            print(f"this was registered in march-august of 200{numbers}")
        elif 10<=numbers<=26:
            print(f"this was registered in march-august of 20{numbers}")
        elif 51<=numbers<60:
            numbers-=SEPFEB_ADD_ON
            print(f"this was registered in febuary-september of 200{numbers}")
        elif 60<=numbers<=76:
            numbers-=SEPFEB_ADD_ON
            print(f"this was registered in febuary-september of 20{numbers}")

    elif ChooseOption=="3":
        user_licence_plate=input("enter valid licence plate")
        user_licence_plate=strip_spaces(user_licence_plate).upper()
        #checks for a valid licence plate 
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
         
        #items allow me to assgin city, region and tags as seperate variables and to go through each
        tag=user_licence_plate[:2]
        
        for cities,(region,tags) in GROUPED_MAP.items():
            #if the tag in in the grouped tag we will print the city and region and then break the loop so else isnt printed
            if tag in tags:
                print(f"region in: {region} registed in: {cities}")
                break
    
print("quitting program")
