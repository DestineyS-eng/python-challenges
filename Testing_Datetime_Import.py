from datetime import datetime
#checking if i can join datetime with concastation
currentdate=str(datetime.now().day)+"/"+str(datetime.now().month)+"/"+str(datetime.now().year)
print(currentdate)
#checking if i can extract string values using slicing 
new=str(datetime.now().year)
length=len(new)
print(new[length-2:])
