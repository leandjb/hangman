from random import choice


def hangman(word):
    guessed_letters: str = ''
    tries: str = 3

    while tries > 0:
        blanks: int = 0

        print('Word:', end='')
        for letter in word:
            if letter in guessed_letters:
                print(letter, end='')
            else:
                print('_', end='')
                blanks += 1

        if blanks == 0:
            print("\nYou win!")
            break

        guess: str = input("|||>Enter a letter:")

        if guess in guessed_letters:
            print(
                f"You have already guessed this letter {guess}. Try with another one!")
            continue

        guessed_letters += guess

        if guess not in word:
            tries -= 1
            print(
                f"Sorry, '{guess}' is not in the word. You have {tries} tries left.")

            if tries == 0:
                print("You lose!")
                break


def run_game():
    word: str = choice(["python", "java", "kotlin", "javascript"])

    username: str = input("|||>Enter your name:")
    print(f"Welcome to Hang-man, {username}!")
    print("> Guess the next programming language:", end="\n\n")
    hangman(word)


if __name__ == "__main__":
    run_game()
