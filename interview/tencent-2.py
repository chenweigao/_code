n, m = input(), list(map(int, input().split()))

m.sort(reverse=True)

sum_niuniu = sum([v for i, v in enumerate(m) if i % 2 == 0])
sum_yangyang = sum([v for i,v in enumerate(m) if i % 2 != 0])

print(sum_niuniu - sum_yangyang)