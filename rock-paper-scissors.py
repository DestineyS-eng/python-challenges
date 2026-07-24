import random 
points=0
CPUpoints=0
moves=["rock","paper","scissors"]
#an array to hold the values of CPUmoves 
for x in range (0,4):
      movePlayer=str(input("rock, paper or scissors :"))
      CPUmove=random.choice(moves)
      # CPU moves will be random each time 
      if (movePlayer=="rock" and CPUmove=="scissors") or(movePlayer=="paper" and CPUmove=="rock") or(movePlayer=="scissors" and CPUmove=="paper"):
          print("player wins")
          points=points+5
          #all possible ways player can win resulting in a 5 point additon
      if movePlayer== CPUmove :
          print("draw")
          #equal outputs will result in draws.no additonal points 
      else:
          print("CPU wins")
          CPUpoints=CPUpoints+5
          #anything else should result in CPU winning 
winner=points-CPUpoints
if winner > 0:
    print("PLAYER WINS!")
else:
    print("YOU LOOSE")
#calculating overall winners using the fact that if player won their diffrence of points will be postive which is above zero. and negative if they lost which is below zero.
      
          
       
