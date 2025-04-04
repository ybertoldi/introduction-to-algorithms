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

def leastDivisor(x):
    for i in range(2, x+1):
        if x % i == 0:
            return i
        
    return x

def multiply(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    
    def matrix_multiply_recursive(pos_a: Pos, pos_b: Pos, pos_c: Pos, n: int):
        if n == 1:
            C[pos_c.l][pos_c.c] += A[pos_a.l][pos_a.c] * B[pos_b.l][pos_b.c]
            return
        
        d = leastDivisor(n)
        newN = n // d
        
        for l in range(d):
            for c in range(d):
                for k in range(d):
                    n_a = pos_a.addLine_Col(l * newN, k * newN)
                    n_b = pos_b.addLine_Col(k * newN, c * newN)
                    n_c = pos_c.addLine_Col(l * newN, c * newN)
                    matrix_multiply_recursive(n_a, n_b, n_c, newN)
                    
    
    matrix_multiply_recursive(Pos(0, 0), Pos(0, 0), Pos(0, 0), n)
    return C 

A = [
    [1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12],
    [13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24],
    [25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36]
]
B = [
    [36, 35, 34, 33, 32, 31],
    [30, 29, 28, 27, 26, 25],
    [24, 23, 22, 21, 20, 19],
    [18, 17, 16, 15, 14, 13],
    [12, 11, 10, 9, 8, 7],
    [6, 5, 4, 3, 2, 1]
]

print(multiply(A, B))
print(range(2,4)[1])