def location_indicators(s):
  #banned letters not allowed and lciense plate is striped of spaces and uppercased
  BANNED="QIZ"
  BANNED2="JUTX"
  s=s.strip().upper()
  #will hold the letters in the lciense plate
  letters=""
  #looks at each character in s
  if len(s)==7:
    for char in s:
      #if s is a letter it gets added to letters 
      if char.isalpha() and (not char in BANNED):
        letters+=char
        #if the length is exactly 5 then return the first 2
    if len(letters)==5 and (letters[0] not in BANNED2):
      return letters[:2]
#will store the tag outside the function
tag=location_indicators("Aa43Msf")
#listed all the offices and their tags
grouped_map = {
    # ANGLIA
    "Peterborough": ("Anglia", ["AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AJ", "AK", "AL", "AM", "AN"]),
    "Norwich": ("Anglia", ["AO", "AP", "AR", "AS", "AT", "AU"]),
    "Ipswich": ("Anglia", ["AV", "AW", "AX", "AY"]),
    
    # BIRMINGHAM
    "Birmingham": ("Birmingham", ["BA", "BB", "BC", "BD", "BE", "BF", "BG", "BH", "BJ", "BK", "BL", "BM", "BN", "BO", "BP", "BR", "BS", "BT", "BU", "BV", "BW", "BX", "BY"]),
    
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
    "Manchester": ("Manchester / Merseyside", ["MA", "MB", "MC", "MD", "ME", "MF", "MG", "MH", "MJ", "MK", "ML", "MM", "MN", "MP", "MT", "MU", "MV", "MW", "MX", "MY"]),
    
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
#items allow me to assgin city, region and tags as seperate variables and to go through each
for citys,(region,tags) in grouped_map.items():
  #if the tag in in the grouped tag we will print the city and region and then break the loop so else isnt printed
  if tag in tags:
    print(f"region in: {region} registed in: {citys}")
    break
else:
  print("unknown location (e.g. personalised or pre-2001 plate")
    
