from builtins import input
while True:
    try:
        a, b = map(int, input().split())
        grades = list(map(int, input().split()))
        for i in range(b):
            command = input().split()
            if command[0] == 'Q':
                start, end = sorted([int(command[1]), int(command[2])])
                print(max(grades[start - 1: end]))
            else:
                grades[int(command[1]) - 1] = int(command[2])
    except:
        break


'''
input:

5 7
1 2 3 4 5
Q 1 5
U 3 6
Q 3 4
Q 4 5
U 4 5
U 2 9
Q 1 5

output:

5
6
5
9
'''
