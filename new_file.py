# def genrator(x):
#     for i in x:
#         yield i
# x=[1,2,3]        
# # print(genrator(x))
# g = genrator(x)
# print(next(g))
# print(next(g))
# print(next(g))
# # print(next(g))

l = [1,2,3,3,4,67,5,5]
d = []
n = []
for i in l:
    if i not in d:
        d.append(i)
    else:
        n.append(i)
print(n)



for i in range(10,30):
    if all(i%n!=0 for n in range(2,i)):
        print(i)

def uppercase(func):
    def my_function(string):
        result = func(string.upper())
        return result.upper()
    return my_function

@uppercase
def reverse(string):
    return string[::-1]

print(reverse("Hello, world!"))
 
def my_dec(function):
    def my_new_fxn(s):
        result = function(s.upper())
        return result.upper()
    return my_new_fxn
@my_dec
def reverse(s):
    return s[::-1]
print(reverse("hello you are baffaloo"))



import cv2
