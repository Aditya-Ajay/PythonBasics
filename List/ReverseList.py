'''
REVERSING A LIST IN PYTHON

'''


from itertools import count


def reversedList(list):
    str_element = 0
    end_element = len(list) - 1
    while (str_element < end_element):
        list[str_element], list[end_element] = list[end_element], list[str_element]
        str_element += 1
        end_element -= 1
    return list


# print(reversedList([2, 10, 34, 42]))


'''
REMOVING DUPLICATES
'''


# arr = [2, 0, 10]

# arr.insert(3, 5)

# print(arr)


# def updateArray(arr, n, idx, element):
#     if (idx < n):
#         arr[idx] = element
#     else:
#         return -1

#     return arr


# print(updateArray([2, 10], 2, 3, 3))


# def reverseArray(arr, n):

#     for x,  i in arr:
#         arr[x] = arr[n]

#         n = n-1


# print(reverseArray([2, 9, 10, 12], 4))


# def minimumElement(arr, n):
#     minimum = arr[0]

#     for i in range(0, n):
#         if arr[i] < minimum:
#             minimum = arr[i]
#     return minimum


# def maximumElement(arr, n,):
#     maximum = arr[0]

#     for i in range(0, n):
#         if arr[i] > maximum:
#             maximum = arr[i]
#     return maximum


# class Solution:
# inf has been imported in driver code
def immediateGreater(arr, n, x):
    largest = -float("inf")
    for i in range(0, n):
        if (arr[i] < x and arr[i] > largest):
            largest = arr[i]
        if (arr[i] > x):
            largest = -1
    # print(largest)
    return largest


# print(immediateGreater([9, 10, 14, 12, 25], 5, 68))

# class Solution:
#     def isSorted(self, arr, n):
#         isSort = "true"
#         for i in range(0, n - 1):
#             if arr[i] > arr[i + 1]:
#                 isSort = "false"
#                 break

#         return 1 if isSort == "true" else 0


def reverseArray(arr, n):
    for i in range(0, n):
        arr[i] = arr[n-i - 1]
    return arr


# print(reverseArray([2, 8, 10, 15], 4))


# class Solution:
#     # Function to rotate an array by d elements in counter-clockwise direction.
#     def rotateArr(arr, D, N):
#         for i in range(D):
#             first_element = arr[0]
#             for j in range(N-1):
#                 arr[j] = arr[j+1]
#             arr[N-1] = first_element
#         print(arr)


class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, A, D, N):
        rotated_arr = A[D % N:] + A[:D % N]
        print(* rotated_arr)


print(reverseArray([2, 8, 10, 15], 4))
