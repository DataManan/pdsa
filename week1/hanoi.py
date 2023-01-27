''' ########################################################
this challenge is to implement a stack data structure to solve problem -> tower of hanoi.
Here we have three tower (say), A|B|C. Tower A contains 3 rings, we need to transfer these 3 rings to tower C on at a time such that the order of the rings in tower C is same as it was in tower A.
############################################################'''
# import stack class
from stack import Stack
# implementing stack data
class Hanoi:
    def __init__(self):
        self.newStack = Stack()
