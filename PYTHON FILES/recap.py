"""
name = input("what is your name? ")
age =int (input("how old are you in words? "))
blood_group = input ("what is the name of your blood group? ")
address = input ("were do you live? ")
phone_number = int(input("what is your phone number"))
nationality = input ("which Country are you from? ")
print(f"The details of {name} is as follows: age {age};  blood_group  {blood_group};  natioiality  {nationality};  address  {address};  phone_number  {phone_number}")



#Arithmetic_opertions
print(2+5)
print(5-2)
print(2*5)
print(9/3)
print(8//3)
print(5%2)
print(10**3)



x = 10
x = x + 3
print(x)

x = 10
x += 3
print(x)

x = 10
x -= 3
print(x)


#MATH_FUNTIONS
x = 2.9
print(round (x))

x = 2.9
print(abs(x))



temperture = int(input("Input number: "))

if temperture  > 37:
    print("It's too hot!")
elif temperture < 37:
    print("It's too cold!")
else:
    print("It's warm!")    



has_good_more_than_250_in_jamb = True
has_5_credit_in_jamb = True

if has_good_more_than_250_in_jamb or has_5_credit_in_jamb:
    print("eligible for admission")
else:
    print("not eligible for admission")   



is_hot = False

if is_hot:
    print("it's hot day")
print("enjoy your day") 



price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price 
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")    
X

#WHILE LOOPS

i = 1
while i <= 5:
    print(i)
    i = i + 1
print("done")    


i = 1
while i <= 5:
    print("*" * i)
    i = i + 1
print("done")  


name = input("what is your name? ")
print("GUESSING GAME")
print("INTRUCTION")
print("1. You can only guess the number 0 to 9.")
print("2. You can only guess three times.")
secret_number = 0
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input(" guess number: "))
    guess_count += 1
    if guess == secret_number:
        print("YOU WON!")
        break
    else:
        print("sorry you failed!")


command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("car as started")
        else:
            started = True
            print("car started")
    elif command == "stop":
        if stopped:
            print("car stopped")
        else:
            stopped = True
            print("car stopped")
    elif command == "help":
        print(""
        start - to start the car
        stop- to stop the car
        quit - to quit
        )
    elif command == "quit":
        break
    else:
        print("I don't understand that!")                



#FOR_LOOPS

for items in 'python':
    print(items)


for items in ['John', 'James', 'paul']:
    print(items)
for items in [1,2,3]:
    print(items)  


# range

for item in range (10):
    print(item)


price = [10,20,30]
total = 0
for prices in price:
    total = total + prices
    print(f"Total:{total}")


#Nested_loops: is used to add one loop into  another loop.

for x in range (4):
    print(x)


for x in range(4):
    for y in range (3):
        print(f"({x} , {y})")


numbers = [5, 1, 5, 1, 1]
for x_count in numbers:
    print('x' * x_count)


#lists

names = ['Mary', 'Mark', 'Grace', 'Ben']
names[0] = 'may'
print(names)
"""

numbers = [3, 10, 2, 6, 8, 4]
max = numbers [0]
for number in numbers:
    if number > max:
        max = number
    elif number < max:
        number = max    
print(number)  
