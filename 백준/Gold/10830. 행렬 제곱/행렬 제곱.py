import sys
input = sys.stdin.readline

A, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(A)]

def pow_matrix(cnt):
    if cnt == 1 : return [[matrix[i][j] % 1000 for j in range(A)] for i in range(A)]
    elif cnt == 2 : 
        return mul_matrix(matrix, matrix)
    else:
        new_ = pow_matrix(cnt//2)
        return mul_matrix(matrix, mul_matrix(new_, new_)) if cnt % 2 else mul_matrix(new_,new_)
    
def mul_matrix(m1, m2):
    return [[sum([m1[i][k] * m2[k][j] for k in range(A)])%1000 for j in range(A)] for i in range(A)]

for arr in pow_matrix(B) : print(*arr)