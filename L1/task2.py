def check(value, base):
    counter = 0;
    while value > 0 and base > 1:
        if value % base != 0:
            break;
        else:
            counter += 1
        value /= base
    return counter

n = int(input())
bases = [int(n) for n in input().split()]
zeros = [int(n) for n in input().split()]
#bases = list(map(int, input().split()))
#zeros = list(map(int, input().split()))
res = 1
flag = 0
while flag != 1:
    counter = 0
    for i in range(0, len(bases)):
        if check(res, int(bases[i])) >= int(zeros[i]):
            counter += 1
    if counter == len(bases):
        break;
    res += 1

print(res)

