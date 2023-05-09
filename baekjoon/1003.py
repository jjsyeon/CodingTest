T = int(input())

def fibonacci(n):
    if n < 2 : return n
    val_list = [1,1]
    for i in range(n-2):
        val_list.append(val_list[i]+ val_list[i+1])
    return val_list[-1]

for test_case in range(T):
    value = int(input())

    if value == 0: print(1,0)
    elif value == 1: print(0,1)
    elif value == 2: print(1,1)
    else : print(fibonacci(value-1), fibonacci(value))
