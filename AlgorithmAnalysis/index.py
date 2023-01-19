# Sum of n natural Number :


# Execution Speed of a function will depend on :

# 1- Programing language dependent
# 2- Machine Dependent
# 3- Machine Load dependent


# def sumOfNaturalNumber1(n):
#     return n*(n+1)/2


# print(sumOfNaturalNumber1(5))


# def sumOfNaturalNumber(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     return sum


# print(sumOfNaturalNumber(5))


# To avoid all the dependency to check the execution speed
# we cam up with the Asymptomatic notation
# ------------------------

# which is machine independent , programming lang independent
# the only thing which it is dependent on is the size of input


# Selection Sort

arr2 = [80, 25, 90, 4, 14]


def output(arr):
    for i in range(0, len(arr)):
        print(i)

        for j in range(i, len(arr)):

            print(j)


print(output(arr2))

# -------------------
