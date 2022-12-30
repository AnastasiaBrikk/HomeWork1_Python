# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

print('Inpur a number of day in week')
day = int(input())
if day < 1 or day > 7:
    print('Incorrect number!')
else:
    print(day<6)
