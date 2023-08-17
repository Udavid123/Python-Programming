"""
matrix = [
    [1, 2, 3] ,
    [4, 5, 6] ,
    [7, 8, 9] 
]
matrix[0][1] = 50
print(matrix)
"""


matrix = [
    [1, 2, 3] ,
    [4, 5, 6] ,
    [7, 8, 9] 
]
for row in matrix:
    for items in row:
        print(items)