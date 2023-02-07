def is_sorted(l):
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            return False
    return True


print(is_sorted([5, 10, 15]))
