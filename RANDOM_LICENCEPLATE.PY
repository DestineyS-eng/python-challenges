import random 
VALID_LAST_3_LETTERS=["A","B","C","D","E","F","G","H","K","L","M","N","O","P","R","S","V","W","Y","J","U","S","T","X","Z"]
VALID_SECOND_LETTERS=["A","B","C","D","E","F","G","H","K","L","M","N","O","P","R","S","V","W","Y","J","U","S","T","X"]
VALID_LETTERS=["A","B","C","D","E","F","G","H","K","L","M","N","O","P","R","S","V","W","Y"]

randomNum=random.choice([random.randint(2,26),random.randint(51,76)])
randomfristLetter=random.choice(VALID_LETTERS)
randomSecondLetter=random.choice(VALID_SECOND_LETTERS)

randomlast3=random.sample(VALID_LAST_3_LETTERS,3)
randomlast3="".join(randomlast3)

if randomNum<10:
  GenlicencePlate=randomfristLetter+randomSecondLetter+"0"+str(randomNum)+randomlast3
  print(f"an example licence plate would be {GenlicencePlate}")
else:
  GenlicencePlate=randomfristLetter+randomSecondLetter+str(randomNum)+randomlast3
  print(f"an example licence plate would be {GenlicencePlate}")
