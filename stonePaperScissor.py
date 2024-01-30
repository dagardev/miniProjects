import random;
computerChoice=random.choice(["Stone","Paper","Scissor"])
# print(computerChoice)

while(True):
    userChoice=int(input('''"Enter Your Choice:- "
                     Press 1 for Stone
                     Press 2 for Paper
                     Press 3 for Scissor
                     '''))
    if (userChoice==1):
        userChoice="Stone"
    elif (userChoice==2):
        userChoice="Paper"
    elif (userChoice==3):
        userChoice="Scissor"
    else:
        print("Invalid Choice Try Again")
        continue
    break

print("Computer Choice = ", computerChoice)
print("User Choice = ", userChoice)
if(computerChoice==userChoice):
    print("Match Tie")
elif (computerChoice=="Stone" and userChoice=="Scissor" or computerChoice=="Paper" and userChoice=="Stone" or computerChoice=="Scissor" and userChoice=="Paper"):
    print("COMPUTER WON")
else:
    print("USER WON")