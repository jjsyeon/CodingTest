T = int(input())
answer = 0
for test_case in range(T):
    text = input()
    words = set(text)
    group = True
    for word in words:
        num = text.count(word)
        if text.find(word*num) == -1:
            group = False
            break
    if group: answer+=1
        
print(answer)