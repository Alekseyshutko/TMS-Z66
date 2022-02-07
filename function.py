def validity(day, month, year):
    sp_1 = [4, 6, 9, 11]
    # checking for a high-grade year
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        year_v = 1
    else:
        year_v = 0
    if day > 31 or month > 12 or year < 0:
        return "Wrong date"
    elif year_v == 0 and month == 2 and day == 29:
        return "Wrong date"
    elif month in sp_1 and day == 31:
        return "Wrong date"
    else:
        return "Great"


def line_length(line):  # calculating the length of a string
    letters_numbers = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789"
    sys1 = " #$%&\'()*+,-./:;?@[\\]^_`{|}~ "
    lgy = 0
    for i in line.lower():
        if i in letters_numbers or i in sys1:
            lgy += 1
    return lgy


def number_divisors(number):
    sp = []
    for i in range(1, number + 1):
        if number % i == 0:
            sp.append(i)
    return sp


def element_line(element, a):
    i = 0
    a = str(a)
    element = str(element)
    while True:
        if element == a[i]:
            k = 1
            break
        else:
            k = 0
            break
        i += 1
    return True if k == 1 else False


def fib_rec(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib_rec(n - 1) + fib_rec(n - 2)


def simple_rec(n, k=None):
    if k is None:
        k = n - 1
    while k > 2:
        if n % k == 0:
            return False
        else:
            return simple_rec(n, k - 1)
    else:
        return True


def range_m(*n):
    n = list(n)
    sp = []
    if len(n) == 1:
        start = 0
        stop = n[0]
        step = 1
    elif len(n) == 2:
        start = n[0]
        stop = n[1]
        step = 1
    elif len(n) == 3:
        start = n[0]
        stop = n[1]
        step = n[2]
    sp.append(n[0])
    while n[0] < n[1] - n[2]:
        sp.append(n[0] + n[2])
        n[0] = n[0] + n[2]
    return sp


u = list(map(int, input().split()))
print(*range_m(u))
