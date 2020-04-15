from array import array
a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])

from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)

from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(heapify(data))                      # rearrange the list into heap order
print(heappush(data, -5))                 # add a new entry
print([heappop(data) for i in range(3)])  # fetch the three smallest entries
