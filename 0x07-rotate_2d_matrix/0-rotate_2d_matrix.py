# Rotating a 2d matrix 90 degrees
def rotate_2d_matrix(matrix):
    n = len(matrix)

    #transpose the matrix
    for i in range(n):
        for j in range(i,n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    #reverse each column
    for i in range(n):
        for j in range (int(n/2)):
            temp = matrix[n-j-1][i]
            matrix[n-j-1][i] = matrix[j][i]
            matrix[j][i] = temp
    
#driver program
