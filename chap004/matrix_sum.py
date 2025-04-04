class Pos():
    def __init__(self, l ,c):
        self.l = l
        self.c = c 
        
    def __str__(self):
        return f"({self.l}, {self.c})"
    
    def add(self, lin, col):
        return Pos(self.l + lin, self.c + col)

def soma(A, B):
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
    
    matrix_sum_recursive(Pos(0, 0), Pos(0, 0), Pos(0, 0), n)
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
print(soma(A, B))
