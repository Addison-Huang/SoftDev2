'''
Team Weem Addison Huang and Hui Min Wu
softDev2 pd 8
k19
2019-04-17
'''

#goes through list A and returns if its in B
def intersection(A,B):
    return [x for x in A if x in B]

print(intersection([1,2,3],[2,3,4]))

#goes through list A and returns it if its not in B
def setdiff(A, B):
    return [x for x in A if not x in B]

print(setdiff([2,3,4], [1,2,3]))

#uses setdiff twice
def sym(A, B):
    return setdiff(A, B) + setdiff(B, A)

print(sym([1,2,3], [2,3,4]))

#returns list of x,y where x and y are elements in A and B respectively
def cartProd(A,B):
    return [[x,y] for x in A for y in B]

print(cartProd([1,2],["red","white"]))

def union(A,B):
    """return union of two lists every element(no duplicates)"""
    return [x for x in A if x not in B] + [x for x in B]

print(union([1,2,3],[2,3,4]))
