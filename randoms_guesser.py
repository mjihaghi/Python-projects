import random

print("Hi you are going to guess a number between 1-10")
print("You have 5 chances to guess it unless you will lose")

random_number = random.randint(1,10)


number_of_guesses = 5

while number_of_guesses > 0 :
    user_number = input("Guess the number between 1-10: ")
    if user_number.isnumeric():
        user_number = int(user_number)
        if user_number in range(1,10):
            if user_number == random_number:
                print("YAAAYYY you guessed it right!!!")
                quit()
            else:
                print("Wrong guess! You are " +  str(abs(random_number - user_number)) + " digits away")
                number_of_guesses -=1
                print("You have " + str(number_of_guesses) + " guesses left") 
        else:
            print("The number you guessed is not in the guess range")
            #print(user_number)
    else:
        print("Please insert a numeric value")

print("Too bad! the right number was " + str(random_number))
#print(int(user_number))