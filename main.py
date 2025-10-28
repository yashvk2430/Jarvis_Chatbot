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
    if(computer==-1 and you==1):
        print("you win!")
    elif(computer==-1 and you==0):
        print("you loss!")
    elif(computer==1 and you==-1):
        print("you loss!")
    elif(computer==1 and you==0):
        print("you win!")
    elif(computer==0 and you==1):
        print("you loss!")
    elif(computer==0 and you==-1):
        print("you win!")
    else:
        print("Something went wrong!!")
