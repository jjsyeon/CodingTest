N = int(input())
times = list(map(int, input().split())).sort(reverse=True)

times.sort(reverse=True)
result = sum([(i+1) * times[i] for i in range(len(times))])
print(result)
