grades=[2,1,1,2,2]
def get_mode(grades):
  #will hold a tie between values
  more=[]
  #will hold the singluar mode value
  mode=0
  #holds how many times the mode has appeared 
  times_appeared=0
  for i in range (len(grades)):
    #if the amount of times the element in grades appeared more than times_appeared
    #we will set it as a mode and also set it as the frist item of the more list 
    if grades.count(grades[i])>times_appeared:
      times_appeared=grades.count(grades[i])
      mode=grades[i]
      more=[grades[i]]
    #if the amount of times appeared is equal and not already in more
    #we will append this value into more
    elif times_appeared==grades.count(grades[i]):
      if not grades[i] in more:
        more.append(grades[i])
  #if the list length is less than or equal to 1 we will just return the singluar mode value 
  if len(more)<=1:
    return mode
  #if not it will return the bimodal or multimodal list
  else:
    return more
x=get_mode(grades)
print(x)
