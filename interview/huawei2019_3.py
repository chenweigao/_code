from builtins import input


class Solution:
    def solution(self, num_cpu, num_task, task):
        task.sort()
        m_task = [0 for _ in range(num_cpu)]
        res = 0
        if num_cpu >= num_task:
            return task[-1]
        else:
            i = 0
            while i < num_cpu:
                m_task[i] = task[i]
                i += 1
            while i < num_task:
                min_t = m_task[0]
                res += min_t
                for j in range(num_cpu):
                    m_task[j] -= min_t
                m_task.pop(0)
                import bisect
                bisect.insort_left(m_task, task[i])
                i += 1
        return res + max(m_task)

# while True:
#     try:
#         num = list(map(int, input().split()))
#         task = list(map(int, input().split()))
#         num_cpu = num[0]
#         num_task = num[1]
#         print(Solution().solution(num_cpu, num_task, task))
#     except:
#         break


num_cpu = 3
num_task = 5
task = [8, 4, 3, 1, 10]
print(Solution().solution(num_cpu, num_task, task))
