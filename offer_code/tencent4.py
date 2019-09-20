# array = [5, 8, 10, 3, 6, 10, 8]
m, n = [int(_) for _ in input().split()]
array = [int(_) for _ in input().split()]
array = sorted(array)
while n:
    print(array[0])
    temp = array[0]
    del array[0]
    array = [num - temp for num in array if num - temp != 0]
    n -= 1