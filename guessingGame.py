secret_word = "Infinite"
guessing_word = ""
limit_count = 3
guess_count = 0
out_of_guess = False

while guessing_word != secret_word and not out_of_guess:
    if guess_count < limit_count:
        if guess_count == 0:
            print("Its a Kpop Group")
            guessing_word = input("Enter word: ")

        elif guess_count == 1:
            print("Boy Group Debuted in 2010")
            guessing_word = input("Enter word: ")
        elif guess_count == 2:
            print("Group of 7 people, Known for their knife like sharp dance moves")
            guessing_word = input("Enter word: ")
        guess_count += 1

    else:
        out_of_guess = True

if not out_of_guess:
    print("You win")
else:
    print("You loose")
