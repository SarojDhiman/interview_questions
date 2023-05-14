#find the pair with given number in a list
# l = [1,2,3,4,5,6,7,8,9]
# k = 10
# n = len(l)
# for i in range(n):
#     for j in range(i+1,n):
#         if (l[i]+l[j]) == k:
#             print(l[i],l[j])

#   create fibonnaci series thy using recurssion
# n = int(input("enter the string"))
# def fibbonaci(n):

#     if n<=0:
#         return 1
#     elif n==1 and n==2:
#         return 1
#     else:
#         return fibbonaci(n-1) + fibbonaci(n-2)
# #11print(fibbonaci(n))
# def feb_ci(n):
#     for i in range(n):
#         print(fibbonaci(i))
# feb_ci(n)
x = "the sky is blue"
# s=string.split()
# list1=[]
# for i in s:
#     list1.insert(0,i)

# print(" ".join(list1))
import time
found = -1
start = time.time()
def rev_str(x):
    s=[]
    m = x.split()
    for i in m:
        s.insert(0,i)
    return " ".join(s)
print(rev_str(x))
end = time.time()
found=1
print(found)
print(1000*(end-start))