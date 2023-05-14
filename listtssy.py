# # l=[1,2,3]
# # y = [3,4,5]
# # # l2 = list(map(lambda x: x**2,l))
# # # print(l2)
# # #if i want to use lambda on list
# # s = "meri zindghi main aye ho to"
# # vowel = "aeiou"
# # s1 = list(map(lambda l,y:l+y))
# # print(s1)

# #to add two lists


p=lambda x,y:(1/x+y)**3+1
print(p(3,7))
############count the maximum repeated word
# s = "abbacaa"
# from collections import Counter
# m = Counter(s)
# print(max(m,key=m.get))########### with this we get the number of maximum keys
# print(m)
# count=0
# for i in s:
#     if i in c:
#         c[i] += 1
#     else :
#         c[i] = 1
# print(max(c,key=c.get))
# print(c)

# question:  sort list without using sort keyword

# l1 =[5,1,2,3,4]
# print(l1)
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i]>l1[j]:
#             l1[i],l1[j]=l1[j],l1[i]
# print(l1),,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,










# import numpy as np
# a = np.full((5,6),6,dtype=int)
# print(a)
# array1 = np.matrix("[1,2,3;4,5,6;7,8,9]")
# print(array1)
# p = max(array1)
# print(p)
# import pandas as pd
# # s1 = pd.Series(range(2,4))
# # s2 = pd.Series(range(4,6))
# # print(s1+s2)

# df = pd.DataFrame([['s','a'],[5,6]],columns=["name","rank"])

# print(df)

# s = {11,2,3,4}
# print(sorted(s))


# import datetime as dt
# saroj = dt.datetime.now()
# def create_file():
#     with open(saroj.strftime("%Y %B %d")+".txt",'w') as file:
#         file.write("welcome")
# create_file()

# import pandas as pd
# import numpy as np
# s =pd.Series(np.random.rand(3))
# print(s)
# s1 =pd.DataFrame(np.random.rand(3,4))
# print(s1)


# import pandas as pd
# df = pd.DataFrame({'names':["saroj","anju","ankush","anku"],
#                    'age':[23,45,65,32]},index=['USA','JAPAN','PATTI','GURGAO'])
# print(df)
# print(df.loc['USA']) #so loc use here to extract information
# print(df.iloc[[0,3],0])
# print(df.loc[2:3])

import pandas as pd
df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],columns=['s','a','r'])
print(df)
df1 = pd.DataFrame({'a':1,'b':2},index=['usa','japan'])
print(df1)
#print(df.iloc[[0,3],1])
#print(df.loc[1])







































