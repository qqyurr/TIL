def itoa(num):
    x = num
    y = 0
    arr = []
    while x:
        y = x % 10
        x //= 10
        arr.append(chr(y + ord('0')))
    arr.reverse()
    str = ''.join(arr)
    return str

x = 123
print(x, type(x))
str = itoa(x)
print(str, type(str))