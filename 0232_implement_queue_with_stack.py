# its ok
class MyQueue:

    def __init__(self):
        self.stack = []
        self.buffer = []

    def push(self, x: int) -> None:
        while self.stack:
            self.buffer.append(self.stack.pop())
        self.stack = [x]
        while self.buffer:
            self.stack.append(self.buffer.pop())

    def pop(self) -> int:
        return self.stack.pop()

    def peek(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()