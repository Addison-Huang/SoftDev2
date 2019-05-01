'''
ADdison Huang
Softdev2 pd8
k22-- closure
2019 04 30
'''
def repeat(str):
    def iteration(x):
        return str * x
    return iteration

r1 = repeat("hello")
r2 = repeat("goodbye")

print(r1(2))
print(r2(2))
print(repeat('cool')(3))

def make_counter():
    x = 0
    def count():
        nonlocal x
        x = x + 1
        return x
    return count

ctr1 = make_counter()
print(ctr1())
print(ctr1())
ctr2=make_counter()
print(ctr2())
print(ctr1())
print(ctr2())
