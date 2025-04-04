class Pos():
    def __init__(self, l ,c):
        self.l = l
        self.c = c 
        
    def __str__(self):
        return f"({self.l}, {self.c})"
    
    def add(self, lin, col):
        return Pos(self.l + lin, self.c + col)

def matrix_sum(A, B, pa = Pos(0,0), pb = Pos(0, 0), n = 0):
    if not n:
        n = len(A)
    C = [[0] * n for _ in range(n)]
    
    def matrix_sum_recursive(pos_a: Pos, pos_b: Pos, pos_c: Pos, size: int):
        if size == 1:
            C[pos_c.l][pos_c.c] = A[pos_a.l][pos_a.c] + B[pos_b.l][pos_b.c]
            return
        
        half = size // 2
        matrix_sum_recursive(pos_a, pos_b, pos_c, half)
        matrix_sum_recursive(pos_a.add(0, half), pos_b.add(0, half), pos_c.add(0, half), half)
        matrix_sum_recursive(pos_a.add(half, 0), pos_b.add(half, 0), pos_c.add(half, 0), half)
        matrix_sum_recursive(pos_a.add(half, half), pos_b.add(half, half), pos_c.add(half, half), half)
    
    matrix_sum_recursive(pa, pb, Pos(0, 0), n)
    return C 

def matrix_sub(A, B, pa = Pos(0,0), pb = Pos(0, 0), n = 0):
    if not n:
        n = len(A)
    C = [[0] * n for _ in range(n)]
    
    def matrix_sub_recursive(pos_a: Pos, pos_b: Pos, pos_c: Pos, size: int):
        if size == 1:
            C[pos_c.l][pos_c.c] = A[pos_a.l][pos_a.c] - B[pos_b.l][pos_b.c]
            return
        
        half = size // 2
        matrix_sub_recursive(pos_a, pos_b, pos_c, half)
        matrix_sub_recursive(pos_a.add(0, half), pos_b.add(0, half), pos_c.add(0, half), half)
        matrix_sub_recursive(pos_a.add(half, 0), pos_b.add(half, 0), pos_c.add(half, 0), half)
        matrix_sub_recursive(pos_a.add(half, half), pos_b.add(half, half), pos_c.add(half, half), half)
    
    matrix_sub_recursive(pa, pb, Pos(0, 0), n)
    return C 

def matrix_sum_byReference(A, C, pos_a: Pos, pos_c: Pos, size: int):
    if size == 1:
        C[pos_c.l][pos_c.c] += A[pos_a.l][pos_a.c] 
        return
    
    half = size // 2
    matrix_sum_byReference(A, C, pos_a,  pos_c, half)
    matrix_sum_byReference(A, C, pos_a.add(0, half),  pos_c.add(0, half), half)
    matrix_sum_byReference(A, C, pos_a.add(half, 0),  pos_c.add(half, 0), half)
    matrix_sum_byReference(A, C, pos_a.add(half, half), pos_c.add(half, half), half)


def matrix_sub_byReference(A, C, pos_a: Pos, pos_c: Pos, size: int):
    if size == 1:
        C[pos_c.l][pos_c.c] -= A[pos_a.l][pos_a.c]
        return
    
    half = size // 2
    matrix_sub_byReference(A, C, pos_a, pos_c, half)
    matrix_sub_byReference(A, C, pos_a.add(0, half), pos_c.add(0, half), half)
    matrix_sub_byReference(A, C, pos_a.add(half, 0),  pos_c.add(half, 0), half)
    matrix_sub_byReference(A, C, pos_a.add(half, half), pos_c.add(half, half), half)


def strassen_recursive(A, B, C, pos_a: Pos, pos_b: Pos, pos_c: Pos, n: int):
    if n == 1:
        C[pos_c.l][pos_c.c] += A[pos_a.l][pos_a.c] * B[pos_b.l][pos_b.c]
        return

    half = n // 2
    a11 = pos_a
    a12 = pos_a.add(0, half)
    a21 = pos_a.add(half, 0)
    a22 = pos_a.add(half, half)
    
    b11 = pos_b
    b12 = pos_b.add(0, half)
    b21 = pos_b.add(half, 0)
    b22 = pos_b.add(half, half)
    
    c11 = pos_c
    c12 = pos_c.add(0, half)
    c21 = pos_c.add(half, 0)
    c22 = pos_c.add(half, half)
    
    s1 = matrix_sub(B, B, b12, b22, half)
    s2 = matrix_sum(A, A, a11, a12, half)
    s3 = matrix_sum(A, A, a21, a22, half)
    s4 = matrix_sub(B, B, b21, b11, half)
    s5 = matrix_sum(A, A, a11, a22, half)
    s6 = matrix_sum(B, B, b11, b22, half)
    s7 = matrix_sub(A, A, a12, a22, half)
    s8 = matrix_sum(B, B, b21, b22, half)
    s9 = matrix_sub(A, A, a11, a21, half)
    s10 = matrix_sum(B, B, b11, b12, half)
    
    p1 = [[0] * half for _ in range(half)]
    strassen_recursive(A, s1, p1, a11, Pos(0,0), Pos(0,0), half)
    
    p2 = [[0] * half for _ in range(half)]
    strassen_recursive(s2, B, p2, Pos(0,0), b22, Pos(0,0), half)
    
    p3 = [[0] * half for _ in range(half)]
    strassen_recursive(s3, B, p3, Pos(0,0), b11, Pos(0,0), half)
    
    p4 = [[0] * half for _ in range(half)]
    strassen_recursive(A, s4, p4, a22, Pos(0,0), Pos(0,0), half)
    
    p5 = [[0] * half for _ in range(half)]
    strassen_recursive(s5, s6, p5, Pos(0,0), Pos(0,0), Pos(0,0), half)
    
    p6 = [[0] * half for _ in range(half)]
    strassen_recursive(s7, s8, p6, Pos(0,0), Pos(0,0), Pos(0,0), half)
    
    p7 = [[0] * half for _ in range(half)]
    strassen_recursive(s9, s10, p7, Pos(0,0), Pos(0,0), Pos(0,0), half)
    
    
    #c11 = c11 + p5 + p4 - p2 + p6
    matrix_sum_byReference(p5, C, Pos(0,0), c11, half)
    matrix_sum_byReference(p4, C, Pos(0,0), c11, half)
    matrix_sub_byReference(p2, C, Pos(0,0), c11, half)
    matrix_sum_byReference(p6, C, Pos(0,0), c11, half)
    
    #c12 = c12 + p1 + p2
    matrix_sum_byReference(p1, C, Pos(0,0), c12, half)
    matrix_sum_byReference(p2, C, Pos(0,0), c12, half)
    
    #c21 = c21 + p3 + p4
    matrix_sum_byReference(p3, C, Pos(0,0), c21, half)
    matrix_sum_byReference(p4, C, Pos(0,0), c21, half)
    
    #c22 = c22 + p5 + p1 - p3 - p7
    matrix_sum_byReference(p5, C, Pos(0,0), c22, half)
    matrix_sum_byReference(p1, C, Pos(0,0), c22, half)
    matrix_sub_byReference(p3, C, Pos(0,0), c22, half)
    matrix_sub_byReference(p7, C, Pos(0,0), c22, half)
    

def matrix_multiply_strassen(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]  
    strassen_recursive(A, B, C, Pos(0, 0), Pos(0, 0), Pos(0, 0), n)
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
    [8, 7, 2, 9],
    [4, 3, 3 , 15]
]
print(matrix_multiply_strassen(A, B))
