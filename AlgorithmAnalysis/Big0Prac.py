# O(1)

def cons(arr):
    print("HELLO WORLD")


# cons([2, 3])


''' in this case does input size does not matter , the function will take the same
    same amount of time irrespective of the input  
'''

# 0(n)


def linear(arr):
    for i in arr:
        print("hi")


# linear([2, 8, 10, 25])

'''
IN THIS CASE THIS FUNCTION SIGNIFIES THAT THE TIME TAKEN WILL INCREASE IN THE LINEAR MANNER
AS THE INPUT SIZE RISES THE TIME WILL INCREASE BUT IN THE LINEAR MANNER
'''


# 0(n^2)


# for i in range(3):
#     for j in range(2):
#         print(f'{i} => {j}')

'''
the iteation is actually doubled 
'''

'''
Logarithmic Complexity - O(logn)

Some algorithms achieve logarithmic complexity, such as Binary Search. 
Binary Search searches for an element in an array, by checking the middle 
of an array, and pruning the half in which the element isn't. It does this 
again for the remaining half, and continues the same steps until the element 
is found. In each step, it halves the number of elements in the array.

This requires the array to be sorted, and for us to make an assumption about the 
data (such as that it's sorted).


When you can make assumptions about the incoming data, you can take steps that reduce the complexity of an algorithm. Logarithmic complexity is desireable, as it achieves good performance even with 
highly scaled input.

'''
