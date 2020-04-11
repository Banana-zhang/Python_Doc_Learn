from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue)
queue.append("Terry")           # Terry arrives
print(queue)
queue.append("Graham")
print(queue)                      # Graham arrives
queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves

print(queue)                          # Remaining queue in order of arrival