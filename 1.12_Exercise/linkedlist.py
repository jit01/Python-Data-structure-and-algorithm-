# class Node:
#
#     # Function to initialise the node object
#     def __init__(self, data):
#         self.data = data  # Assign data
#         self.next = None  # Initialize next as null
#
#
# # Linked List class contains a Node object
# class LinkedList:
#
#     # Function to initialize head
#     def __init__(self):
#         self.head = None
#
#     # This function prints contents of linked list
#     # starting from head
#     def printList(self):
#         temp = self.head
#         while (temp):
#             print(temp.data)
#             temp = temp.next
#
#
# # Code execution starts here
# if __name__ == '__main__':
#     # Start with the empty list
#     llist = LinkedList()
#
#     llist.head = Node(1)
#     second = Node(2)
#     third = Node(3)
#
#     llist.head.next = second  # Link first node with second
#     second.next = third  # Link second node with the third node
#
#     llist.printList()
#
# def str_decor(func):
#     def inner(value):
#         list_b = []
#         for i in range(len(value)):
#             if isinstance(i, int):
#                 i = value[i]
#             list_b.insert(1, i)
#         return list_b
#     return inner
#
#
# @str_decor
# def revers(str):
#     pass
#
#
# print(revers('-123'))

def decor(func):
    def inner(a):
        print(f"I'm calling from decorator\t{a+a}")
        return func(a)
    return inner


@decor
def dum_fun(a):
    return f"I'm calling from function\t{a}"


print(dum_fun(10))