# Declaring a 2D array with 3 rows and 4 columns
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
#print(matrix[1][2])

for row in matrix:
    print(len(row))
    for element in row:
        print(element)
        

matrix[0][3] = 100  # Modifying the element in the first row and fourth column
new_row = [8,9,10,20]
matrix.append(new_row)
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()  # Move to the next line for the next row
    