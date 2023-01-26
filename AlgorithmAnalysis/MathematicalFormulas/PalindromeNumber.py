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


def palindromeNumber(n):
    n = str(n)
    if (countDigit(int(n)) == 1):
        return "YES IT IS A PALINDROME NUMBER"
    if (countDigit(int(n)) > 1):
        print(n, n[::-1])
        if n == n[::-1]:
            return "YES IT IS A PALINDROME NUMBER"

        else:
            return "NO IT IS NOT A PALINDROME NUMBER"


number = int(input("ENTER A NUMBER"))
print(palindromeNumber(number))
