from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)
q.pop()
print(q)
#deque(['y', 'a', 'b', 'c', 'x'])
