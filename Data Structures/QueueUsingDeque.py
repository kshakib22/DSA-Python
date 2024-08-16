from collections import deque

print("Title: Queue with Deque from collections \n")

customQ = deque(maxlen=3)
customQ.append(3)
customQ.append(33)
customQ.append(23)
print(customQ)
customQ.popleft()
print(customQ)
customQ.clear()
print(customQ)