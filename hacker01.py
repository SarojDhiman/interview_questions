# #prime number between 100 to 200
# for i in range(100,201):
#     if all(i%n!=0 for n in range(2,i)):
#         print(i)

# #sort a list without using sort function
# l1 = [22,41,2,12,34,56]
# for i in range(0,len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i]>l1[j]:
#             l1[i],l1[j]=l1[j],l1[i]
# print(l1)

# #print fibbonaci series
# def fibbonaci(x):
#     if x<=1:
#         return 1
#     else:
#         return fibbonaci(x-1)+fibbonaci(x-2)
    
# for i in range(0,12):
#     print(fibbonaci(i),end=" ")

# #python program to reverse the list
# ll = [1,5,33,2,9,0]
# ll.sort()
# ll[::-1]#reveser   , you can also use insert 
# print(ll)

# #chedking the string is palindrome or not
# string = "madam"
# def palindrome(string):
#     rev_str = string[::-1]
#     if rev_str == string:   # u can also use reversed
#         print("the string is palidrom!")
#     else:
#         print("the string is not palindrom!")

# print(palindrome(string))

# r = "".join(reversed(string))
# if r == string:

#     print("yeh palindrome!")

# #print duplicates in a list:
# l1 = ["saroj",1,2,3,4,3,0,6,"saroj",56]
# l2 = []
# for i in l1:
    
#     if i not in  l2:
#         l2.append(i)
# print(l2)
# #we can directly print the set as well
# print(set(l1))# when we take set these come as arranged

# print(set([i for i in l1 if l1.count(i)>1]))

# #print number of words in a given sentence
# s = "this is grass"
# print(len(s.split()))

# #python program to search the element in a given array

# array = [1,2,3,4,5]
# for i in array:
#     if i == 5 in array:
#         print("yes 5 is present")

# # and if we have to define the function to check the list is present or not
# def recheck_element(x,n):
#     for i in x:
#         if i==n in x:
#             return "o yes its present!"
# print(recheck_element([4,5,6,7,8,5],8))

# #write a python program to implement a binary search!



# #ploting bar chart
# import matplotlib.pyplot as plt
# import pandas as pd
# data = [["saroj",12,90,"cdac"],
#         ["sunita",13,70,"nursing"],
#         ["sachin",14,67,"bcom"]]
# df = pd.DataFrame(data,columns=['names','rollno','score','course'])
# print(df)
# plt.bar(df['rollno'],df['score'])
# #plt.show()

# #write python program to join 2 strings
# s1 = "saroj"
# s2 = "dhiman"
# print(s1+" "+s2)
# print("".join(s1 + s2))


# #write a python program to extract digits from the string
# string = "12sar56323421jklmnopq"
# digits = "1234567890"
# k=[]
# for i in string:
#     if i in digits:
#         k.append(i)
# print("".join(k))
# print(k)

# #write a python program to split string by using delimater
# string = "this is dog"
# print(string.rstrip().split(' '))

# #write a program to delete the reoccuring character in the string and return a new string
# string = "this is a blue colur maggi and i love this maggi"
# # string = string.split()  if u uncomment this u get whole word expect the maggie
# s = []
# for i in string:
#     if i not in s:
#         s.append(i)
# print("".join(s))


# newlist =[[52, None, None], [129, None, None], [56, None, None], [111, None, None],  
#           [22, None, None], [33, None, None], [28, None, None], [52, None, None],  
#           [52, None, None], [52, None, None], [129, None, None], [56, None, None],  
#           [111, None, None], [22, None, None], [33, None, None], [28, None, None]]
# newlist = [item for items in newlist for item in items]
# print(newlist)

# # newlist = [item for sublist in newlist for item in sublist]
# # print(newlist)

# #sort a dictionary by using a list comprehenssion
# d1 = {21:'saroj',12:'sara',4:'how',45:'do'}
# d2 = {}
# s = sorted(d1.keys())
# for i in s:
#     d2[i] = d1[i]
# print(d2)


# #find a pair of sum in a given list
# l1 = [1,2,3,4,5,6,7,8,9]
# k = 10
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i]+l1[j]==k:
#             print(l1[i],l1[j])
     
        
# #give the output of string as s2
# s1 = "the sky is blue"
# s = s1.split()
# s = s[::-1]
# print(" ".join(s))

# #find the maximum repeated characters in a string
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
#         print(i,end = " ")

# #find max and min in a list without using predefined functions
# l = [1,5,67,3,4,5,6,8,9]
# l.sort()
# print(l[0])
# print(l[-1])

# #without min max

# min1 = l[0]
# max1 = l[0]
# for i in l:
#     if i>min1:
#         max1 = i
#     if i<min1:
#         min1 = i
#     print(max1,min1)

# #convert lists into dictionary
# l1 = ["s","a","r"]
# l2 = [1,2,3]
# result = dict(zip(l1,l2))
# print(result)        
# p=list(result.values())
# q=list(result.keys())
# p.sort()
# q.sort()
# print(p[-2],q[-2])


list1 = [1,2,3,4,5,6,7,8,9,3,5,6,7]
d = {}
for i in range(list1):
    if i in d:
        d[i]+=1
    else:
        d[i] = 0


print(d)    
        
        










