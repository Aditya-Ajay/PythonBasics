'''
TO COUNT THE DIGIT WHICH THE USERS HAS PASSED 
'''


def countDigit(number):

    res = 0

    while (number > 0):
        number = number // 10
        res += 1

    return res


number = int(input("ENTER A VALUE : "))

print(countDigit(number))


# TIME COMPLEXITY IS theta(n)
# as the iteration will increase as the input size increases
