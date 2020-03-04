class StackUnderflow(ValueError):
    pass

class SStack():
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self._elems == []:
            raise StackUnderflow("In SStack.top()")
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise StackUnderflow("In SStack.op()")
        return self._elems.pop()


if __name__ == "__main__":
    a = SStack()
    a.push(1)
    a.push(2)
    a.push(3)
    print(a.pop())
    print(a.top())
    a.top()
