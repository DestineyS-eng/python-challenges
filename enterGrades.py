#constant of full marks and full class so that you can change it depending on tests
FULL_CLASS=13
FULL_MARKS=100
grades=[]
#collecting the 13 grades
while len(grades)!=FULL_CLASS:
  try:
    enterGrade=int(input("Enter a grade:"))
  except ValueError:
    enterGrade=-1
  if 0>enterGrade or enterGrade>FULL_MARKS:
    print("error:invalid grade")
  else:
    grades.append(enterGrade)
#average grade
total=0
for num in grades:
  total+=num
average=total/FULL_CLASS
print(f"the average score is:{average}")
#highest score
highest=max(grades)
print(f"the highest score is:{highest}")
#lowest score
lowest=min(grades)
print(f"the lowest score is:{lowest}")

