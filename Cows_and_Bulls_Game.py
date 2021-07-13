import random
digit=5
name=input("enter your name** ")
print("Hello***",name,"***WELCOME TO COWS AND BULLS GAME")
print("********************************************")

def getSecretNum():
    number=list(range(10))
    random.shuffle(number)
    return number
def getclues():
    numbers=getSecretNum()
    secret_num=[]
    for i in range(digit):
        secret_num.append(numbers[i])
    return secret_num
def check_guess():
    bull=[]
    cow=[]
    num=getclues()
    print(num)
    user_can_guess=10
    while user_can_guess>0:
        guess=int(input("enter your guess** "))
        position=int(input("enter the position of your number** "))
        print("----------------------------")
        if guess not in num:
            print("This number is not in the list")
        print("----------------------------")
        if  guess in num:
            index = num.index(guess)
            if index== position: 
                if guess not in bull:
                    bull.insert(index,guess)
                    print("Bull ",bull)
                    print("----------------------------")
                else:
                    print("You Already Used This digit Try  any Different digit")
                    print("----------------------------")
            else:
                if guess not in cow:
                    cow.append(guess)
                    print("This number is in list you can reuse it")
                    print("----------------------------")
                    print("Cow ",cow)
                    print("----------------------------")
                else:
                    print("You Already Used This digit Try  any Different digit")     
                    print("----------------------------")   
        if bull==num:
            print(name,"Congractulations you win the game ")
            print("----------------------------")
            break 
        user_can_guess-=1
        print(user_can_guess,"Turns are left")
    else:
        print("You ran out your tries, You Loose The Game")   
        print("----------------------------")
    return bull
check_guess()
def play_again():
    while True:
        again=input("If you Want to play again press y for yes or n of No*** ") 
        if again=="y":
            check_guess()
        else:
            break 
play_again()