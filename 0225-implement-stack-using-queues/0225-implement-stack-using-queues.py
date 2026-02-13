from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()


    def push(self, x: int) -> None:
        self.q.append(x)
        for i in range(0, len(self.q)-1):
            self.q.append(self.q.popleft())    

    def pop(self) -> int:
        x = self.q.popleft()
        return x
        
    def top(self) -> int:
        x = self.q[0]
        return x
        

    def empty(self) -> bool:
        if len(self.q) > 0:
            return False
        return True    
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


