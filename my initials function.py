def abbrev_name(name):
    Name=list(name.upper()) #puts the persons name into uppercase and a list 
    Initials="." 
    Initials=str(Name[0])+Initials #do the frist name letter frist as we dont need to locate it via a loop 
    for i in range (len(Name)):
        if Name[i]==" ":
            Initials=Initials+(Name[i+1]) #frist letter aftere the space will be the frist letter of the surname 
    return Initials
