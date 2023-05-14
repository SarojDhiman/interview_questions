s = 'a4b3c2'
output = 'aaaabbbcc'
s = 'a4b3c2'
output = 'aaaabbbcc'
r = []
o = []
for i in s:
    if i.isdigit():
        s = int(i)
        r.append(s)
    else:
        o.append(i)
        

print(o)

print(r)
for i in range(0,3):
    print(o[i]*r[i],end= "")

d = {}
for i in range(1,3):
    name = input("enter the name: ")
    marks = int(input("enter the marks"))
#     d[name]=marks
#     i+=1
# print(d)
# print(max(d.items()))
# print(sum(d.values()))









# u = 'b4a1d3'
# output = 'abd134'

# a = []
# d = []
# for i in u:
#     if i.isalpha():
#         d.append(i)
#     else:
#         a.append(i)
# print("".join(sorted(d))+"".join(sorted(a)))

# d = {}
# v = {'a','e','i','o','u'}
# s = "abfsjahdjjdsioafhdksgskdvlacvsk"
# for i in s:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i]=0
# print(d)
# for i in  d:
#     if i in v:
#         print(i)
        

#find the maximum repeated characters in a string
# string = "ghdfauieth"
# d = {}
# for i in string:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i] = 1
# print(d)
# print(max(d,key = d.get))
# print(d.values())
# print(d.keys())

# l = [1,2,3,4,5]
# w = [6,7,8,9,0]
# l1 = list(map(lambda l,w : l**2+w**2,l,w))
# print(l1)
def outer(x):
    return "the name is",x
def decorator(y):
    return outer(y)

print(decorator("saroj"))