
name = input("what is your name? ")
print("GUESS GAME")
print("INTRUCTIONS")
print('1. you can only guess between the number o to 9.')
print('2. you can only guess three times.')
secret_number = 7
guess_count = 0
guess_limit = 2
while guess_count < guess_limit:
    guess = int(input('guess: '))
    guess_count += 1
    if guess == secret_number:
        print("you pasted!")
        break
    else:
        print("sorry you failed!")    


"""
command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("car started...")
    elif command == "stop":
        print("car stopped")
    elif command == "help":
        print(
        start - to start the car
        stop - to stop the car 
        quit - to quit
       )
    elif command == "quit":
        break
    else:
        print(" I do not understand.")            
"""