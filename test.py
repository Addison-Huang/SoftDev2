def outer(x):
    def contains(l):
        return x in l
    return contains

contains_15 = outer(15)
print(contains_15([1,2,3,4,5]))
print(contains_15([13,14,15,16,17]))
print(contains_15(range(1,20)))

print(outer(42))
del outer
#print(outer(42))
print(contains_15(range(14,20)))

def repeat(str):
    def iteration(x):
        return str * x
    return iteration

r1 = repeat("hello")
r2 = repeat("goodbye")

print(r1(2))
print(r2(2))
print(repeat('cool')(3))
'''
def outer():
    x = "foo"
    def inner():
        x = "bar"
    inner()
    return x

print(outer())
'''
def outer():
    x = "foo"
    def inner():
        nonlocal x
        x = "bar"
    inner()
    return x

print(outer())

def make_counter():
    x = 0
    def count():
        nonlocal x
        x = x + 1
    count()
    return x
