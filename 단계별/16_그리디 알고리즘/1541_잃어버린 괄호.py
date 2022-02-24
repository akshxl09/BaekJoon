string = input()

tmp = []
num = []
operator = ['+']
for i in string:
    if i.isdigit():
        tmp.append(i)
    else:
        operator.append(i)
        num.append(int(''.join(tmp)))
        tmp = []
num.append(int(''.join(tmp)))

flag = False
plus = 0
minus = 0
for i, letter in enumerate(operator):
    if flag:
        if letter == '-':
            flag = False
        else:
            minus += num[i]
    else:
        if letter == '+':
            plus += num[i]

    if letter == '-':
        flag = True
        minus += num[i]
    

print(plus - minus)

        