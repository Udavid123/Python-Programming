"""
name = ['joe', 'mark', 'jude', 'zoe', 'max']
name [0] = "luke"
print(name)



numbers = [3, 10, 2, 6, 8, 4]
max = numbers [0]
for number in numbers:
    if number > max:
        max = number
    elif number < max:
        number = max    
print(number)  
"""
 
#Write a program to find the lowest number in a list

numbers = input("what is the postive integers? ")
lowest = numbers [0]
for number in numbers:
    if number > lowest:
        number = lowest
    elif number < lowest:
        lowest = number
print(lowest)            