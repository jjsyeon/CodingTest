s = input()
space = s.count(' ') + 1

if s[0] == ' ': space -= 1
if s[len(s)-1] == ' ': space -= 1
print(space)
