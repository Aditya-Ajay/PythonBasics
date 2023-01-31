# Palindrom number is a number in which the number is same from both left and
# right side


# def PalindromNumber(n) :
#     if(len(n) < 1) :
#         return "YES"


def countDigit(number):

    res = 0

    while (number > 0):
        number = number // 10
        res += 1

    return res


# def palindromeNumber(n):
#     n = str(n)
#     if (countDigit(int(n)) == 1):
#         return "YES IT IS A PALINDROME NUMBER"
#     if (countDigit(int(n)) > 1):
#         print(n, n[::-1])
#         if n == n[::-1]:
#             return "YES IT IS A PALINDROME NUMBER"

#         else:
#             return "NO IT IS NOT A PALINDROME NUMBER"


# number = int(input("ENTER A NUMBER"))


# print(palindromeNumber(number))


'''
A BETTER OPTIMIZED WAY TO FIND A PALINDROME NUMBER
'''


def isPal(n):
    rev = 0
    tem = n

    while tem != 0:
        ld = tem % 10
        rev = rev * 10 + ld
        tem = tem // 10
    return rev == n


print(isPal(222))
