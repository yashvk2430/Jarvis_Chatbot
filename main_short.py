import random
computer=random.choice([-1,0,1])
youstr=input("enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reversedDict={1:"snake",-1:"water",0:"gun"}
you=youDict[youstr]
print(f"your choice is {reversedDict[you]} and computer choice is {reversedDict[computer]}")
if(computer==you):
    print("Draw!!")
else:
    if((computer-you)==-1 or (computer-you)==2):
        print("you loss!")
    else:
        print("you win!")