# import math
# print(math.sqrt(16))

# import math as m
# print(m.sqrt(16))

# from math import*
# print(int(sqrt(12.2)))
# print(floor(12.2))
# print(ceil(12.2))
# print(fabs(12.2))
# print(fabs(-12.2))


#RANDOM MODULE
#This module defines several functions to generate random numbsers and we can use this while developing games 
# from random import*
# for i in range(5):    
#     print(random())

#To genrate random integers between to given numbers
# from random import*
# for i in range(5):    
#     print(randint(1,100000))


#random float values between 2 given numbeers
# from random import*
# for i in range(5):    
#     print(uniform(1,10))



#cchoice() function:
#it wont return random number, it will return a randim object from the given list or tuple
from random import*
list=["cee", "maani", "sujal","pratham", "anuj"]
for i in range(10):
    print(choice(list))