
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)

def fibo(n):
    if n<2:
        return n
    return fibo(n-1)+fibo(n-2)

def cuenta(n):
    if n<10:
        return 1
    return 1+cuenta(n//10)

def A(m,n):
    if m==0:
        return n+1
    if n==0 and m>0:
        return A(m-1,1)
    if n>0 and m>0:
        return A(m-1,A(m,n-1))
#recursividad  de cola

def factooo(n):
    return facto_tail(n,1)

def facto_tail(n,p):
    if n==0:
        return p
    return facto_tail(n-1,n*p)
print(factooo(900))

