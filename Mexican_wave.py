def wave(people):
    #holds the wave ouputs
    new=[]
    #if the letter is a letter it will uppercase the current and add the rest from the front and back
    for i in range (1,len(people)):
        if people[i].isalpha():
            new.append(people[:i-1] + people[i-1].upper() + people[i:])
    return new
x=wave("hello")
print(x)
