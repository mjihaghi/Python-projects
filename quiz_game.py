print("Hi! let us play a game!")

correct_answer = 0
while (correct_answer !=1):
    Playing = input("Be aware!! This is a very addicting game are you sure you want to continue(Yes/No)??: ")
    correct_answers = {"Yes","No"}
    #if Playing not in correct_answers:
    if ((Playing != "Yes") and (Playing != "No")):
        print("Hi")
        print(type(Playing))
    else:
        correct_answer = 1

if Playing == "No":
    print("Such a shame! You lost the chance of playing the best game in the world!!")
    quit()