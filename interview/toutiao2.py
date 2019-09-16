from queue import Queue

class Solution:
    def solution(self, tasks):
        q = Queue()
        max_time = 0
        for task in tasks:
            max_time = max(task[0], max_time)
        remain = 0
        for task in tasks:
            q.put(task[1])
        # for _ in q.queue:
        #     remain = sum(q.queue) - max_time + 1
        for _ in q.queue:
            if _ >= 1:
                _ -= 1
        res = remain + max_time
        return q.queue
tasks = [
    [1, 3],
    [2, 3],
    [3, 3]
]


# m = int(input())
# tasks = []
# for i in range(m):
#     temp = [int(_) for _ in input().split()]
#     tasks.append(temp)

res = Solution().solution(tasks)

print(res)
