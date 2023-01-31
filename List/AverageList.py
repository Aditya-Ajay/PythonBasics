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


seg([2, 9, 10, 35])


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


print(largetNumber([2, 10, 34, 38, 42]))
