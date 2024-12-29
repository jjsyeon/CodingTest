n = int(input())

arr = sorted([input() for _ in range(n)],key=lambda x: [len(x), 
                                                        sum([int(w) for w in x if '0'<w<='9']),
                                                        x])

print('\n'.join(arr))