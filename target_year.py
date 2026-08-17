def nb_year(p0, percent, aug, p):
    #will hold the years it took
    years=0
    #while the current population isnt greater than or equal to the target
    #we will calucate the increase each year and increase year buy 1
    while not p0>=p:
        p0=p0+int(p0*percent/100)+aug
        years+=1
    return years
        
    
