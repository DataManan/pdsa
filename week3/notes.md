# Stacks, Queue and Linked List
## Linked List
-----------

A ***Linked List*** is a data structure that stores sequencial data in itself. 
* A flexible data structure, appending and inserting data in list requires an O(1) time complexity
* However, finding data/Node in the data structure takes O(n) time, since the objects of this data structure are scattered all across the memory of system.

## Arrays
------------

An **array** is also a data structure to store sequential data values. But, they are different than list they have a fixed size and in most languages they can contain elements of same type

* A array have fixed size with
* It has a random access to all the elements in the it, but to append or delete an element from an array can be expensive
### Java
```Java
// in languages such as Java a array has to declared with it size at the time of initialization, same is with languages such as python and C++
int[] arr = new int[10]
// here an array is declared with a size of ten elements in it.
// therefore, it will only contain integers values and no other values.
```

*  However, in very high level languages suvh as python, we can create a list which can have different data types in the list. Python has a list and not an array.
### Python
```Python
mylsit = []
mylist2 = list()
# both are right implementation of list in python language
```
* You can see, unlike java a python has a list from beggining rather than an array.
