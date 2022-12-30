# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


print('Input a number og quart:')
quart = int(input())

if quart == 1:
    print('x: 0, +inf; y: 0, +inf')
elif quart == 2:
    print('x: -inf, 0; y: 0, +inf')
elif quart == 3:
    print('x: -inf, 0; y: -inf, 0')
elif quart == 4:
    print('x: 0, +inf; y: -inf, 0')
else:
    print('Incorrect number!')
