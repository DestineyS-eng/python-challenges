def tower_builder(n_floors):
    tower=["*"]
    #the symbol will be used to calucate the amount of symbols
    symbol="*"
    #starting total for the frist to calculate each layer
    total=3
    if n_floors==2:
        # if its 2 it will return this list so i can sepearte it from the greater values
        tower=["*","***"]
    elif n_floors>2:
        tower=["*","***"]
        #starting at the second position of the loop
        for x in range (2,(n_floors)):
            #it will times the symbol by the value of the layer 
            new=symbol*(x+total)
            #total increases each time to adjust to a new value 
            total+=1
            #add the new stars to the array
            tower.append(new)
    #for the range of the list created it will center each element according to the width of the base
    for i in range (len(tower)):
        tower[i]=tower[i].center(((2*n_floors)-1))
    return tower
    
