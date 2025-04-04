def matrix_multiply_strassen(A,B):    
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    half = n // 2
    A11, A12, A21, A22 = split_matrix(A, half)
    B11, B12, B21, B22 = split_matrix(B, half)
    S1 = matrix_sub(B12, B22)
    S2 = matrix_sum(A11, A12)
    S3 = matrix_sum(A21, A22)
    S4 = matrix_sub(B21, B11)
    S5 = matrix_sum(A11, A22)
    S6 = matrix_sum(B11, B22)
    S7 = matrix_sub(A12, A22)
    S8 = matrix_sum(B21, B22)
    S9 = matrix_sub(A11, A21)
    S10 = matrix_sum(B11, B12)
    
    P1 = matrix_multiply_strassen(A11, S1)
    P2 = matrix_multiply_strassen(S2, B22)
    P3 = matrix_multiply_strassen(S3, B11)
    P4 = matrix_multiply_strassen(A22, S4)
    P5 = matrix_multiply_strassen(S5, S6)
    P6 = matrix_multiply_strassen(S7, S8)
    P7 = matrix_multiply_strassen(S9, S10)
    
    C11 = matrix_sum(matrix_sub(matrix_sum(P5, P4), P2), P6)
    C12 = matrix_sum(P1, P2)
    C21 = matrix_sum(P3, P4)
    C22 = matrix_sub(matrix_sub(matrix_sum(P5, P1), P3), P7)
    
    return combine_matrices(C11, C12, C21, C22)

def split_matrix(M, h):
    M11 = [row[:h] for row in M[:h]]
    M12 = [row[h:] for row in M[:h]]
    M21 = [row[:h] for row in M[h:]]
    M22 = [row[h:] for row in M[h:]]
    return (M11, M12, M21, M22)

def combine_matrices(M11, M12, M21, M22):
    n = len(M11) * 2
    M = [[0] * n for _ in range(n)]
    half = n // 2
    
    for i in range(half):
        for j in range(half):
            M[i][j] = M11[i][j]
            M[i][j+half] = M12[i][j]
            M[i+half][j] = M21[i][j]
            M[i+half][j+half] = M22[i][j]
    return M

def matrix_sum(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    
    return C

def matrix_sub(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C

A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
B = [
    [16, 15, 14, 13],
    [12, 11, 10, 9],
    [8, 7, 6, 5],
    [4, 3, 2, 1]
]

r = matrix_multiply_strassen(A, B)
for row in r:
    print(row)