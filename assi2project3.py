import random
#how_to_play
#you need pick front or back of your hand with another 2 people if ...
#you somehow get lucky and your hand is not like 2 other players you gonna win the game ezy as that .
another_game=1
while(another_game==1):

    print("Welcome to palam polom polich weird name right... :D")
    print("Lets start the game pick your move ... secretly ")
    print("For back of your hand type 1 / For front of your hand type 2 ")

    condi_loop=1

    while(condi_loop==1):

     user_input=int(input())

     if user_input == 1 or user_input == 2:
        computer_1=random.randint(1,3)
        computer_2=random.randint(1,3)

        if (user_input<computer_1 and user_input<computer_2) or (user_input>computer_1 and user_input>computer_2):
            print("You won congrats")
            condi_loop=0

        elif (computer_1<computer_2 and computer_1<user_input) or (computer_1>user_input and computer_1>computer_2):
            print("computer 1 won ... you lost that'sunlucky")
            condi_loop = 0

        elif (computer_2<computer_1 and computer_2<user_input) or (computer_2>user_input and computer_2>computer_1):
            print("computer 2 won .... you lost better luck next time")
            condi_loop = 0

        else:
            print("it's draw try again")

     else:
          print("invalid input try again")


    print("if you wanna play again type 1 ")
    another_game=int(input())


