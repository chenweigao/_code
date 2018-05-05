def sort_priority(values, group):
    found = False

    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 7, 5}
sort_priority(numbers, group)
print(numbers)
