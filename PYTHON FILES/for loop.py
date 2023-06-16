"""
for items in 'python':
    print(items)


for words in ['john', 'james', 'paul']:
    print(words)""



limit = int(input("what is the limit? "))

for num in range (3, limit +1, 3):
    print(num)


for item in range (10+1):
    print(item)

for number in range (5,10):
    print(number)
"""

prices = [10, 20, 30,]
total = 0

for price in prices:
    total = total + price
    print(f"Total = {total}")