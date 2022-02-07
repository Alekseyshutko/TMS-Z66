from math import sin, cos, log, log10, tan


def isfloat(value):     # function for determining the validity of a number
    try:
        float(value)
        return True
    except ValueError:
        return False


t = 0
while True:
    sk = input('if arithmetic then type "A" if other then "L" ')
    if sk == 'A':
        while True:
            a, b, c = map(str, input('Enter number ').split())
            if isfloat(a) and isfloat(c) and b in "+-*/":
                break
            else:
                print('It is not a number. Please enter number')
                continue

        a = float(a)
        c = float(c)
        if b == '+':
            print(a + c)
        elif b == '-':
            print(a - c)
        elif b == '*':
            print(a * c)
        elif b == '/':
            if c == '0':
                print("Can't divide by zero. Please enter another number")
                k = float(input())
                print(a / k)
            else:
                print(a / c)
    else:
        while True:
            d, e = map(str, input().split())
            if isfloat(e):
                break
            else:
                print('It is not a number. Please enter number')
        e = float(e)
        if d == "cos":
            print(cos(e))
        elif d == "log":
            print(log(e))
        elif d == 'sin':
            print(sin(e))
        elif d == 'log10':
            print(log10(e))
        elif d == 'tan':
            print(tan(e))
    k = input("Do you still want to enter a calculation?  ").lower()
    if k == "yes":
        continue
    else:
        break