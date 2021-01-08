import random

print("Welcome to NUMBER GUESSING GAME!!!")
#checking type of input
def is_int(a):
    try:
        b=int(a)
        return b
    except ValueError:       
        return None
    
while(True):
    
    no=random.randint(0,100)
    chances=6
    
    while chances>0:
        
        a=input("Guess a number (from 1-100) : ")
        x=is_int(a)
        #if x is other than int
        if( x is None):
            print("Not an Integer.")
        #if x is out of range    
        elif(x>100 or x<0):
            print("Invalid Number.")
            
        elif no < x:
            print("Too HIGH! Guess a number smaller than ",x)
            
        elif no > x:
            print("Too LOW! Guess a number greater than ",x)
            
        elif no==x:
            print("Congratulations, You WON!!!")
            break
        #decrementing and printing chances left
        chances=chances-1
        print("Tries left :",chances)
    #failed    
    if chances==0:
        print("Better luck next time!!")
        print("The number is ",no)
    #playing again   
    y=input("Play Again?(Y/N) : ")
    
    if (y=='n'or y=='N') :
        break
    
