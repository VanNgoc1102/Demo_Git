import re


def fibonacci(n):
    a=[]
    if n<=2 :
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Nhap gt n: "))
print(fibonacci(n))
def listfibo(n):
    for i in range(1,n+1):
        print (fibonacci(i),end='\t')
listfibo(9)