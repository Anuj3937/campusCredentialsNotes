# p=int(input())
# q=int(input())
# try:
#     print(p/q)
# except ZeroDivisionError as msg:
#     print("no zerp",msg)
# except ValueError as msg:
#     print("number dal bhai ",msg)


# try:
#     p=int(input())
#     q=int(input())
#     print(p/q)
# except ZeroDivisionError as msg:
#     print("no zerp",msg)
# except ValueError as msg:
#     print("number dal bhai ",msg)

# try:
#     a=int(input())
#     b=int(input())
#     print(a/b)
# except (ValueError , ZeroDivisionError) as msg:
#     print(msg)
# except:
#     ("default block")

# try:
#     a=int(input())
#     b=int(input())
#     print(a/b)
# except (ValueError , ZeroDivisionError) as msg:
#     print(msg)
# else:
#     print("everything ok")


# try:
#     a=int(input())
#     b=int(input())
#     print(a/b)
# except (ValueError , ZeroDivisionError) as msg:
#     print(msg)
# finally:
#     print("this block always gets executed")

# try:
#     a=int(input())
#     b=int(input())
#     try:
#         print(a/b)
#     except  ZeroDivisionError as msg:
#         print(msg)
# except ValueError as msg:
#     print(msg)
# finally:
#     print("this block always gets executed")

try:
    a=int(input())
    b=int(input())
    print(a/b)
except (ValueError , ZeroDivisionError) as msg:
    print(msg)
else:
    print("everything ok")
finally:
    print("ok")
