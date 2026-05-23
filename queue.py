class Queue:
    def __init__(self):
        self.size = 5
        self.q = list(range(self.size))

        self.i = 0
        self.o = 0

        self.isEmpty = True
        self.isFull = False

    def _inc(self, val):
        if val + 1 == self.size:
            return 0
        else:
            return val + 1

    def enqueue(self, val):
        if self.isFull:
            raise IndexError("Queue already Full . Cannot Queue")

        self.q[self.i] = val
        self.i = self._inc(self.i)

        self.isEmpty = False

        if self.i == self.o:
            self.isFull = True

    def dequeue(self):
        if self.isEmpty:
            raise IndexError("Queue Empty. Cannot Dequeue")

        ret = self.q[self.o]

        self.o = self._inc(self.o)

        self.isFull = False

        if self.i == self.o:
            self.isEmpty = True

        return ret

    def __str__(self):
        return str(self.q)


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)

print(q)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

