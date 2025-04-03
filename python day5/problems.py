# mylist=[[100,198,333,323],[122,232,221,111],[223,565,245,764]]
# new_list=[]
# for i in range(3):
#     j=0
#     max=mylist[i][j]
#     for j in range(4):
#         c_max=mylist[i][j]
#         if max<c_max:
#             max=c_max
#     new_list.append(max)
# print(new_list)


# a="anuj*is*a*good*programmer"
# n=""
# val=""
# for i in a:
#     if i=="*":
#         n=n+i
#     else:
#         val=val+i
# print(n+val)
# n=10
# a=[1,2,3,3,4,1,4,5,1,2]
# b={}
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# for key,value in b.items():
#     print({key},"ocuurs",{value},"times")   
#other way
# for i in range(n):
#     key=a[i]
#     c=0
#     j=i+1
#     for j in range(len(a)):
#         if key==a[j]:
#             c+=1
#     b[key]=c
# for i,j in b.items():
#     print(i,"occurs",j,"times")
n="abcdfjgerj abcdfijger"
def stringvarifieh(n):
    for i in range(len(n)):
        if n[i]==" ":
            return n[i-1]
print(stringvarifieh)