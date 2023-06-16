string = input("Enter a string: ")
count = 0

for char in string:
    if char != ' ':
        count +=1

print("Number of characters (excluding spaces) in the string:", count)