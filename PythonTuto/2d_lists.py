# define a matrix 2d
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# access item on list and update it
matrix[0][1] = 20
print(matrix[0][1])

# map on matrix
for row in matrix:
    for col in row:
        print(col)