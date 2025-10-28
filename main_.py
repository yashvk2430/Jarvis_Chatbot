import random

n=random.randint(1,100)
a=-1
guesses=1
while(a!=n):
    
    a=int(input("enter the number"))
    if(a>n):
        print("lower number please")
    elif(a<n):
        print("higher number please")
    guesses+=1
print(f"you have guesse the number {n} correctly {guesses} attempts")