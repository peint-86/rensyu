x = int(input())
def fib(y):
    if y < 2 :
        return y
    else:
        return fib(y-1) + fib(y-2)
print(fib(x))