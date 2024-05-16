def remove_first_occurrence(tup, value):
    found = False
    def filter_func(x):
        nonlocal found
        if x == value and not found:
            found = True
            return False
        return True
    
    return tuple(filter(filter_func, tup))

print(remove_first_occurrence((1, 2, 3), 1))
print(remove_first_occurrence((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(remove_first_occurrence((2, 4, 6, 6, 4, 2), 9))
