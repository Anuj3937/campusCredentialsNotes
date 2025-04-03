# #data=input("enter any number")
# data='578378923'
# key=[]
# num=list(data)
# for i in num:
#    if num.count(i)>=2 and i not in key:
#       key.append(i)
# print(len(key))
# num.sort()
# for i in data:
#     if data.count(i)>2:

# data = input("Enter any number")


# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()
# data = input("Enter any number")
# data = '578378923'

# # Use a set to track unique digits that repeat at least twice
# repeated_digits = {digit for digit in set(data) if data.count(digit) >= 2}

# # Output the count of such digits
# print(len(repeated_digits))
# for i in range(1,6):
#     for j in range(1,5+2-i):
#         print(chr(64+j),end=" ")
#     print()


# a=input("enter a string=")
# if a==a[::-1]:
#     print('pali')
# else:
#     ("no pali")

# a="listen"
# b='silent'
# c=sorted(a)
# d=sorted(b)
# if c==d:
#     print("anagram")
# else:
#     print("no")

#s="The quick brown fox jumps over the lazy dog"
# s=input()
# for i in range(1,27):
#     if chr(64+i) not in s and chr(96+i) not in s:
#         print("not pangram")
#         break
# else:
#     print("pangram")

# s="programming"
# p=""
# for char in s:
#     if char not in p:
#         p=p+char
# print(p)

a="ababababababbababa"
print(a.count("ab"))