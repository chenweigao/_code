# Returns the n maximum elements from the provided list. 
# If n is greater than or equal to the provided list's length, then return the original list(sorted in descending order).

def max_n(lst, n=1, reverse=True):
    return sorted(lst, reverse=reverse)[:n]


print(max_n([1, 3, 2, 6]))
print(max_n([1, 3, 2, 6], 2))
