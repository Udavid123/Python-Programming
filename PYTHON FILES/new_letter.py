name = input("What's your name: ")
print("GUESSING GAME")
print("Instructions:")
print("1. Guess a letter between 'a' and 'j'")
print("2. You can only guess three times")
secret_letter = 'c'
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = input("Guess: ")
    guess_count += 1
    if guess == secret_letter:
        print("You Won!")
        break

else:
    print("Sorry, You Failed")
