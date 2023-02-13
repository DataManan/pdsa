def quickSort(L, l, r):
    if (r-l <=1):
        return
    (pivot, lower, upper) = (L[l], l+1, l+1)
    for i in range(l+1, r):
        if L[i] > pivot :
            upper = upper+ 1
        else:
            (L[i], L[lower]) = (L[lower], L[i])

            (lower, upper) = (lower+1, upper+1)
    (L[l], L[lower-1]) = (L[lower-1], L[l])
    lower = lower-1

    quickSort(L, l, lower)
    quickSort(L, lower+1, upper)
    return L


qlist = [5, -100,1,7,10,2,6, 3,8,9,4]

qsort = quickSort(qlist,0,len(qlist))
print(qlist)
