import random
import sys


def getstr(n):
    str = ''
    random.seed()
    for i in range(0, n):
        if random.randint(0, 1) == 1:
            str += '('
        else:
            str += ')'
    return str


def check(str, a, b):
    # ( - вверх
    # ) - вниз
    a -= 1
    level = 0
    if (a < b) and (len(str) > a) and (len(str) > b - 1):
        for i in range(a, b):
            if str[i] == '(':
                level += 1
            if str[i] == ')':
                level -= 1
            if level < 0:
                break
    if level != 0:
        return 'No'
    else:
        return 'Yes'


def restore(str):
    # ( - вверх
    # ) - вниз
    rstr = ''
    while len(rstr) != len(str):
        rstr += '*'
    while rstr.find('*')!=-1:
        a, b = map(int, input('? ').split())
        if check(str, a, b) == 'Yes':
            rstr = rstr[:a - 1] + '(' + rstr[a:]
            rstr = rstr[:b - 1] + ')' + rstr[b:]
        print(rstr)
        print(check(str, a, b))


def main():
    n = int(input('Ввдеите число скобок:'))
    str = getstr(n)
    while check(str, 1, len(str)) != 'Yes':
        str = getstr(n)
    print(str)
    restore(str)
    # print(check(str, 0, len(str) - 1))
    print()


main()
