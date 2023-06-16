"""
i = 1

while i <= 5:
    print(i)
    i = i + 1
print("done")    


    
n = 2
 
while n <= 20:
    print(n)
    n = n + 2
print("done")    



x = 3

while x <= 30:
    print(x)
    x = x  3
print ("done")    



h = 4
while h <= 40:
    print(h)
    h = h + 4
print("done")    



g = 5

while g <= 50:
    print(g)
    g = g + 5
print("done")    



j = 6

while j <= 60:
    print(j)
    j = j + 6
print("done")    



r = 7

while r <= 70:
    print(r)
    r = r + 7
print("done")    



e = 8

while e <= 80:
    print(e)
    e = e + 8
print("done")    



d = 9

while d <= 90:
    print(d)
    d = d + 9
print("done")



a = 10

while a <= 100:
    print(a)
    a = a + 10
print("done")    



i = 1
while i <= 5:
    print("*" * i)
    i = i + 1
print("done")       



name = input("What is your name? ")
print("GUESS GAME")
print("Instructions:")
print('1. Guess a number between 0 and 9')
print('2. You can guess only three times')
secret_number = 3
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('guess: '))
    guess_count += 1
    if guess == secret_number:
        print("you are a star winner!")
        break
else:
    print("sorry, you failed!")
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
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("i'm sorry i don't understand")            