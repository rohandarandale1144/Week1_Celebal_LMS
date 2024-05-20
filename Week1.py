# #Lower Triangular Pattern
def lower_triangular(n):
    for i in range(n):
        for j in range(n):
            if j <= i:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

n = 5
lower_triangular(n)


#Upper Triangular Pattern
def upper_triangular(n):
    for i in range(n):
        for j in range(n):
            if j >= i:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

n = 5
upper_triangular(n)


#Pyramid Pattern
def pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))

n = 5
pyramid(n)