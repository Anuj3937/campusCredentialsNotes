# def remove_keys_from_input():
#     dictionary = dict(input("Enter key value pairs: ").split() for _ in range(int(input("Number of pairs: "))))
#     for key in input("Keys to remove: ").split():
#         dictionary.pop(key, None)
#     print(dictionary)

# remove_keys_from_input()





# def msg():
#   print("hello")
# msg()
# msg()
# msg()
# positional
# keyword
# default
# variable length/variablenumber of argument
# unknown argument
# def login():
#   username=input()
#   password=input()
#   if username==password:
#     print("successfully")
#   else:
#     print("Non")
# login()
#positional
# def info(fn,ln):
#     print("fn" , fn)
#     print("ln" , ln)
# info("anuj","pathak")
# def add(n1,n2):
#     return n1+n2
# a=int(input())
# b=int(input())
# print(add(a,b))
# def arithmetic(a,b):
#     r=a*b
#     p=a/b
#     q=a+b
#     return r,p,q
# print("res=",arithmetic(10,5))

# keyword argument
# def info(fn,ln):
#     print("fn" , fn)
#     print("ln" , ln)
# fn="anuj"
# ln="pathak"
# info(fn,ln)


#default
# def func(city="nugpur"):
#     print(city)
# func("Delhi")
# func("mumbai")
# func()

# def func(name):
#     for i in name:
#         print(i)
# name_of_p=["anurag","singh","sandip"]
# func(name_of_p)

#variable length argument
def name(*name):
    print(name)
name("anuj","anurag",1001)