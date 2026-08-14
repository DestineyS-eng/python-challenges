def count_smileys(arr):
    #holds the total number of valid smiles 
    total=0
    #goes through each list 
    for smile in arr:
        #checks if the frist element contains valid eyes
        if smile[0]==";" or smile[0]==":":
            #if the length of the smile is two and contains either of the valid mouths
            #then we increase total  by 1
            if len(smile)==2 and (smile[1]==")" or smile[1]=="D"):
                total+=1
            #if it isnt then it will check if the length is three and has either of the vaild noses
            elif  len(smile)==3 and (smile[1]=="-" or smile[1]=="~"):
                #then it will check for a vaild mouth 
                #if it meets thde critrea then total will increase by 1 
                if smile[2]==")" or smile[2]=="D":
                    total+=1
    return total
