'''
Team Zadical -- Zane Wang and Addison Huang
SoftDev2 pd8
K17 -- PPFTLCW
2018-04-14
'''

#creates a list of 0 through 4 and multiplies all elements by 22
def doubleEvenLoop():
    array = []
    for x in range(5):
        array.append(str(x*22))
    return array

print(doubleEvenLoop())

def doubleEvenList():
    return [str(x*22) for x in range(5)]

print(doubleEvenList())

#returns the first 5 numbers that end with a 7 by adding 7 to 0, 10, 20, 30 and 40
def sevensLoop():
    array = []
    for x in range(5):
        array.append(x*10+7)
    return array

print(sevensLoop())

def sevensList():
    return [x*10+7 for x in range(5)]

print(sevensList())

#returns a pattern where of three lists, with the first element being 0, second being which list, and the third being 2 times the list number
def tripletsLoop():
    array =[]
    for x in range(3):
        array.append(0)
        array.append(x)
        array.append(x*2)
    return array

print(tripletsLoop())

def tripletsList():
    return [0 if x%3 == 0 else y if x%3==1 else y*2 for y in range(3) for x in range(3) ]

print(tripletsList())

#searches for composite numbers, by adding them to array after finding them divisible by a number greater than 1 and less than itself
def compositeLoop():
    array = []
    for x in range(101):
        for y in range(2,x/2+1):
            if (x%y == 0):
                array.append(x)
                break;
    return array

print(compositeLoop())

def compositeList():
    return [x for x in range(101) if len([1 for y in range(2, x/2+1) if x % y == 0]) != 0]

print(compositeList())

#returns a list of elements that aren't composite, not including 1 because 1 only has 1 divisor
def primeLoop():
    array = []
    composites = compositeLoop()
    for x in range(2,101):
        if not x in composites:
            array.append(x)
    return array

print(primeLoop())

def primeList():
    return [x for x in range(2,101) if x not in compositeLoop()]

print primeList()

#returns the array of all divisors of a number by looking at divisibility of numbers from 1 to that number
def divisorLoop(n):
    array = []
    for x in range(1,n):
        if (n%x == 0):
            array.append(x)
    return array

print(divisorLoop(15))

def divisorList(n):
    return [x for x in range(1, n) if n%x==0]

print(divisorList(15))

#creates a new 2D array and switches the row and column inputs
def transposeLoop(matrix):
    array = []
    for i in range(len(matrix[0])):
        array.append([]) 
        for j in range(len(matrix)):
            array[i].append(matrix[j][i])
    return array

print(transposeLoop([[1,2,3],[4,5,6]]))


def transposeList(matrix):
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    print(transposeList([[1,2,3],[4,5,6]]))
