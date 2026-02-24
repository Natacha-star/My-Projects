# Create two 2x2 matrices
matrix_A = [[1, 2], [3, 4]]
matrix_B = [[5, 6], [7, 8]]

# Initialize a 2x2 matrix for the result with zeros
result = [[0, 0], [0, 0]]


# Addition logic
for i in range(2):        # Loop through rows
    for j in range(2):    # Loop through columns
        result[i][j] = matrix_A[i][j] + matrix_B[i][j]
        if result[i][j] > 10:
            result[i][j] = 10

# Display result
print("Resulting Matrix:")
for row in result:
    print(row)
for row in result:
    
    print(row)
