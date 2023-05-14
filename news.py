#vowel we see
vowel = "aeiou"
s=[]
count = 0
string = input("enter the input")
for i in string:
    if i in vowel:
        s.append(i)
        count += 1
        
        #print("yes vowels are there in string")
print(count)
print("".join(s))