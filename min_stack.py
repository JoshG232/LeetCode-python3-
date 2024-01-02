class MinStack:

    def __init__(self):
        self.arr = []


    def push(self, val: int) -> None:
        self.arr.append(val)


    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:

        return min(self.arr)

obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.pop()
param_3 = obj.top()
print(param_3)
# param_4 = obj.getMin()