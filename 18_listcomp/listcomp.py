import math
def pythTriple(n):
    return [[y,x,z] for x in range (1,n) for y in range(1,x) for z in range(1,n) if x**2 +y**2 == z**2]

print(pythTriple(20))

    
    
