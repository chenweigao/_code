import sys 
for line in sys.stdin:
    a = line.split()
    print(a)
    print(int(a[0]) + int(a[1]))