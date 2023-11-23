import random

random_number = random.randint(1,3)

choices = {"r": "rock",
           "p": "paper",
           "s": "scissors"}#["r","p","s"]

print("Welcome! This is a rock paper scissors game")
print("input options are:")
print("     R: Rock")
print("     P: Paper")
print("     S: Scissors")
print("     A: (to restart the game)")
print("     Q: (To quit tha game)")
user_score=0
computer_score = 0

possible_inputs = {"r","p","s","a","q"}
while True:
    #computer_choice = random.choice(choices)
    random_key, random_value = random.choice(list(choices.items()))
    computer_choice = random_key
    user_input = input("Pick a choice of (r)ock,(p)aper,(s)cissors: ").lower()
    if user_input in possible_inputs:
        if user_input == "a":
            restart= input("You really want to restart the game?(yes/no) ").lower()
            if restart == "yes":
                print("The game is restarted")
                user_score=0
                computer_score = 0
                continue
            else:
              continue
        elif user_input == "q":
            print("Thank you for playing the game.")
            print("Final Score:     Computer score",computer_score,"-",user_score,"User score.")
            break
        else:
            print("Computer picked",random_value + ".")
            if user_input == computer_choice:
                print("Draw!    Computer score",computer_score,"-",user_score,"User score.")
                continue
            if (user_input == "r" and computer_choice =="s") or (user_input == "s" and computer_choice =="p") or (user_input == "p" and computer_choice =="r"):
                user_score+=1
                print("User win! Computer score",computer_score,"-",user_score,"User score.")
                continue            
            if (user_input == "r" and computer_choice =="p") or (user_input == "p" and computer_choice =="s") or (user_input == "s" and computer_choice =="r"):
                computer_score+=1
                print("Computer win! Computer score",computer_score,"-",user_score,"User score.")
                continue


    else:
        print("incorrect input, choose again")

quit()