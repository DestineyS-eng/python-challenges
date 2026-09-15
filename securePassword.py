#defining constants 
REQ_CHAR=8
#checks if the length is at least 8
def lengthCheck(s):
  if len(s)>=REQ_CHAR:
    return True
  return False
#checks for at least 1 special character
def SpecialCheck(s):
  for char in s:
    if not char.isalpha() and not char.isdigit():
      return True
  return False
#checks for at least 1 digit
def numbersCheck(s):
  for num in s:
    if num.isdigit():
      return True
  return False
#accepts input for passwords
password=input("enter password")
#validation checks adds error to the list
errors=[]
if not lengthCheck(password):
  errors.append("incorrect length")
if not SpecialCheck(password):
  errors.append("missing special character")
if not numbersCheck(password):
  errors.append("missing number")
#if errors is empty print secure else print the errors 
if len(errors)==0:
  print("secure")
else:
  print("rejected password for the following reasons:")
  for error in errors:
    print(f"-{error}")
    
