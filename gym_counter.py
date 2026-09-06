#the required workout time must be 30 so ive set it as a constant
BASELINE=30
#as input is default string i wont check for value errors for name 
#but I will check workout_mins so that if theres an error it will give -1 which will be rejected
name=input("enter your name")
try:
    workout_mins=int(input("enter total minutes of your workout"))
except ValueError:
    workout_mins=-1
#if name isnt letters or workout is less than 0 it will return error
if not name.replace(" ","").isalpha() or workout_mins<0:
    print("error")
#if checks baseline against workout to get the right output
else:
    if workout_mins>BASELINE:
        mins_over=workout_mins-BASELINE
        print(f"{name} you have gone over the 30 minute goal by {mins_over} minutes")
    elif workout_mins<30:
        mins_under=BASELINE-workout_mins
        print(f"{name} you have gone under the 30 minute goal by {mins_under} minutes")
    else:
        print(f"{name} you have met the 30 minute goal exactly")
    
