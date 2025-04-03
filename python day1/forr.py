for i in range(12,1,-2):
    print(i)
for i in range(1,21,2):
    print(i)
# for i in range (1,11):
#     print(i*2,"             ", i*3,"       ", i*4)
# # print()
# a="anujaa"
# for i in a:
#     if i=='a':
#         print(i)
# cvv=0
# ccc=0
# n="prashantjha"
# for i in n:
#     if i=='a'or i=='e'or i=='i'or i=='o'or i=='u':
#         cvv+=1
#     else:
#         ccc+=1
# print(ccc, cvv)
# for i in range(1,6):
#     if i ==4:
#         continue
#         print(i)
for i,j in zip(range (1,6),range(5,0,-1)):
    if i==3 and j==3:
        continue
    print(i ," " ,j)