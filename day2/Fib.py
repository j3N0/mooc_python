#Fib.py
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    n = eval(input())
    print(fib(n))
