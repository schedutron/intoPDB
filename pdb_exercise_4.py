import sys

def magic(x, y):
    return x + y * 2

x = sys.argv[1]
y = sys.argv[1]

answer = magic(x, y)
print('The answer is: {}'.format(answer))
