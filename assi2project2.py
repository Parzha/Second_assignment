import random


game_choices = ["paper","rock","scissors"]
print("Welcome to rock paper scissors We are going to play for 5 rounds and after that we decide the winner ")



round_counter=0
draw_counter=0
win_counter=0
lose_counter=0

while(round_counter<5):
    print("Round", round_counter+1)
    print("choose one (paper/rock/scissors) ")
    user_choice = input().lower()

    if user_choice == "paper" or user_choice == "rock" or user_choice == "scissors":

            generated_answer = random.choice(game_choices)
            print("computers answer= ", generated_answer)

            if user_choice == generated_answer:
              draw_counter += 1
              round_counter += 1
              print("it's draw")

            elif (user_choice == "scissors" and generated_answer == "paper") or (user_choice == "paper" and generated_answer == "rock") or (user_choice == "rock" and generated_answer == "scissors"):

               win_counter += 1
               round_counter += 1
               print("you won")

            else:
               lose_counter += 1
               round_counter += 1
               print("you lost")

    else:
        print("Invalid input try again")

print("there goes the results on the match--> WIN=", win_counter, " DRAW=", draw_counter, " LOSE=",
                  lose_counter)
if (win_counter > lose_counter):
     print("congrats you won")
elif (lose_counter > win_counter):
     print("You lost better luck next time ")
else:
    print("IT DRAWWWWWWW")




