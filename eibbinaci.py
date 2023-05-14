n = int(input("enter the number"))
#fibbonaci series
def fibb(n):
    if n<=0:
        return 1
    elif n==1 and n==2:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)
    
#6print(fibb(n))
#for i in range(fibb(n)):
    #5print(i)
def Fibbonaci(n):
    for i in range(0,n):
        print(fibb(i))
print(Fibbonaci(n))