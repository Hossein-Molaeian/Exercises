def get_missing_number(lst):
    return set(range(lst[len(lst)-1])[1:]) - set(l)


l = list(range(1, 100))
l.remove(10)
print(get_missing_number(l))
