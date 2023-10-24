from collections import deque 

q1 = deque()
q1.append(2)
q1.append(4)
q1.append(6)

q1.popleft()

print(q1)

l = list(q1)

print(sum(l))