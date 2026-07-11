def DNA_strand(dna):
    DNA_list=dna.upper() #MAKING SURE DNA IS UPPERCASE
    newDNA="" #STORE COMPLEMENTARY PAIRS
    for i in range (len(DNA_list)):  
        if DNA_list[i]=="A":
            newDNA=newDNA+"T"
        elif DNA_list[i]=="T":
            newDNA=newDNA+"A"
        elif DNA_list[i]=="G":
            newDNA=newDNA+"C"
        elif DNA_list[i]=="C":
            newDNA=newDNA+"G"
        else:
            newDNA=newDNA+"" # GIVES NOTHING IF IT ISNT THESE LETTERS 
    return newDNA
    
x= DNA_strand("atgcA")
print(x)
