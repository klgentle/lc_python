"""
225. Implement Stack using Queues
Easy

Implement a last in first out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).

Implement the MyStack class:

    void push(int x) Pushes element x to the top of the stack.
    int pop() Removes the element on the top of the stack and returns it.
    int top() Returns the element on the top of the stack.
    boolean empty() Returns true if the stack is empty, false otherwise.

Notes:

    You must use only standard operations of a queue, which means only push to back, peek/pop from front, size, and is empty operations are valid.
    Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue), as long as you use only a queue's standard operations.

"""

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queues = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queues.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queues.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queues[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queues



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
