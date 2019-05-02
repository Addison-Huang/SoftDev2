'''
Addison Huang
Softdev2 pd8
K23 --closure
01 05 2019
'''

def memoize(f):
    memo={}
    def helper(x):
        if x not in memo.keys():
            memo[x]=f(x)
            return f(x)
        else:
            return memo[x]
    return helper

def fib(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

fib = memoize(fib)
print(fib(40))
