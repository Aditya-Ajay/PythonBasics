import math


def complex_algo(items):

    for i in range(5):
        print("Python is awesome")

    for item in items:
        print(item)

    for item in items:
        print(item)

    print("Big O")
    print("Big O")
    print("Big O")


# complex_algo([4, 5, 6, 8])


'''
To find the overall complexity, we simply have to add these 
individual complexities:

O(5) + O(n) + O(n) + O(3)

We said earlier that when the input (which has length n in this case) becomes extremely large, the constants become insignificant i.e. twice or half of the infinity still remains infinity. Therefore, we can ignore the constants. The final complexity 
of the algorithm will be O(n)!
'''


"Worst vs Best Case Complexity"


def search_algo(num, items):
    for item in items:
        if item == num:
            return True
        else:
            pass


nums = [2, 4, 6, 8, 10]

# print(search_algo(2, nums))

'''
BEST CASE : when the required number is found on first position 

WORST CASE : when the required number is found at the last position 

'''


'''
SPACE COMPLEXITY
In addition to the time complexity, where you count the number of steps required to complete the execution of an algorithm, you can also find the space complexity which refers to the amount of space you need to allocate in 
memory during the execution of a program.
'''


def return_squares(n):
    square_list = []
    for num in n:
        square_list.append(num * num)

    return square_list


nums = [2, 4, 6, 8, 10]
# print(return_squares(nums))

'''
The return_squares() function accepts a list of integers and returns a list with the corresponding squares. 
The algorithm has to allocate memory for the same number of items as in the input list. Therefore, the space 
complexity of the algorithm becomes O(n).
'''


# UNDERSTATING 0 (logn)


def recursiveFun(n):
    if (n == 0):
        return "DONE"

    n = math.floor(n/2)
    return recursiveFun(n)


# print(recursiveFun(8))


'''

THIS IS AN EXAMPLE OF LOGARITHMIC EXPRESSION 
AS WE HAVE TO RECURSE THREE TIME TO ACHIEVE TO THE STAGE 
WHERE n == 0 

AND THE CONCEPT OF LOGARITHMIC IS SAME 

WHAT DOES LOG 8 equal to 
So , Log 8 equals to 3 

basically in computer we take the base as 2 
so Log base 2  to 8 equal to 3 

THAT'S WERE WE GET TO THE SOLUTION 


'''


# BINARY SEARCH


def binary_search(arr, num):
    low = 0
    high = len(arr) - 1

    while (high >= low):
        middle_number = (high + low)//2
        print(high, low)

        if (arr[middle_number] == num):
            return middle_number

        if (arr[middle_number] > num):
            high = middle_number - 1

        if (arr[middle_number] < num):
            low = middle_number + 1

        print(high, low)

    return -1


# print(binary_search([45, 50, 68, 70], 80))

arr = [45, 50, 68, 70]
lo = 0
hi = len(arr) - 1


def binaryRecursive(arr, target, lo, hi):
    middleIndex = hi + lo // 2

    if (lo > hi):
        return -1

    if (arr[middleIndex] == target):
        return middleIndex

    if (arr[middleIndex] > target):
        return binaryRecursive(arr, target, lo, middleIndex - 1)

    if (arr[middleIndex] < target):
        return binaryRecursive(arr, target, middleIndex + 1, hi)


print(binaryRecursive(arr, 70, lo, hi))
