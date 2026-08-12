class MinStack:

    def __init__(self):
        self.array = []
        self.minE = []

    def push(self, val: int) -> None:
        self.array.append(val)
        
        if not self.minE:
            self.minE.append(val)
        else:
            self.minE.append(min(val, self.minE[-1]))

    def pop(self) -> None:
        self.array.pop()
        self.minE.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.minE[-1]
