print("GUESS THE CARTOON CHARACTER !!!!")
print("Solve the first quESTION to get the first clue ;)")
Quiz1 = input("Which is the largest continent: ")
if Quiz1 == "Asia" or Quiz1 == "asia" :
    print("Right answer\nHere is your first clue\nclue 1:He can travel through time with a time machine.")
    secret_word = "Doraemon"
    your_guess = "" 
    guess_count = 0
    guess_limit = 2
    out_of_guesses = False

    while your_guess != secret_word and not out_of_guesses:
        if guess_count < guess_limit:
            your_guess = input("Guess the word: ")
            guess_count += 1
            if your_guess == secret_word:
                print("Yay!! You won")
        else:
            out_of_guesses = True

    if out_of_guesses:
        print("You are out of guesses")
        clue2 = input("Do you want another clue Yes / No: ")
        if clue2 == "Yes":
            print("Then here is another question!")
            clue3 = input("What shape has three sides: ")
            if clue3 == "Triangle" or clue3== "triangle":
                print("Right answer\nHere is your second clue\nclue 2:He loves eating dorayaki  ")
                secret_word = "Doraemon"
                your_guess = "" 
                guess_count = 0
                guess_limit = 2
                out_of_guesses = False

                while your_guess != secret_word and not out_of_guesses:
                    if guess_count < guess_limit:
                        your_guess = input("Guess the word: ")
                        guess_count += 1
                        if your_guess == secret_word:
                            print("Yay!! You won")
                    else:
                        out_of_guesses = True

                if out_of_guesses:
                    print("You are out of guesses")
                    clue4 = input("Do you want another clue Yes / No: ")
                    if clue4 == "Yes":
                        print("Then here is another question!")
                        clue5 = input("What is the square root of 64: ")
                        if clue5 == "8":
                            print("Right answer\nHere is your third clue\nclue 3:He is a blue robot cat from the future.")
                            secret_word = "Doraemon"
                            your_guess = "" 
                            guess_count = 0
                            guess_limit = 2
                            out_of_guesses = False

                            while your_guess != secret_word and not out_of_guesses:
                                if guess_count < guess_limit:
                                    your_guess = input("Guess the word: ")
                                    guess_count += 1
                                    if your_guess == secret_word:
                                        print("Yay!! You won")
                                else:
                                    out_of_guesses = True
                        else:
                            print("Sorry, that's not correct.")
                    else:
                        print("You lose!")
            else:
                print("You lose!")
else:
    print("Oops, Try again!!")

