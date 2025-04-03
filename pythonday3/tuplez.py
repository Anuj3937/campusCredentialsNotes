# a=(23,23,12,"anuj",'erwqe')
# print(a)
# print(type(a))
# a(2)="sunil"
# aa=12,13
# a=a+(3,2)+aa
# print(a)

# b=(1,2,3,"Sde")
# ls=list(b)
# ls.append("a")
# print(ls)
# b=tuple(ls)
# print(b)
# n=int(input())
# sum=0
# ls=[]
# for i in range(n):
#     a=int(input())
#     ls.append(a)
# for j in range(len(ls)):
#     if j+1 in range(len(ls)):
#         sum+=abs(ls[j]-ls[j+1])
# print(sum)

# ch=ord(input())
# if ch>=65 and ch<91:
#     print('upper case')
# elif ch>=97 and ch<122:
#     print('lower case')
# elif ch>=48 and ch<57:
#     print('digit case')
# else:
#     print('speacial case')

s=input()
for i in s:
    if i.isalnum():
        print("output is" ,i,end='\n')
