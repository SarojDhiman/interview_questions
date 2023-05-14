# d1_given = {"saroj":1,"sarz":28,"sachin":18}
# d2_sorted = sorted(d1_given.keys())

# dict_empty={}
# for i in d2_sorted:
#     dict_empty[i]=d1_given[i]
# print(dict_empty)

#pair of given number in a list
# l = [1,2,3,4,5,8]
# k=5
# n=len(l)
# for i in range(n):
#     for j in range(i+1,n):
#         if (l[i]+l[j])==k:
#             print(l[i],l[j])

#find the repeated characters in a string
string1 = "aabbdccfghh"
s = {}
for i in string1:
    if i in s:
        s[i] += 1
    else:
        s[i] = 1
r = max(s,key=s.get)
print(r)































