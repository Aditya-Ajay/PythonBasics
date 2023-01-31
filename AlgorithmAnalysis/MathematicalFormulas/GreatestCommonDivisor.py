'''
TO FIND THE GREATEST COMMOM DIVISOR
eg greatest common divisor between 6 and 15 is 3

'''


def greatestCommonDivisor(num1, num2):
    for i in range(min(num1, num2), 0, -1):
        if (num1 % i == 0) and (num2 % i == 0):
            print(i)
            break


# greatestCommonDivisor(12, 15)


def greatestCommonDiv(num1, num2):
    i = min(num1, num2)
    while (i >= 0):
        if (num1 % i == 0) and (num2 % i == 0):
            print(i)
            break
        i -= 1
        print(i)


greatestCommonDiv(12, 15)
