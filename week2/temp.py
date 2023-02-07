def combinationSort(arr):
    list_1 = M_SortC(arr)
    list_2 = M_Sort2(arr)
    return list_1, list_2

# def reverseList(arr):
#     start = 0
#     end = len(arr) - 1
#     while start < end :
#         temp = arr[start]
#         arr[start] = arr[end]
#         arr[end] = arr[start]
#         end -= 1
#         start += 1
#     return arr


def MergeC(A, B):
    C = []
    if len(A) == 0 and len(B) != 0:
        return B
    elif len(A) != 0 and len(B) == 0:
        return A

    # merging Two non empty list
    while True:
        if A[0][0] > B[0][0]:
          C.append(B.pop(0))
        elif A[0][0] == B[0][0]:
            if A[0][1:] > B[0][1:]:
                C.append(B.pop(0))
            else:
                C.append(A.pop(0))
        else:
          C.append(A.pop(0))
          
        if len(A) == 0 and len(B) != 0:
          C.extend(B)
          break
        elif len(A) != 0 and len(B) == 0:
          C.extend(A)
          break


def Merge2(A, B):
    C = []
    if len(A) == 0 and len(B) != 0:
        return B
    elif len(A) != 0 and len(B) == 0:
        return A

    # merging Two non empty list
    while True:
        if A[0][0] > B[0][0]:
          C.append(B.pop(0))
        elif A[0][0] == B[0][0]:
            if A[0][1:] > B[0][1:]:
                C.append(A.pop(0))
            else:
                C.append(B.pop(0))
        else:
          C.append(A.pop(0))
        if len(A) == 0 and len(B) != 0:
          C.extend(B)
          break
        elif len(A) != 0 and len(B) == 0:
          C.extend(A)
          break

    return C


def M_SortC(L):
    LL1 = L[:(len(L)//2)]
    LL2 = L[(len(L)//2):]
    if len(LL1) < 1 or len(LL2) < 1:
        return MergeC(LL1, LL2)
    A = M_SortC(LL1)
    B = M_SortC(LL2)
    return MergeC(A, B)


def M_Sort2(L):
    LL1 = L[:(len(L)//2)]
    LL2 = L[(len(L)//2):]
    if len(LL1) < 1 or len(LL2) < 1:
        return Merge2(LL1, LL2)
    A = M_Sort2(LL1)
    B = M_Sort2(LL2)
    return Merge2(A, B)

L = ['d34', 'g54', 'd12', 'b87', 'g1', 'c65', 'g40', 'g5', 'd77']

list_tup = combinationSort(L)
print(list_tup)