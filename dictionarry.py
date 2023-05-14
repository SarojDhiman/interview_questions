# d1 = {31:"saroj",6:"sunita",5:"sachin"}
# d = sorted(d1.keys())
# print(d)
# d2 = {}
# for i in d:
#     d2[i]=d1[i]
# print(d2)
# res = {key: val for key, val in sorted(d1.items(), key = lambda ele: ele[1])}






# # res = {key: val for key, val in sorted(d.items(), key = lambda ele: ele[1])}
# print(res)

#find the pair with given number in a list
l = [1,2,3,4,5,6,7,8,9]
l1=[]
k=10
n = len(l)
for i in range(n):
    for j in range(i+1,n):
        if (l[i]+l1[j]) == K:
            print(l[i],l[j])

















