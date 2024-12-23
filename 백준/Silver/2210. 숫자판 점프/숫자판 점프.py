arr = [input().split() for _ in range(5)]

def move(start, num):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    if len(num) == 6: 
        answer.add(num)
        return
    end = [(start[0]+dx[i], start[1]+dy[i]) for i in range(4) if 0<=start[0]+dx[i]<5 and 0<=start[1]+dy[i]<5]
    for next in end:
        x, y = next
        move(next, num+arr[x][y])

answer = set()
for x in range(5):
    for y in range(5):
        move((x,y), arr[x][y])

print(len(answer))