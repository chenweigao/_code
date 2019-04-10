import sys

number_of_cup, waters = [int(_) for _ in input().split()]
capacities = list(map(int, input().split()))
# for i in range(number_of_cup * 2):
#     line = sys.stdin.readline().strip()
#     values = list(map(int, line.split()))
#     # print(capacities)
#     for v in values:
#         capacities.append(v)
#     break
res = 0
waters_boy = capacities[0]
waters_girl = waters_boy / 2
res = (waters_girl + waters_boy) * number_of_cup
while res > waters:
    waters_boy /= 2
    waters_girl = waters_boy / 2
    res = (waters_girl + waters_boy) * number_of_cup
print("%6f" % res)
