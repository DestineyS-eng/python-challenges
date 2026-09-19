#calulating birth year
from datetime import datetime
# Get the current year as an integer
def BirthYear(s):
    current_year = datetime.now().year
    try:
        birth_year=current_year-int(s)
    except ValueError:
        birth_year="a"
    return (f"you where born in {birth_year}")

enter=input("enter the age you are turning this year")
x=BirthYear(enter)
if x=="you where born in a":
    print("error:must be an integer")
else:
    print(x)
