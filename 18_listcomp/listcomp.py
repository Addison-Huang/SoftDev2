'''
Team Zadical -- Addison Huang and Zane Wang
softDev2 pd 8
k18 
2019 - 04 - 16
'''

def pythTriple(n):
    return [(x,y,z) for x in range (1,n) for y in range(x,n) for z in range(y,n) if x**2 +y**2 == z**2]

print(pythTriple(20))

def qsort(array):
    return qsort([x for x in array[1:] if x <= array[0]]) + [array[0]] + qsort([x for x in array[1:] if x > array[0]]) if len(array) > 1 else array

print(qsort([7,1,5,12,3]))
print(qsort([4,1,23,7,8,23,6,1,8,9,12]))
