n = int(input("Enter a positive integer: "))
sum = 0

for num in range(1, n+1):
    sum += num

print("The sum of numbers from 1 to", n, "is:", sum)