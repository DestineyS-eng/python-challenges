import random

MAX_SUMMER=26
MAX_WINTER=76
SEPFEB_ADD_ON = 50
REQ_CHARS = 7
INVALID_LETTERS = 'QIZ'
INVALID_SECOND_LETTERS='JUTX'
INVALID_LAST_LETTERS='QI'
VALID_LAST_3_LETTERS=["A","B","C","D","E","F","G","H","K","L","M","N","O","P","R","S","V","W","Y","J","U","S","T","X","Z"]
VALID_SECOND_LETTERS=["A","B","C","D","E","F","G","H","K","L","M","N","O","P","R","S","V","W","Y","J","U","S","T","X"]
VALID_LETTERS=["A","B","C","D","E","F","G","H","K","L","M","N","O","P","R","S","V","W","Y"]


#listed all the offices and their tags
GROUPED_MAP = {
    # ANGLIA
    "Peterborough": ("Anglia", ["AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AJ", "AK", "AL", "AM", "AN"]),
    "Norwich": ("Anglia", ["AO", "AP", "AR", "AS", "AT", "AU"]),
    "Ipswich": ("Anglia", ["AV", "AW", "AX", "AY"]),

    # BIRMINGHAM
    "Birmingham": ("Birmingham", ["BA", "BB", "BC", "BD", "BE", "BF", "BG", "BH", "BJ", "BK", "BL", "BM", "BN", "BO", "BP", "BR", "BS", "BT", "BU", "BV", "BW", "BX", "BY"]),

    # CYMRU (WALES)
    "Cardiff": ("Cymru / Wales", ["CA", "CB", "CC", "CD", "CE", "CF", "CG", "CH", "CJ", "CK", "CL", "CM", "CN", "CO"]),
    "Swansea": ("Cymru / Wales", ["CP", "CR", "CS", "CT", "CU", "CV"]),
    "Bangor": ("Cymru / Wales", ["CW", "CX", "CY"]),

    # DEESIDE TO SHREWSBURY
    "Chester": ("Deeside / Shrewsbury", ["DA", "DB", "DC", "DD", "DE", "DF", "DG", "DH", "DJ", "DK"]),
    "Shrewsbury": ("Deeside / Shrewsbury", ["DL", "DM", "DN", "DO", "DP", "DR", "DS", "DT", "DU", "DV", "DW", "DX", "DY"]),

    # ESSEX
    "Chelmsford": ("Essex", ["EA", "EB", "EC", "ED", "EE", "EF", "EG", "EH", "EJ", "EK", "EL", "EM", "EN", "EO", "EP", "ER", "ES", "ET", "EU", "EV", "EW", "EX", "EY"]),

    # FOREST AND FENS
    "Nottingham": ("Forest and Fens", ["FA", "FB", "FC", "FD", "FE", "FF", "FG", "FH", "FJ", "FK", "FL", "FM", "FN", "FO", "FP"]),
    "Lincoln": ("Forest and Fens", ["FR", "FS", "FT", "FU", "FV", "FW", "FX", "FY"]),

    # GARDEN OF ENGLAND
    "Maidstone": ("Garden of England", ["GA", "GB", "GC", "GD", "GE", "GF", "GG", "GH", "GJ", "GK", "GL", "GM", "GN", "GO"]),
    "Brighton": ("Garden of England", ["GP", "GR", "GS", "GT", "GU", "GV", "GW", "GX", "GY"]),

    # HAMPSHIRE AND DORSET
    "Bournemouth": ("Hampshire and Dorset", ["HA", "HB", "HC", "HD", "HE", "HF", "HG", "HH", "HJ"]),
    "Portsmouth": ("Hampshire and Dorset", ["HK", "HL", "HM", "HN", "HO", "HP", "HR", "HS", "HT", "HU", "HV", "HX", "HY"]),
    "Isle of Wight": ("Hampshire and Dorset", ["HW"]),

    # LUTON AND NORTHAMPTON
    "Luton": ("Luton / Northampton", ["KA", "KB", "KC", "KD", "KE", "KF", "KG", "KH", "KJ", "KK", "KL"]),
    "Northampton": ("Luton / Northampton", ["KM", "KN", "KO", "KP", "KR", "KS", "KT", "KU", "KV", "KW", "KX", "KY"]),

    # LONDON
    "Wimbledon": ("London", ["LA", "LB", "LC", "LD", "LE", "LF", "LG", "LH", "LJ"]),
    "Stanmore": ("London", ["LK", "LL", "LM", "LN", "LO", "LP", "LR", "LS", "LT"]),
    "Sidcup": ("London", ["LU", "LV", "LW", "LX", "LY"]),

    # MANCHESTER
    "Manchester": ("Manchester", ["MA", "MB", "MC", "MD", "ME", "MF", "MG", "MH", "MJ", "MK", "ML", "MM", "MN", "MO", "MP", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY"]),

    # NORTH
    "Newcastle": ("North", ["NA", "NB", "NC", "ND", "NE", "NF", "NG", "NH", "NJ", "NK", "NL", "NM", "NN", "NO"]),
    "Stockton": ("North", ["NP", "NR", "NS", "NT", "NU", "NV", "NW", "NX", "NY"]),

    # OXFORD
    "Oxford": ("Oxford", ["OA", "OB", "OC", "OD", "OE", "OF", "OG", "OH", "OJ", "OK", "OL", "OM", "ON", "OO", "OP", "OR", "OS", "OT", "OU", "OV", "OW", "OX", "OY"]),

    # PRESTON AND CARLISLE
    "Preston": ("Preston / Carlisle", ["PA", "PB", "PC", "PD", "PE", "PF", "PG", "PH", "PJ", "PK", "PL", "PM", "PN", "PO", "PP", "PR", "PS", "PT"]),
    "Carlisle": ("Preston / Carlisle", ["PU", "PV", "PW", "PX", "PY"]),

    # READING
    "Reading": ("Reading", ["RA", "RB", "RC", "RD", "RE", "RF", "RG", "RH", "RJ", "RK", "RL", "RM", "RN", "RO", "RP", "RR", "RS", "RT", "RU", "RV", "RW", "RX", "RY"]),

    # SCOTLAND
    "Glasgow": ("Scotland", ["SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SJ"]),
    "Edinburgh": ("Scotland", ["SK", "SL", "SM", "SN", "SO"]),
    "Dundee": ("Scotland", ["SP", "SR", "SS", "ST"]),
    "Aberdeen": ("Scotland", ["SU", "SV", "SW"]),
    "Inverness": ("Scotland", ["SX", "SY"]),

    # SEVERN VALLEY
    "Worcester": ("Severn Valley", ["VA", "VB", "VC", "VD", "VE", "VF", "VG", "VH", "VJ", "VK", "VL", "VM", "VN", "VO", "VP", "VR", "VS", "VT", "VU", "VV", "VW", "VX", "VY"]),

    # WEST OF ENGLAND
    "Exeter": ("West of England", ["WA", "WB", "WC", "WD", "WE", "WF", "WG", "WH", "WJ"]),
    "Truro": ("West of England", ["WK", "WL"]),
    "Bristol": ("West of England", ["WM", "WN", "WO", "WP", "WR", "WS", "WT", "WU", "WV", "WW", "WX", "WY"]),

    # YORKSHIRE
    "Leeds": ("Yorkshire", ["YA", "YB", "YC", "YD", "YE", "YF", "YG", "YH", "YJ", "YK"]),
    "Sheffield": ("Yorkshire", ["YL", "YM", "YN", "YO", "YP", "YR", "YS", "YT", "YU"]),
    "Beverley": ("Yorkshire", ["YV", "YW", "YX", "YY"])
}
FLETTER_TEST= [
    # --- VALID FRIST LETTERS LOWER CASE---
    "aA21BTR",
    "bA21BTR",
    "cA21BTR",
    "dA21BTR",
    "eA21BTR",
    "fA21BTR",
    "gA21BTR",
    "hA21BTR",
    "kA21BTR",
    "lA21BTR",
    "mA21BTR",
    "nA21BTR",
    "pA21BTR",
    "pA21BTR",
    "rA21BTR",
    "sA21BTR",
    "vA21BTR",
    "wA21BTR",
    "yA21BTR",
    # --- VALID FIRST LETTERS ---
    "AA21BTR",
    "BA21BTR",
    "CA21BTR",
    "DA21BTR",
    "EA21BTR",
    "FA21BTR",
    "GA21BTR",
    "HA21BTR",
    "KA21BTR",
    "LA21BTR",
    "MA21BTR",
    "NA21BTR",
    "OA21BTR",
    "PA21BTR",
    "RA21BTR",
    "SA21BTR",
    "VA21BTR",
    "WA21BTR",
    "YA21BTR",
    # --- INVALID FIRST LETTERS ---
    "QA21BTR",
    "IA21BTR",
    "ZA21BTR",
    "JA21BTR",
    "UA21BTR",
    "TA21BTR",
    "XA21BTR",
    "QA21BTR",
    "iA21BTR",
    "zA21BTR",
    "jA21BTR",
    "uA21BTR",
    "tA21BTR",
    "xA21BTR",
    # --- ERRONEOUS FIRST CHARACTERS ---
    "0A21BTR",
    "1A21BTR",
    "9A21BTR",
    "#A21BTR",
    "$A21BTR",
    "!A21BTR",
    "@A21BTR",
]
SECLETTER_TEST=[
    # --- VALID SECOND LETTERS (UPPERCASE) ---
    "AA21BTR",
    "AB21BTR",
    "AC21BTR",
    "AD21BTR",
    "AE21BTR",
    "AF21BTR",
    "AG21BTR",
    "AH21BTR",
    "AJ21BTR",
    "AK21BTR",
    "AL21BTR",
    "AM21BTR",
    "AN21BTR",
    "AO21BTR",
    "AP21BTR",
    "AR21BTR",
    "AS21BTR",
    "AT21BTR",
    "AU21BTR",
    "AV21BTR",
    "AW21BTR",
    "AX21BTR",
    "AY21BTR",
    # --- VALID SECOND LETTERS (LOWERCASE) ---
    "Aa21BTR",
    "Ab21BTR",
    "Ac21BTR",
    "Ad21BTR",
    "Ae21BTR",
    "Af21BTR",
    "Ag21BTR",
    "Ah21BTR",
    "Aj21BTR",
    "Ak21BTR",
    "Al21BTR",
    "Am21BTR",
    "An21BTR",
    "Ao21BTR",
    "Ap21BTR",
    "Ar21BTR",
    "As21BTR",
    "At21BTR",
    "Au21BTR",
    "Av21BTR",
    "Aw21BTR",
    "Ax21BTR",
    "Ay21BTR",
    # --- INVALID SECOND LETTERS (UPPERCASE & LOWERCASE) ---
    "AI21BTR",
    "AQ21BTR",
    "AZ21BTR",
    "Ai21BTR",
    "Aq21BTR",
    "Az21BTR",
    # --- ERRONEOUS SECOND CHARACTERS ---
    "A021BTR",
    "A121BTR",
    "A921BTR",
    "A#21BTR",
    "A$21BTR",
    "A!21BTR",
    "A@21BTR",
]
LASTLETTERS_TEST=[
    # --- VALID LAST 3 LETTERS (UPPERCASE) ---
    "AB21AAA",
    "AB21ZZZ",
    "AB21BTR",
    "AB21JUT",
    "AB21STX",
    "AB21CDE",
    "AB21FGH",
    "AB21KLM",
    "AB21NOP",
    "AB21RSV",
    "AB21WYZ",
    # --- VALID LAST 3 LETTERS (LOWERCASE) ---
    "AB21aaa",
    "AB21zzz",
    "AB21btr",
    "AB21jut",
    "AB21stx",
    "AB21cde",
    "AB21fgh",
    "AB21klm",
    "AB21nop",
    "AB21rsv",
    "AB21wyz",
    # --- INVALID LAST 3 LETTERS: 'Q' IN POSITIONS 1, 2, 3 (UPPERCASE) ---
    "AB21QTR",
    "AB21BQR",
    "AB21BTQ",
    # --- INVALID LAST 3 LETTERS: 'I' IN POSITIONS 1, 2, 3 (UPPERCASE) ---
    "AB21ITR",
    "AB21BIR",
    "AB21BTI",
    # --- INVALID LAST 3 LETTERS: COMBINATIONS OF 'Q' AND 'I' (UPPERCASE) ---
    "AB21QIT",
    "AB21IQT",
    "AB21QQQ",
    "AB21III",
    # --- INVALID LAST 3 LETTERS: 'Q' & 'I' (LOWERCASE) ---
    "AB21qtr",
    "AB21bqr",
    "AB21btq",
    "AB21itr",
    "AB21bir",
    "AB21bti",
    "AB21qit",
    "AB21iqt",
    "AB21qqq",
    "AB21iii",
    # --- ERRONEOUS LAST 3 CHARACTERS: DIGITS IN POSITIONS 1, 2, 3 ---
    "AB211TR",
    "AB21B1R",
    "AB21BT1",
    "AB21000",
    "AB21999",
    # --- ERRONEOUS LAST 3 CHARACTERS: SYMBOLS IN POSITIONS 1, 2, 3 ---
    "AB21#TR",
    "AB21B$R",
    "AB21BT!",
    "AB21@TR",
    "AB21%^&",
]
NUMBER_TEST=[
    # --- VALID SUMMER NUMBERS (02 - 26) ---
    "AB02BTR",  # Summer lower boundary (02)
    "AB03BTR",  # Summer lower boundary + 1
    "AB15BTR",  # Summer mid-range (15)
    "AB25BTR",  # Summer upper boundary - 1
    "AB26BTR",  # Summer upper boundary (26)
    # --- VALID WINTER NUMBERS (51 - 76) ---
    "AB51BTR",  # Winter lower boundary (51)
    "AB52BTR",  # Winter lower boundary + 1
    "AB65BTR",  # Winter mid-range (65)
    "AB75BTR",  # Winter upper boundary - 1
    "AB76BTR",  # Winter upper boundary (76)
    # --- INVALID AGE NUMBERS (OUT OF RANGE) ---
    "AB00BTR",  # Below summer lower boundary (00)
    "AB01BTR",  # Below summer lower boundary (01)
    "AB27BTR",  # Above summer upper boundary (27)
    "AB50BTR",  # Below winter lower boundary (50)
    "AB77BTR",  # Above winter upper boundary (77)
    "AB99BTR",  # Far above winter upper boundary (99)
    # --- ERRONEOUS MIDDLE CHARACTERS ---
    "ABXXBTR",  # Letters in place of age numbers
    "AB$$BTR",  # Symbols in place of age numbers
    "AB!!BTR",  # Symbols in place of age numbers
]
LENGTH_TEST=[
    # --- VALID LENGTH (EXACTLY 7 CHARACTERS AFTER STRIPPING SPACES) ---
    "AB21BTR",       # Standard 7-character plate
    "AB 21BTR",      # 7 characters with single internal space
    "AB21 BTR",      # Standard UK space format (7 characters)
    "A B 2 1 B T R", # 7 characters with spaces between all characters
    "  AB21BTR  ",   # 7 characters with leading and trailing spaces

    # --- INVALID LENGTH: TOO SHORT (< 7 CHARACTERS) ---
    "",              # Boundary lower limit (0 characters / empty string)
    "A",             # Single character
    "AB21",          # 4 characters
    "AB21BT",        # Boundary lower limit (6 characters)
    "AB 21BT",       # 6 characters after spaces are stripped

    # --- INVALID LENGTH: TOO LONG (> 7 CHARACTERS) ---
    "AB21BTRX",      # Boundary upper limit (8 characters)
    "AB 21 BTRX",    # 8 characters after spaces are stripped
    "AB-21-BTR",     # Erroneous hyphenated format (9 characters total)
    "AB21BTRXYZ",    # 10 characters
]
REGIONCITY_TEST=[
    # --- ANGLIA ---
    # Peterborough
    "AA21BTR", "AB21BTR", "AC21BTR", "AD21BTR", "AE21BTR", "AF21BTR", "AG21BTR", "AH21BTR", "AJ21BTR", "AK21BTR", "AL21BTR", "AM21BTR", "AN21BTR",
    # Norwich
    "AO21BTR", "AP21BTR", "AR21BTR", "AS21BTR", "AT21BTR", "AU21BTR",
    # Ipswich
    "AV21BTR", "AW21BTR", "AX21BTR", "AY21BTR",

    # --- BIRMINGHAM ---
    # Birmingham
    "BA21BTR", "BB21BTR", "BC21BTR", "BD21BTR", "BE21BTR", "BF21BTR", "BG21BTR", "BH21BTR", "BJ21BTR", "BK21BTR", "BL21BTR", "BM21BTR", "BN21BTR", "BO21BTR", "BP21BTR", "BR21BTR", "BS21BTR", "BT21BTR", "BU21BTR", "BV21BTR", "BW21BTR", "BX21BTR", "BY21BTR",

    # --- CYMRU (WALES) ---
    # Cardiff
    "CA21BTR", "CB21BTR", "CC21BTR", "CD21BTR", "CE21BTR", "CF21BTR", "CG21BTR", "CH21BTR", "CJ21BTR", "CK21BTR", "CL21BTR", "CM21BTR", "CN21BTR", "CO21BTR",
    # Swansea
    "CP21BTR", "CR21BTR", "CS21BTR", "CT21BTR", "CU21BTR", "CV21BTR",
    # Bangor
    "CW21BTR", "CX21BTR", "CY21BTR",

    # --- DEESIDE TO SHREWSBURY ---
    # Chester
    "DA21BTR", "DB21BTR", "DC21BTR", "DD21BTR", "DE21BTR", "DF21BTR", "DG21BTR", "DH21BTR", "DJ21BTR", "DK21BTR",
    # Shrewsbury
    "DL21BTR", "DM21BTR", "DN21BTR", "DO21BTR", "DP21BTR", "DR21BTR", "DS21BTR", "DT21BTR", "DU21BTR", "DV21BTR", "DW21BTR", "DX21BTR", "DY21BTR",

    # --- ESSEX ---
    # Chelmsford
    "EA21BTR", "EB21BTR", "EC21BTR", "ED21BTR", "EE21BTR", "EF21BTR", "EG21BTR", "EH21BTR", "EJ21BTR", "EK21BTR", "EL21BTR", "EM21BTR", "EN21BTR", "EO21BTR", "EP21BTR", "ER21BTR", "ES21BTR", "ET21BTR", "EU21BTR", "EV21BTR", "EW21BTR", "EX21BTR", "EY21BTR",

    # --- FOREST AND FENS ---
    # Nottingham
    "FA21BTR", "FB21BTR", "FC21BTR", "FD21BTR", "FE21BTR", "FF21BTR", "FG21BTR", "FH21BTR", "FJ21BTR", "FK21BTR", "FL21BTR", "FM21BTR", "FN21BTR", "FO21BTR", "FP21BTR",
    # Lincoln
    "FR21BTR", "FS21BTR", "FT21BTR", "FU21BTR", "FV21BTR", "FW21BTR", "FX21BTR", "FY21BTR",

    # --- GARDEN OF ENGLAND ---
    # Maidstone
    "GA21BTR", "GB21BTR", "GC21BTR", "GD21BTR", "GE21BTR", "GF21BTR", "GG21BTR", "GH21BTR", "GJ21BTR", "GK21BTR", "GL21BTR", "GM21BTR", "GN21BTR", "GO21BTR",
    # Brighton
    "GP21BTR", "GR21BTR", "GS21BTR", "GT21BTR", "GU21BTR", "GV21BTR", "GW21BTR", "GX21BTR", "GY21BTR",

    # --- HAMPSHIRE AND DORSET ---
    # Bournemouth
    "HA21BTR", "HB21BTR", "HC21BTR", "HD21BTR", "HE21BTR", "HF21BTR", "HG21BTR", "HH21BTR", "HJ21BTR",
    # Portsmouth
    "HK21BTR", "HL21BTR", "HM21BTR", "HN21BTR", "HO21BTR", "HP21BTR", "HR21BTR", "HS21BTR", "HT21BTR", "HU21BTR", "HV21BTR", "HX21BTR", "HY21BTR",
    # Isle of Wight
    "HW21BTR",

    # --- LUTON AND NORTHAMPTON ---
    # Luton
    "KA21BTR", "KB21BTR", "KC21BTR", "KD21BTR", "KE21BTR", "KF21BTR", "KG21BTR", "KH21BTR", "KJ21BTR", "KK21BTR", "KL21BTR",
    # Northampton
    "KM21BTR", "KN21BTR", "KO21BTR", "KP21BTR", "KR21BTR", "KS21BTR", "KT21BTR", "KU21BTR", "KV21BTR", "KW21BTR", "KX21BTR", "KY21BTR",

    # --- LONDON ---
    # Wimbledon
    "LA21BTR", "LB21BTR", "LC21BTR", "LD21BTR", "LE21BTR", "LF21BTR", "LG21BTR", "LH21BTR", "LJ21BTR",
    # Stanmore
    "LK21BTR", "LL21BTR", "LM21BTR", "LN21BTR", "LO21BTR", "LP21BTR", "LR21BTR", "LS21BTR", "LT21BTR",
    # Sidcup
    "LU21BTR", "LV21BTR", "LW21BTR", "LX21BTR", "LY21BTR",

    # --- MANCHESTER ---
    # Manchester
    "MA21BTR", "MB21BTR", "MC21BTR", "MD21BTR", "ME21BTR", "MF21BTR", "MG21BTR", "MH21BTR", "MJ21BTR", "MK21BTR", "ML21BTR", "MM21BTR", "MN21BTR", "MO21BTR", "MP21BTR", "MR21BTR", "MS21BTR", "MT21BTR", "MU21BTR", "MV21BTR", "MW21BTR", "MX21BTR", "MY21BTR",

    # --- NORTH ---
    # Newcastle
    "NA21BTR", "NB21BTR", "NC21BTR", "ND21BTR", "NE21BTR", "NF21BTR", "NG21BTR", "NH21BTR", "NJ21BTR", "NK21BTR", "NL21BTR", "NM21BTR", "NN21BTR", "NO21BTR",
    # Stockton
    "NP21BTR", "NR21BTR", "NS21BTR", "NT21BTR", "NU21BTR", "NV21BTR", "NW21BTR", "NX21BTR", "NY21BTR",

    # --- OXFORD ---
    # Oxford
    "OA21BTR", "OB21BTR", "OC21BTR", "OD21BTR", "OE21BTR", "OF21BTR", "OG21BTR", "OH21BTR", "OJ21BTR", "OK21BTR", "OL21BTR", "OM21BTR", "ON21BTR", "OO21BTR", "OP21BTR", "OR21BTR", "OS21BTR", "OT21BTR", "OU21BTR", "OV21BTR", "OW21BTR", "OX21BTR", "OY21BTR",

    # --- PRESTON AND CARLISLE ---
    # Preston
    "PA21BTR", "PB21BTR", "PC21BTR", "PD21BTR", "PE21BTR", "PF21BTR", "PG21BTR", "PH21BTR", "PJ21BTR", "PK21BTR", "PL21BTR", "PM21BTR", "PN21BTR", "PO21BTR", "PP21BTR", "PR21BTR", "PS21BTR", "PT21BTR",
    # Carlisle
    "PU21BTR", "PV21BTR", "PW21BTR", "PX21BTR", "PY21BTR",

    # --- READING ---
    # Reading
    "RA21BTR", "RB21BTR", "RC21BTR", "RD21BTR", "RE21BTR", "RF21BTR", "RG21BTR", "RH21BTR", "RJ21BTR", "RK21BTR", "RL21BTR", "RM21BTR", "RN21BTR", "RO21BTR", "RP21BTR", "RR21BTR", "RS21BTR", "RT21BTR", "RU21BTR", "RV21BTR", "RW21BTR", "RX21BTR", "RY21BTR",

    # --- SCOTLAND ---
    # Glasgow
    "SA21BTR", "SB21BTR", "SC21BTR", "SD21BTR", "SE21BTR", "SF21BTR", "SG21BTR", "SH21BTR", "SJ21BTR",
    # Edinburgh
    "SK21BTR", "SL21BTR", "SM21BTR", "SN21BTR", "SO21BTR",
    # Dundee
    "SP21BTR", "SR21BTR", "SS21BTR", "ST21BTR",
    # Aberdeen
    "SU21BTR", "SV21BTR", "SW21BTR",
    # Inverness
    "SX21BTR", "SY21BTR",

    # --- SEVERN VALLEY ---
    # Worcester
    "VA21BTR", "VB21BTR", "VC21BTR", "VD21BTR", "VE21BTR", "VF21BTR", "VG21BTR", "VH21BTR", "VJ21BTR", "VK21BTR", "VL21BTR", "VM21BTR", "VN21BTR", "VO21BTR", "VP21BTR", "VR21BTR", "VS21BTR", "VT21BTR", "VU21BTR", "VV21BTR", "VW21BTR", "VX21BTR", "VY21BTR",

    # --- WEST OF ENGLAND ---
    # Exeter
    "WA21BTR", "WB21BTR", "WC21BTR", "WD21BTR", "WE21BTR", "WF21BTR", "WG21BTR", "WH21BTR", "WJ21BTR",
    # Truro
    "WK21BTR", "WL21BTR",
    # Bristol
    "WM21BTR", "WN21BTR", "WO21BTR", "WP21BTR", "WR21BTR", "WS21BTR", "WT21BTR", "WU21BTR", "WV21BTR", "WW21BTR", "WX21BTR", "WY21BTR",

    # --- YORKSHIRE ---
    # Leeds
    "YA21BTR", "YB21BTR", "YC21BTR", "YD21BTR", "YE21BTR", "YF21BTR", "YG21BTR", "YH21BTR", "YJ21BTR", "YK21BTR",
    # Sheffield
    "YL21BTR", "YM21BTR", "YN21BTR", "YO21BTR", "YP21BTR", "YR21BTR", "YS21BTR", "YT21BTR", "YU21BTR",
    # Beverley
    "YV21BTR", "YW21BTR", "YX21BTR", "YY21BTR",

    # --- LOWERCASE VALID TAGS ---
    "aa21btr", "ba21btr", "ca21btr", "da21btr", "ea21btr", "fa21btr", "ga21btr", "ha21btr", "ka21btr", "la21btr", "ma21btr", "na21btr", "oa21btr", "pa21btr", "ra21btr", "sa21btr", "va21btr", "wa21btr", "ya21btr",

    # --- INVALID START TAGS (DISALLOWED LETTERS Q, I, Z, J, U, T, X) ---
    "QA21BTR", "IA21BTR", "ZA21BTR", "JA21BTR", "UA21BTR", "TA21BTR", "XA21BTR",
    "AQ21BTR", "AI21BTR", "AZ21BTR", "ZZ21BTR",

    # --- ERRONEOUS START TAGS (DIGITS & SYMBOLS) ---
    "0A21BTR", "1A21BTR", "9A21BTR", "#A21BTR", "$A21BTR", "!A21BTR", "@A21BTR",
    "A021BTR", "A121BTR", "A921BTR", "A#21BTR", "A$21BTR", "A!21BTR", "A@21BTR"
]
YEAR_OUTPUT_TEST = [
    # --- SUMMER REGISTRATIONS (MARCH - AUGUST) ---
    "AB02BTR",  # Single digit year (<10) -> march-august of 2002
    "AB09BTR",  # Single digit year (<10) -> march-august of 2009
    "AB10BTR",  # Two digit year (10-26)  -> march-august of 2010
    "AB21BTR",  # Two digit year (10-26)  -> march-august of 2021
    "AB26BTR",  # Summer max boundary     -> march-august of 2026

    # --- WINTER REGISTRATIONS (FEBRUARY - SEPTEMBER) ---
    "AB51BTR",  # Single digit year after subtraction (51-59) -> febuary-september of 2001
    "AB59BTR",  # Single digit year after subtraction (51-59) -> febuary-september of 2009
    "AB60BTR",  # Two digit year after subtraction (60-76)    -> febuary-september of 2010
    "AB71BTR",  # Two digit year after subtraction (60-76)    -> febuary-september of 2021
    "AB76BTR"   # Winter max boundary                        -> febuary-september of 2026
]
MENU_TEST = [
    # --- VALID MENU SELECTIONS (NORMAL / BOUNDARY) ---
    "0",   # Exit program / Minimum boundary
    "1",   # Option 1: Check for valid licence plate
    "2",   # Option 2: Find age of the car
    "3",   # Option 3: Find the city registered in
    "4",   # Option 4: Generate example licence plate / Maximum boundary

    # --- INVALID NUMERIC OPTIONS (OUT OF RANGE) ---
    "5",   # Numeric value above valid range
    "9",   # Single digit far above range
    "-1",  # Negative number
    "10",  # Multi-digit number
    "123", # Long numeric string

    # --- SUBSTRING EDGE CASES ---
    "12",   # Contiguous multi-digit substring
    "23",   # Contiguous multi-digit substring
    "34",   # Contiguous multi-digit substring
    "012",  # Three-digit contiguous substring

    # --- INVALID NON-NUMERIC / CHARACTER INPUTS ---
    "a",   # Lowercase letter
    "A",   # Uppercase letter
    "x",   # Arbitrary character
    "#",   # Special character / symbol
    "!",   # Symbol

    # --- ERRONEOUS / BOUNDARY INPUTS ---
    "",    # Empty string (user presses Enter without typing)
    " ",   # Single whitespace
    " 1 ", # Valid choice surrounded by spaces
    "0.0", # Floating point number format
]
#this function takes a string and strips out the spaces
def strip_spaces(s):
    s=s.replace(" ","")
    return s

#this returns true if the final 3 letters are valid
def ValidEnd(s):
    for char in s:
        if char in INVALID_LAST_LETTERS or char.isdigit() or not char.isalpha():
            return False
    return True
#valid length
def ValidLength(s):
    if len(s)!=7:
        return False
    return True
#checks for valid start
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

print("\nChoose A Test Case: \n1.frist letters \n2.second letters \n3.last 3 letters \n4.number test \n5.length test \n6.region and city test \n7.year output\n8.Menu test\n9.Random plate test")
Test=input("Choose a test 1-9:")
if Test=="1":
    for plate in FLETTER_TEST:
        user_licence_plate=plate
        user_licence_plate=strip_spaces(user_licence_plate).upper()
        #checks for a valid licence plate 
        final_char=user_licence_plate[-3:] 
                
        if not ValidLength(user_licence_plate):
            print(f'error: this length does not equal 7{plate}')
        elif not ValidStartLetters(user_licence_plate):
            print(f'error: the starting letters are not valid (QIZJUSTX and digits){plate}')
        elif not ValidEnd(final_char):
            print(f'error: that is not a valid end {plate}')
            
        elif not ValidMIddleNUmbers(user_licence_plate):
            print(f'error: these digits are not in valid ranges (2-{MAX_SUMMER}) and (51-{MAX_WINTER})/ non digits {plate}')
        else:
            print(f"this is a valid licence plate {plate}")


elif Test=="2":
    for secPlate in SECLETTER_TEST:
        user_licence_plate=secPlate
        user_licence_plate=strip_spaces(user_licence_plate).upper()
         #checks for a valid licence plate 
        final_char=user_licence_plate[-3:] 
                
        if not ValidLength(user_licence_plate):
            print(f'error: this length does not equal 7{secPlate}')
        elif not ValidStartLetters(user_licence_plate):
            print(f'error: the starting letters are not valid (QIZJUSTX and digits){secPlate}')
        elif not ValidEnd(final_char):
            print(f'error: that is not a valid end {secPlate}')
            
        elif not ValidMIddleNUmbers(user_licence_plate):
            print(f'error: these digits are not in valid ranges (2-{MAX_SUMMER}) and (51-{MAX_WINTER})/ non digits {secPlate}')
        else:
            print(f"this is a valid licence plate {secPlate}")
        
elif Test=="3":
    for ThirdPlate in LASTLETTERS_TEST:
        user_licence_plate=ThirdPlate
        user_licence_plate=strip_spaces(user_licence_plate).upper()
        #checks for a valid licence plate 
        final_char=user_licence_plate[-3:] 
        
        if not ValidLength(user_licence_plate):
            print(f'error: this length does not equal 7{ThirdPlate}')
        elif not ValidStartLetters(user_licence_plate):
            print(f'error: the starting letters are not valid (QIZJUSTX and digits){ThirdPlate}')
        elif not ValidEnd(final_char):
            print(f'error: that is not a valid end {ThirdPlate}')
         
        elif not ValidMIddleNUmbers(user_licence_plate):
            print(f'error: these digits are not in valid ranges (2-{MAX_SUMMER}) and (51-{MAX_WINTER})/ non digits {ThirdPlate}')
        else:
            print(f"this is a valid licence plate {ThirdPlate}")

elif Test=="4":
    for fourthPlate in NUMBER_TEST:
        user_licence_plate=fourthPlate
        user_licence_plate=strip_spaces(user_licence_plate).upper()
         #checks for a valid licence plate 
        final_char=user_licence_plate[-3:] 
                
        if not ValidLength(user_licence_plate):
            print(f'error: this length does not equal 7{fourthPlate}')
        elif not ValidStartLetters(user_licence_plate):
            print(f'error: the starting letters are not valid (QIZJUSTX and digits){fourthPlate}')
        elif not ValidEnd(final_char):
            print(f'error: that is not a valid end {fourthPlate}')
            
        elif not ValidMIddleNUmbers(user_licence_plate):
            print(f'error: these digits are not in valid ranges (2-{MAX_SUMMER}) and (51-{MAX_WINTER})/ non digits {fourthPlate}')
        else:
            print(f"this is a valid licence plate {fourthPlate}")
        
elif Test=="5":
    for test5 in LENGTH_TEST:
        user_licence_plate=test5
        user_licence_plate=strip_spaces(user_licence_plate).upper()
        #checks for a valid licence plate 
        final_char=user_licence_plate[-3:] 
                
        if not ValidLength(user_licence_plate):
            print(f'error: this length does not equal 7{test5}')
        elif not ValidStartLetters(user_licence_plate):
            print(f'error: the starting letters are not valid (QIZJUSTX and digits){test5}')
        elif not ValidEnd(final_char):
            print(f'error: that is not a valid end {test5}')
            
        elif not ValidMIddleNUmbers(user_licence_plate):
            print(f'error: these digits are not in valid ranges (2-{MAX_SUMMER}) and (51-{MAX_WINTER})/ non digits {test5}')
        else:
            print(f"this is a valid licence plate {test5}")    
elif Test=="6":
    for test6 in REGIONCITY_TEST:
        user_licence_plate=test6
        user_licence_plate=strip_spaces(user_licence_plate).upper()
        #checks for a valid licence plate 
        final_char=user_licence_plate[-3:] 
                
        if not ValidLength(user_licence_plate):
            print(f'error: this length does not equal 7{test6}')
        elif not ValidStartLetters(user_licence_plate):
            print(f'error: the starting letters are not valid (QIZJUSTX and digits){test6}')
        elif not ValidEnd(final_char):
            print(f'error: that is not a valid end {test6}')
            
        elif not ValidMIddleNUmbers(user_licence_plate):
            print(f'error: these digits are not in valid ranges (2-{MAX_SUMMER}) and (51-{MAX_WINTER})/ non digits {test6}')
        else:
            print(f"this is a valid licence plate {test6}") 
        #items allow me to assgin city, region and tags as seperate variables and to go through each
        tag=user_licence_plate[:2]
                
        for cities,(region,tags) in GROUPED_MAP.items():
        #if the tag in in the grouped tag we will print the city and region and then break the loop so else isnt printed
            if tag in tags:
                print(f"region in: {region} registed in: {cities}")
elif Test=="7":
    for year in YEAR_OUTPUT_TEST:
        user_licence_plate=year
        user_licence_plate=strip_spaces(user_licence_plate).upper()

        numbers=int(user_licence_plate[2:4])
                        
        #gives the year and approx months
        if numbers<10:
            print(f"this was registered in march-august of 2{numbers:0>3} ,{year}")
        elif 10<=numbers<=MAX_SUMMER:
            print(f"this was registered in march-august of 20{numbers} ,{year}")
        elif 51<=numbers<60:
            numbers-=SEPFEB_ADD_ON
            print(f"this was registered in febuary-september of 2{numbers:0>3} ,{year}")
        elif 60<=numbers<=MAX_WINTER:
            numbers-=SEPFEB_ADD_ON
            print(f"this was registered in febuary-september of 20{numbers} ,{year}")
elif Test=="8":
    for test8 in MENU_TEST:
        ChooseOption=test8
        if not ChooseOption in ['0','1','2','3','4']:
            print(f"Error not a valid number {test8}")
        elif ChooseOption=="4":
            print(f"Generate example licence plate {test8}")
        elif ChooseOption=="1":
            print(f"Check for valid licence plate {test8}")
        elif ChooseOption=="2":
            print(f"Find age of the car {test8}")
        elif ChooseOption=="3":
            print(f"Find the city registered in {test8}")
        elif ChooseOption=="0":
            print(f"Quitting program {test8}")
elif Test=="9":
    for i in range (len(REGIONCITY_TEST)):
        #generates an example licence plate 
        randomNum=random.choice([random.randint(2,MAX_SUMMER),random.randint(51,MAX_WINTER)])
        randomfristLetter=random.choice(VALID_LETTERS)
        randomSecondLetter=random.choice(VALID_SECOND_LETTERS)
    
        randomlast3=random.sample(VALID_LAST_3_LETTERS,3)
        randomlast3="".join(randomlast3)
        
        if randomNum<10:
            licence=GenlicencePlate=randomfristLetter+randomSecondLetter+"0"+str(randomNum)+randomlast3
            tag=licence[:2]
            
            for cities,(region,tags) in GROUPED_MAP.items():
                    #if the tag in in the grouped tag we will print the city and region and then break the loop so else isnt printed
                    if tag in tags:
                        print(f"region in: {region} registed in: {cities} ,{licence}")
        elif randomNum>=10:
            licence=GenlicencePlate=randomfristLetter+randomSecondLetter+str(randomNum)+randomlast3
            tag=licence[:2]

            for cities,(region,tags) in GROUPED_MAP.items():
                #if the tag in in the grouped tag we will print the city and region and then break the loop so else isnt printed
                if tag in tags:
                    print(f"region in: {region} registed in: {cities} ,{licence}")
        else:
            print(f"not found")
