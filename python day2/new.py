n=[3,5,4,7,1]
s=0
for i in n:
    print(i)
    if i<s:
        print(i,s)
        s=i
print(s)
