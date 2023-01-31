'''
WHAT IS A FACTORIAL 
So factorail of (5) is basically 
1*2*3*4*5

and factorial of 0 is 1
'''


def factorailNumber(n):
    str = 1

    for i in range(2, n+1):
        str *= i
    return str


# print(factorailNumber(0))


#  So this is the iteration approach
'''
in this case the complexity is 0(n) as more the number more the iteartion . 
And that to in a linear pattern 
'''


'''
TO OPTIMIZE THE FUNCTION WE CAN USE RECURSIVE APPROACH TOO 
IN THE CASE OF RECURSIVE APPROCAH WE NEED A BASE CASE 

if n ==0 it will return 1 
'''


def recursiveFact(n):

    if (n == 0):
        return 1

    return n * recursiveFact(n-1)


# print(recursiveFact(5))


def recursiveFact(n):

    if (n == 0):
        return 1

    return n * recursiveFact(n-1)


def trailingFactorial(n):
    a = recursiveFact(n)
    res = 0

    while a % 10 == 0:
        res += 1
        a = a // 10

    return res


'''

THIS SOLUTION IS CORRECT BUT IT WILL INCREASE A LOT OF LOAD
'''

# print(trailingFactorial(100))


'''
SO WE HAVE A BETTER APPROACH , 
If you  want to find the  trailing zeroes 

all we need to know how much combinations of 5 and 2 is there 

So , in case of factorial we can get to know about how much zeroes are there
by knowing how much 5 are there as 2's are always more amount then 5 

eg ==> if we see 

5! = 5 * 4 * 3 * 2 * 1  = 120 

so in this case zero is 1 

how can we find it with the approach which i have mentioned earlier . 

so in 5! the amount of 2's are 3 (2*1 , 2*2) and 5 is only 1 , so the zero will be only 
one . By this method we don't have to calculate the entire factorial , the only thing 

we are required to know is the amount of 5 we have . 
'''


def trailfac(number):
    count = 0
    i = 5

    while (number // i != 0):
        count = count + number // i
        i *= 5       # we have done this because in the case like 25 , by dividing 5
        #  we get five 5 number , in 5's factorial  25 (5*5) alone have 2 5's so we can get into
        # a problem so to avoid that problem we have done this

    return count


# print(trailfac(20))
