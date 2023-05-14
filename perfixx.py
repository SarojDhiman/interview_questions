#sort a list
l1 = [1,2,67,4,5,6,7]
for i in range(0,len(l1)):
    for j in range(i+1):
        if l1[i]>l1[j]:
            l1[i],l1[j]=l1[j],l1[i]
print(l1)