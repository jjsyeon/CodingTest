def reverse_num(num):
    str_num = str(num)
    result = ''
    for i in range(len(str_num)):
        result += str_num[len(str_num)-1-i]
    return int(result)

num1, num2 = map(int, input().split())
if len(str(num1)) != len(str(num2)):
    if num1 > num2:
        print(reverse_num(num1))
    else:
        print(reverse_num(num2))
else:
    num1 = reverse_num(num1)
    num2 = reverse_num(num2)
    if num1 > num2:
        print(num1)
    else:
        print(num2)
