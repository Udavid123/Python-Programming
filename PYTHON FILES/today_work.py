"""
name = input("what is your name? ")
print("GUESSING GAME")
print("1.YOU CAN ONLY CHOOSE A NUMBER BETWEEN 0 AND 9")
print("2. YOU CAN ONLY GUESS THREE 2 TIMES")
Secret_number = 0
guess_count = 0
guess_limit = 2
while guess_count < guess_limit:
    guess =int(input('guess: '))
    guess_count += 1
    if guess == Secret_number:
        print("you have pasted sucessfully")
        break
    else:
        print("you failed")
"""


command = ""
while True:
    command = input(">").lower()
    if command == "start":
        print("car started...")
    elif command == "stop":
        print("car stopped")
    elif command == "help":
        print("""
        start - to start the car.
        stop - to stop the car.
        quit - to quit.
        """)
    elif command == "quit":
        break
    else:
        print("I do not understand")            