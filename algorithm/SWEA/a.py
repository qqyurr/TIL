N = 5
b = 'a'


for j in range(N):
    if j >= 3:
        j = 4 - j

    print(' '*(j) + b*(5-2*j) + ' '*(j))


print('-------------------------------')

for i in range(1,N+1):
    if i >= 4:
        i = 6 - i

    print(' '*(3-i) + b*(i*2-1) + ' '*(3-i))

print('-------------------------------')

for j in range(N):
    if j < 2:
        print(b * (j + 1) + ' ' * (5 - 2 * (j + 1)) + b * (j + 1))
    if j == 2:
        print(b*5)
    elif j > 2:
        j = 4 - j
        print( b * (j+1) + ' '* (5 - 2 * (j+1)) + b*(j+1))
