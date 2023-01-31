def prime(number):
    if (number == 1):
        print("IT IS NOT A PRIME")

    count = 0
    for i in range(1, number + 1):
        if (number % i == 0):
            count += 1
    if (count > 2):
        print("IT IS NOT A PRIME NUMBER")
    else:
        print('IT IS A PRIME NUMBER')


prime(17)


'''
TIME COMPLEXITY WILL BE 0(n)
'''


def isPrime(number):
    if (number == 1):
        return False

    for i in range(2, number):

        if (number % i == 0):
            return False
    return True
