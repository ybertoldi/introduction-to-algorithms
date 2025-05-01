class Pos():
    
    def __init__(self, l ,c):
        self.l = l
        self.c = c 
        
    def __str__(self):
        return f"({self.l}, {self.c})"
    
    def addLine(self, val):
        return Pos(self.l + val, self.c)
    
    def addCol(self, val):
        return Pos(self.l, self.c + val)
    
    def addLine_Col(self, lin, col):
        return Pos(self.l + lin, self.c + col)

def multiply(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    
    def matrix_multiply_recursive(pos_a: Pos, pos_b: Pos, pos_c: Pos, n: int):
        if n == 1:
            C[pos_c.l][pos_c.c] += A[pos_a.l][pos_a.c] * B[pos_b.l][pos_b.c]
            return
        
        newN = n // 2
        # c11 = a11 * b11 + a12 * b21
        matrix_multiply_recursive(pos_a, pos_b ,pos_c, newN)
        matrix_multiply_recursive(pos_a.addCol(newN), pos_b.addLine(newN), pos_c, newN)
        
        # c12 = a11 * b12 + a12 * b22
        matrix_multiply_recursive(pos_a, pos_b.addCol(newN), pos_c.addCol(newN), newN)
        matrix_multiply_recursive(pos_a.addCol(newN), pos_b.addLine_Col(newN,newN), pos_c.addCol(newN), newN)
        
        # c21 = a21 * b11 + a22 * b21
        matrix_multiply_recursive(pos_a.addLine(newN), pos_b, pos_c.addLine(newN), newN)
        matrix_multiply_recursive(pos_a.addLine_Col(newN,newN), pos_b.addLine(newN), pos_c.addLine(newN) , newN)
        
        # c22 = a21 * b12 + a22 * b22
        matrix_multiply_recursive(pos_a.addLine(newN), pos_b.addCol(newN), pos_c.addLine_Col(newN,newN), newN)
        matrix_multiply_recursive(pos_a.addLine_Col(newN,newN), pos_b.addLine_Col(newN,newN), pos_c.addLine_Col(newN,newN), newN)
        
    
    matrix_multiply_recursive(Pos(0, 0), Pos(0, 0), Pos(0, 0), n)
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

print(multiply(A, B))
