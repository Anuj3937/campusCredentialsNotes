# mylist=['Anuj',77,45.3,'ddos','swswsw',12+2j,22,12,12.2]
# print(mylist[0])
# # print(mylist[0])
# # print(mylist[1])
# # print(mylist[2])
# # print(mylist[-1])
# # print(mylist[2:5])
# # print(mylist[1:])
# # print(mylist[:5])
# # print(mylist[2:5:2])
# mylist[0]='wwe'
# print(mylist[0])
# mylist.append('anuj')
# print(mylist[9])
# mylist.extend('gygy')
# print(mylist)
# mylist.insert(0,23)
# print(mylist)
# # mylist.remove('prashant')          error
# mylist.remove('anuj')
# print(mylist)

# a=mylist.copy()
# print('a=',a)

#  2d list
# b=[['anuj',23],[32],['ttr','434']]
# print(b)
# print(b[0][1])
# print(b[1][0])
# print(b[2][1])
# b.append([[23],[55]])
# c=['anuj','ssd']
# print(c*2)
# d=[22,12]
# print(c,d)
# print(c+d)
# del c[1]
# del c     #entire list deleted , remove keyword removes a single element at a time
# # print(c)
# d.clear()
# print(d)

# typecasting
# a=1,5,8
# print(a)
# b=list(a)
# print(b)

# a=[12,13,13,41,31]
# a.reverse()
# print(a)

# sorting example
# a=[41,21,3421,2324,122,12,11]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)

#alising
# a=[1,2,3,4,5,6]
# b=a
# print(id(b))
# print(id(a))
# a.append(3)
# print(a)
# # print(b)
# traverse
# a=[1,2,3,4,5]
# for i in a:
#     print(i)

# q. find the majority element
# data=[3,3,4,2,4,4,2,4,4]
# max=min=data[0]
# for i in range(len(data)):
#     if data[i]>max:
#         max=data[i]
#     if data[i]<min:
#         min=data[i]
# print('max',max)
# print('min', min)

# data=[1,0,0,1,2,3,0,1,5,4,3,0,5,3,1,0,4,3,3,0]
# for i in range(len(data)):
#     if data[i]==0:
#         data.remove(0)
#         data.append(0)
# print(data)

# data=[3,3,4,2,4,4,2,4,4]
# max=min=data[0]
# for i in range(len(data)):            del not working properly
#     if data[i]>max:
#         max=data[i]
#     if data[i]<min:
#         min=data[i]
# print('max',max)
# print('min', min)


# num=[2,3,4,1,22,43,12,41]
# num.sort(reverse=True)
# print(num)
# a=int(input("enter value of k"))
# print(num[a-1])

# mycart=[10,20,30,40,400,600]
# for item in mycart:
#     if item>400:
#         print("not my budget")
#         continue
#     print(item)
#           print("you got everything")


# a=([1,2,3],[4,3,2],[7,6,3])

# print('anuj12'.isalnum())
# print('anuj12'.isalpha())
# print('12'.isdigit())
# print('anuj12'.istitle())
# print(' a n u j 1 2 '.isspace())
# print(' '.isalpha())

# n=[1,2,3,5,5,5,2,1,4,4,4,6,6,6,4]
# print(n.count(1))
# print(n.count(2))
# print(n.count(3))
# print(n.count(4))
# print(n.count(5))
# print(n.count(6))
# print(n.count(7))

# count=0
# data=[1,1,0,1,1,1,0,1,1,1,1]
# for i in range(len(data)-1):
#     if data[i]==1 and data[i+1]==1:
#             count=count+1
# print(count)

# a=[1,2,3,4]
# b=[3,4,5,6]
# mewlist=[]
# for i in a:
#     if i in b:
#         mewlist.append(i)
# print(mewlist)

# a=[2,6,5,4,4,2,6,5,7]
# if i in 
