'''
FINDING THE AVERAGE OF THE LIST
'''


def averageList(list):
    sum = 0

    for i in list:
        sum += i
    average = sum / len(list)
    print(average)


# averageList([2, 9, 1])


'''
SEGREGATING A LIST INTO ODD LIST AND EVEN LIST 
'''


def segregatingList(list):
    odd = []
    even = []

    for i in list:
        if (i % 2 == 0):
            even.append(i)
        else:
            odd.append(i)
    # print(odd, even)


# segregatingList([2, 22, 10, 20])


'''

python program to return a list in which the 
numbers are less than the numbers which we have specified . 


'''


def num(list, number):
    modlist = []
    for i in list:
        if (i < number):
            modlist.append(i)
    # print(modlist)


# num([2, 9, 20], 12)


'''
SOLVING THE QUESTIONS USING COMPREHSNION LIST 
'''


def listSmaller(l, x):
    return [e for e in l if e < x]  # This is the use of comprehensive list


aditya = listSmaller([2, 9, 10], 4)

# print(aditya)


def seg(l):
    even = [x for x in l if x % 2 == 0]
    odd = [y for y in l if y % 2 != 0]

    print(even, odd)


# seg([2, 9, 10, 35])


string = "geeksforgeeks"

rem = [x for x in string if x in "aeiou"]


'''
TO FIND THE LARGEST NUMBER IN THE LISTS 
'''


def largetNumber(list):
    largestNumber = list[0]

    for i in list:
        if (i > largestNumber):
            largestNumber = i
    return largestNumber


# print(largetNumber([2, 10, 34, 38, 42]))


'''
ANOTHER METHOD 

'''


def getMax(list):
    for x in list:
        for y in list:
            if y > x:
                break
        else:
            return x
    return None


# print(getMax([2, 8, 19]))

'''
NEED TO HAVE A BETTER UNDERSTANDING ON THIS CONCEPT
'''


'''
WRITE A PROGRAM TO FIND THE SECOND LARGET ELEMENT IN A LIST
'''


def largestElement(list):
    largest = list[0]
    for i in list:
        if (i > largest):
            largest = i
    return largest


def secondLargest(list):
    if (len(list) < 2):
        return None

    largestNumber = largestElement(list)
    secondLargest = list[0]
    for i in list:
        if i != largestNumber and i > secondLargest:
            secondLargest = i
        # print(i)
    return secondLargest


# print(secondLargest([2, 9, 10, 25, 81, 23]))
