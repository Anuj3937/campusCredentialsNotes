# # a=int(input('Enter a number:'))
# # if a>0:
# #     print("positive")
# # if a<0:
# #     print("negative")
# # if a==0:
# #     print("zero")
# # a1=int(input('Enter a number:'))
# # a2=int(input('Enter a number:'))
# # a3=int(input('Enter a number:'))
# # a4=int(input('Enter a number:'))
# # a5=int(input('Enter a number:'))
# # if a1>a2 and a1>a3 and a1>a4 and a1> a5:
# #     print("a1 big")
# # if a2>a1 and a2>a3 and a2>a4 and a2>a5:
# #     print("a2 big")
# # if a3>a2 and a3>a1 and a3>a4 and a3> a5:
# #     print("a3 big")
# # if a4>a2 and a4>a3 and a4>a1 and a4> a5:
# #     print("a4 big")
# # if a5>a2 and a5>a3 and a5>a4 and a5> a1:
# #     print("a5 big")

# d="SATURDAY"
# d.lower()
# if d=="SATURDAY":
#     print("weekend")
ch=ord(input())
if ch>=65 and ch<91:
    print('upper case')
elif ch>=97 and ch<122:
    print('lower case')
elif ch>=48 and ch<57:
    print('digit case')
else:
    print('speacial case')