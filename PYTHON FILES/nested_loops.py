"""
for x in range (4):
    print(x)


for x in range (4):
    for y in range (3):
        print(f"({x} , {y})")


number = [5,1,5,1,1,]
for x_count in number:
    print("x" * x_count)

    

for x in range (1, 13, 1):
    for y in range (1, 13, 1):
        print(x * y, end='\t')
    print()
"""


number = int(input("Enter a number: "))
limit = int(input("enter a limit: "))

sum_of_multiples = 0
for i in range(1, limit + 1):
    if i %number == 0:
        sum_of_multiples += i
print(f"The sum of multiples of {number} up to {limit} is: {sum_of_multiples}")


