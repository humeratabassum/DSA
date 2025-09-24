"""Short summary: this MyStack class implements a stack (LIFO) using a single deque (a double-ended queue). The trick is that every push(x) appends x to the right then rotates the queue so that x ends up at the left/front. That makes pop() and top() simple popleft() / q[0] operations that return the most recently pushed item."""

from collections import deque
class MyStack:
    def __init__(self):
        self.q=deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()
        

    def top(self) -> int:
        return self.q[0]
        
    def empty(self) -> bool:
        return len(self.q)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()