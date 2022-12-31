




# 1. LeeCode-python队列




队列 (queue) 是一种特殊的线性表，特殊之处在于它只允许在表的前端（front）进行删除操作，而在表的后端（rear）进行插入操作，和栈一样，队列是一种操作受限制的线性表。进行插入操作的端称为队尾，进行删除操作的端称为队头。

```python
import collections
# Create a deque
DoubleEnded = collections.deque(["Mon","Tue","Wed"])
print (DoubleEnded)

# Append to the right
print("Adding to the right: ")
DoubleEnded.append("Thu")
print (DoubleEnded)

# append to the left
print("Adding to the left: ")
DoubleEnded.appendleft("Sun")
print (DoubleEnded)

# Remove from the right
print("Removing from the right: ")
DoubleEnded.pop()
print (DoubleEnded)

# Remove from the left
print("Removing from the left: ")
DoubleEnded.popleft()
print (DoubleEnded)

# Reverse the dequeue
print("Reversing the deque: ")
DoubleEnded.reverse()
print (DoubleEnded)



```
https://www.yiibai.com/python/py_data_structure/python_deque.html






































