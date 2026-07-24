def open_or_senior(data):
    output=""
    if data[0]>=55  and data[1]>7:  # data[0] is for age and data[1] is for handicap
        output=print("Senior")
    else:
        output=print("Open")
        
    return output

x= open_or_senior([55,22])
