# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")
#     def reverse_linked_list(self):
#         prev = None
#         current = self.head
#         while current:
#             next_node = current.next 
#             current.next = prev    
#             prev = current            
#             current = next_node       
#         self.head = prev  
# llist = LinkedList()
# llist.insert_at_beginning(10)
# llist.insert_at_beginning(20)
# print("Original list:")
# llist.display()
# llist.reverse_linked_list()  
# print("Reversed list:")
# llist.display()


#take a string as a input as a sentence . reverse the even word of that string and replace the original content then print the whole string using python 
# enter a sentence : i love programming in python
# modified sentence : i evol programming ni nohtyp 
# sentence = input("Enter a sentence: ")
# words = sentence.split()
# modified_words = [
#     word[::-1] if i % 2 != 0 else word
#     for i, word in enumerate(words)
# ]
# modified_sentence = ' '.join(modified_words)
# print("Modified sentence:", modified_sentence)

# n=int(input())
# if n%2==1:
#     print("weird")
# elif n%2==0 and n in range(2,5):
#     print("not weird")
# elif n%2==0 and n in  range(6,20):
#     print("Weird")
# elif n%2==0 and n in  range(20,999999):
#     print("not weird")
# else:
#     print("hamse na ho payega")
def lin_search(n,a):
    for i in range(len(n)):
        if  a == n[i]:
            print("mil gaya")
n= eval(input())
n.sort()
a = int(input())
lin_search(n,a)


