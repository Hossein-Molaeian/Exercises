def qsort(lst):
    if lst == []:
        return []
    return qsort([x for x in lst[1:] if x < lst[0]]) + lst[0:1] + qsort([x for x in lst[1:] if x >= lst[0]])
