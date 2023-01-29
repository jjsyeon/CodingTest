T=int(input())
answer = []
numbers=list(map(int,input().split()))
sort_numbers=sorted(set(numbers))
numbers_dict={i:num for num,i in enumerate(sort_numbers)}

for num in numbers:
    answer.append(str(numbers_dict[num]))
print(" ".join(answer))