def location_indicators(s):
  #banned letters not allowed and lciense plate is striped of spaces and uppercased
  BANNED="QIZ"
  s=s.strip().upper()
  #will hold the letters in the lciense plate
  letters=""
  #looks at each character in s
  if len(s)==7:
    for char in s:
      #if s is a letter it gets added to letters 
      if char.isalpha() and (not char in BANNED):
        letters+=char
        #if the length is exactly 5 then return the first 2
    if len(letters)==5:
      return letters[:2]
#will store the tag outside the function
tag=location_indicators("BA43Msf")
print(tag)
  
