string ="agfdjkdsu5673jgvk"
digits ="1234567890"
s = []
r = []
for i in string:
    if i in digits:
        s.append(i)
    else:
        r.append(i)
print(r)
