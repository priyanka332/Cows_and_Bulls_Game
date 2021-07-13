import random
def cow_bull():
    list1=[0,1,2,3,4,5,6,7,8,9]
    i=0
    secret_list=[]
    bull=[]
    cow=[]
    while i < 5:
        random_number = random.choice(list1)
        if random_number not in secret_list:
            secret_list.append(random_number)
            i=i+1
    print(secret_list,"ye secret list hain")
    total_chances=10
    count_of_chances=0
    while count_of_chances<total_chances:
        number=int(input("guess a number"))
        position=int(input("guess the position"))
        if (number in secret_list) and (secret_list.index(number) == position):
            if number not in bull:
                bull.insert(position,number)
                print("-------------------------------------")
                print("Bull",bull)
                print("-------------------------------------")
            else:
                print("-------------------------------------")
                print("you already used this digit, try another digit")
                print("-------------------------------------")
        elif (number in secret_list):
            if number not in cow:
                cow.append(number)
                print("-------------------------------------")
                print("Cow, These are correct numbers you can reuse it",cow)
                print("-------------------------------------")
            else:
                print("-------------------------------------")
                print("you already used this digit, try another digit")
                print("-------------------------------------")
        else:
            print("-------------------------------------")
            print("this number is not in secret list")
            print("-------------------------------------")
        count_of_chances+=1 
        print("chances that you used",total_chances-count_of_chances)
        if secret_list==bull:
            print("-------------------------------------")
            print("you win the game")
            break
    else:
        print("-------------------------------------")
        print("you lose the game")
    while True:
        again=input("you want to play again yes or no:=")
        if again=="yes":
            cow_bull()
        else:
            break              
cow_bull()