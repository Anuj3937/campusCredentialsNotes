from mod1 import welcome,square,pi
n=5
print(square(n))
print()




##1st way (By module name we will access var, char, fun, class)
# import module1
# print(module1.pi)
# module1.square(4)
# module1.welcome('chinmayi','palav')
# module1.login('cee','cee')


# #2nd way (access by alias way or shortcut name)
# import module1 as cee
# cee.login('user', 'user')
# print(cee.pi)
# cee.square(5)


##3rd way (import a specific func/var/class/etc)
# from module1 import login, pi, square,welcome
# print('cee', 'cee')
# print(pi)
# print(7)
# print('chinmayi', 'palav')

##4th way 
from mod1 import *
print(pi)