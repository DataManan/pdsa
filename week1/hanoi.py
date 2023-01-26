''' ########################################################
this challenge is to implement a stack data structure to solve problem -> tower of hanoi.
Here we have three tower (say), A|B|C. Tower A contains 3 rings, we need to transfer these 3 rings to tower C on at a time such that the order of the rings in tower C is same as it was in tower A.
############################################################'''
# import stack class
from stack import Stack
# implementing stack data
A = Stack()
B = Stack()
C = Stack()

A.push("c")
A.push("b")
A.push("a")

print(A.peek())
A.printstack()
print(A.stackSize())

"""##############################################################
solving for tower of hanoi
#################################################################"""

B.push(A.pop())
B.push(A.pop())
B.printstack()
A.printstack()
C.push(A.pop())
C.push(B.pop())
C.push(B.pop())
B.printstack()
A.printstack()
C.printstack()
