import sys
input = sys.stdin.readline

N = int(input())
B = [list(map(int, input().split())) for _ in range(N)]
w_cnt, b_cnt = 0,0

def split_paper(x,y,n):
    global w_cnt, b_cnt
    tmp_cnt = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if B[i][j]: tmp_cnt += 1
    
    if tmp_cnt == 0: # 1이 하나도 없음. 하얀색 색종이
        w_cnt += 1
    elif tmp_cnt == n ** 2: # 0이 하나도 없음. 검은색 색종이
        b_cnt += 1
    else:
        split_paper(x, y, n // 2)
        split_paper(x + n // 2, y, n // 2)
        split_paper(x, y + n // 2, n // 2)
        split_paper(x + n // 2, y + n // 2, n // 2)

split_paper(0,0,N)
print(w_cnt)
print(b_cnt)
